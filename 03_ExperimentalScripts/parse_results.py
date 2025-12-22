"""
Parses all experiment results from a specified `run_experiments.sh` output
directory (which may contain multiple runs) and generates a comprehensive
Markdown report.
"""
import argparse
import os
import glob
import json
from collections import defaultdict

# --- Configuration ---
# These should match the experiment configuration
MODELS = [
    "gemma3:270m", "smollm:360m", "qwen:0.5b", "tinyllama:1.1b", "deepseek-r1:1.5b",
    "stablelm2:1.6b", "qwen:1.8b", "gemma:2b", "falcon3:3b", "llama3.2:3b",
    "phi3:mini", "gemma3:4b", "qwen:4b", "yi:6b", "gemma:7b", "mistral:7b",
    "llama2:7b", "deepseek-llm:7b", "deepseek-r1:8b", "llama3:8b",
]
LANGUAGES = ["ja", "en", "eo", "jbo"]

# Task-specific configurations
SIMPLE_TASKS = ["return_one", "copy_list", "simple_sort", "reverse_sort", "length_sort", "custom_sort"]
DIAGNOSIS_TYPES = ["s_expr", "json", "tsv", "token_test"]
EINSTEIN_TYPES = ["s_expr", "json", "token_test", "cot_baseline"]

# --- Log Parsing Functions ---

def parse_nl_log_file(log_path: str) -> bool:
    """Parses a natural language task log file for a SUCCESS line."""
    if not os.path.exists(log_path):
        return False
    try:
        with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                if "Overall Result" in line and "SUCCESS" in line:
                    return True
        return False
    except IOError:
        return False

def parse_symbolic_log_file(log_path: str) -> bool:
    """Parses a symbolic task log file for a SUCCESS marker."""
    if not os.path.exists(log_path):
        return False
    try:
        with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
            return "🎉 SUCCESS" in f.read()
    except IOError:
        return False

# --- Table Generation Functions ---

def generate_matrix_table(title: str, results: dict, row_keys: list, col_keys: list, row_header: str, col_header: str):
    """Generates a generic Markdown table for matrix-like results (e.g., Model x Language)."""
    print(f"### {title}")
    
    # Header
    header = f"| {row_header} / {col_header} | {' | '.join(col_keys)} |"
    separator = f"| :--- | {' :---: |' * len(col_keys)}"
    print(header)
    print(separator)
    
    # Body
    for row_key in row_keys:
        row = f"| `{row_key}`"
        for col_key in col_keys:
            stats = results.get(row_key, {}).get(col_key, {'success': 0, 'total': 0})
            success_count = stats.get('success', 0)
            total_count = stats.get('total', 0)
            row += f" | {success_count}/{total_count}"
        row += " |"
        print(row)
    print("")

# --- Main ---

def main():
    """Main function to parse all results and generate a full report."""
    parser = argparse.ArgumentParser(description="Parse all experiment results from a single run directory and generate a combined Markdown report.")
    parser.add_argument("results_dir", help="The main directory containing all experiment run subdirectories (e.g., 'symbolic_run_...').")
    args = parser.parse_args()

    if not os.path.isdir(args.results_dir):
        print(f"Error: Directory not found -> {args.results_dir}")
        return
    
    # --- Data Collection ---
    all_results = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: {'success': 0, 'total': 0})))

    for model in MODELS:
        model_clean = model.replace(":", "_").replace("/", "_")

        # 1. Simple Tasks (NL)
        for task in SIMPLE_TASKS:
            for lang in LANGUAGES:
                if task == "custom_sort":
                    base_dir_name = f"simple_task_{task}_{lang}_{model_clean}"
                    run_dirs_path = os.path.join(args.results_dir, base_dir_name, "run_*")
                    run_dirs = glob.glob(run_dirs_path)
                    for run_dir in run_dirs:
                        log_path = os.path.join(run_dir, "execution.log")
                        if os.path.exists(log_path):
                            all_results[task][model][lang]['total'] += 1
                            if parse_nl_log_file(log_path):
                                all_results[task][model][lang]['success'] += 1
                else:
                    for style in ["imperative", "conversational"]:
                        base_dir_name = f"simple_task_{task}_{lang}_{style}_{model_clean}"
                        run_dirs_path = os.path.join(args.results_dir, base_dir_name, "run_*")
                        run_dirs = glob.glob(run_dirs_path)
                        for run_dir in run_dirs:
                            log_path = os.path.join(run_dir, "execution.log")
                            if os.path.exists(log_path):
                                all_results[task][model][lang]['total'] += 1
                                if parse_nl_log_file(log_path):
                                    all_results[task][model][lang]['success'] += 1
        
        # 2. Roundtrip (Symbolic)
        base_dir_name = f"roundtrip_{model_clean}"
        run_dirs_path = os.path.join(args.results_dir, base_dir_name, "run_*")
        run_dirs = glob.glob(run_dirs_path)
        for run_dir in run_dirs:
            log_path = os.path.join(run_dir, "execution.log")
            if os.path.exists(log_path):
                all_results["roundtrip"][model]["sexpr"]['total'] += 1
                if parse_symbolic_log_file(log_path):
                    all_results["roundtrip"][model]["sexpr"]['success'] += 1

        # 3. Diagnosis (Symbolic)
        for test_type in DIAGNOSIS_TYPES:
            base_dir_name = f"diagnosis_{test_type}_{model_clean}"
            run_dirs_path = os.path.join(args.results_dir, base_dir_name, "run_*")
            run_dirs = glob.glob(run_dirs_path)
            for run_dir in run_dirs:
                log_path = os.path.join(run_dir, "execution.log")
                if os.path.exists(log_path):
                    all_results["diagnosis"][model][test_type]['total'] += 1
                    if parse_symbolic_log_file(log_path):
                        all_results["diagnosis"][model][test_type]['success'] += 1
                        
        # 4. Einstein
        for test_type in EINSTEIN_TYPES:
            if test_type == "cot_baseline": # NL Task
                for lang in LANGUAGES:
                    base_dir_name = f"einstein_{test_type}_{lang}_{model_clean}"
                    run_dirs_path = os.path.join(args.results_dir, base_dir_name, "run_*")
                    run_dirs = glob.glob(run_dirs_path)
                    for run_dir in run_dirs:
                        log_path = os.path.join(run_dir, "execution.log")
                        if os.path.exists(log_path):
                            all_results["einstein"][model][f"cot_{lang}"]['total'] += 1
                            if parse_nl_log_file(log_path):
                                 all_results["einstein"][model][f"cot_{lang}"]['success'] += 1
            else: # Symbolic Task
                base_dir_name = f"einstein_{test_type}_{model_clean}"
                run_dirs_path = os.path.join(args.results_dir, base_dir_name, "run_*")
                run_dirs = glob.glob(run_dirs_path)
                for run_dir in run_dirs:
                    log_path = os.path.join(run_dir, "execution.log")
                    if os.path.exists(log_path):
                        all_results["einstein"][model][test_type]['total'] += 1
                        if parse_symbolic_log_file(log_path):
                            all_results["einstein"][model][test_type]['success'] += 1



        # 5. Filtered List Test (NL)
        for lang in LANGUAGES:
            base_dir_name = f"filtered_list_{lang}_{model_clean}"
            run_dirs_path = os.path.join(args.results_dir, base_dir_name, "run_*")
            run_dirs = glob.glob(run_dirs_path)
            for run_dir in run_dirs:
                log_path = os.path.join(run_dir, "execution.log")
                if os.path.exists(log_path):
                    all_results["filtered_list"][model][lang]['total'] += 1
                    if parse_nl_log_file(log_path):
                        all_results["filtered_list"][model][lang]['success'] += 1

    # --- Report Generation ---
    print("# Experiment Results Summary\n")
    
    for task in SIMPLE_TASKS:
        generate_matrix_table(f"{task.replace('_', ' ').title()} Success Rates", all_results[task], MODELS, LANGUAGES, "Model", "Language")
        
    generate_matrix_table("Roundtrip (Fibonacci S-Expr) Success Rates", all_results["roundtrip"], MODELS, ["sexpr"], "Model", "Format")
    generate_matrix_table("Diagnosis Logic Success Rates", all_results["diagnosis"], MODELS, DIAGNOSIS_TYPES, "Model", "Format")
    
    # Custom columns for Einstein
    einstein_cols = [t for t in EINSTEIN_TYPES if t != "cot_baseline"] + [f"cot_{lang}" for lang in LANGUAGES]
    generate_matrix_table("Einstein Riddle Success Rates", all_results["einstein"], MODELS, einstein_cols, "Model", "Format/Language")
    generate_matrix_table("Filtered List Success Rates", all_results["filtered_list"], MODELS, LANGUAGES, "Model", "Language")

if __name__ == "__main__":
    main()