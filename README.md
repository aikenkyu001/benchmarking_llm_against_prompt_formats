# Benchmarking Large Language Models Against Prompt Formats

This repository serves as the official experimental environment and accompanying resources for the research paper titled "Benchmarking Large Language Models Against Prompt Formats: Experimental Methods and Results." It provides a comprehensive, self-contained, and reproducible framework for investigating how Large Language Models (LLMs) respond to various prompt formats, languages, styles, and symbolic representations.

Here you will find:
- **Paper Manuscripts:** Drafts of the research paper in both English and Japanese.
- **Experimental Scripts:** Python scripts for running the benchmarks and analyzing results.
- **Prompt Definitions:** The diverse set of prompts used in the experiments.
- **Test Definitions:** Pytest definitions for validating LLM-generated code.
- **Raw Data:** Raw output logs from the benchmark runs.

This project aims to offer an objective and data-driven understanding of LLM capabilities and limitations, particularly in handling formal and ambiguous languages. For more details, please refer to the paper manuscripts within the `01_Manuscripts/` directory.

---

# Experimental Environment: Verifying the Computational Properties of Large Language Models

This directory contains a self-contained experimental environment to verify the claims made in the paper "A Study on the Computational Properties of Large Language Models and the Feasibility of Artificial General Intelligence." This environment is publicly available at [https://github.com/aikenkyu001/benchmarking_llm_against_prompt_formats](https://github.com/aikenkyu001/benchmarking_llm_against_prompt_formats).

## Overview

This experimental environment is provided to allow readers to accurately reproduce the experiments reported in the paper "Benchmarking Large Language Models Against Prompt Formats: Experimental Methods and Results."

The purpose of this paper is not to assert a specific theory, but to provide an objective and reproducible benchmark dataset that measures how LLM responses change with the format of the prompt (language, style, syntax).

## Implemented Tests

This section details the benchmark tests included in this environment.

| Prompt Structure | Task Name | Description |
| :--- | :--- | :--- |
| **Natural Language** | `return_one`, `copy_list`, `simple_sort`, `reverse_sort`, `length_sort` | A suite of five simple tasks to generate a function that performs a basic operation. These tests are conducted across four natural languages (English, Japanese, Esperanto, Lojban) and two prompt styles (imperative and conversational) to evaluate baseline code generation and language understanding. |
| **Natural Language** | `custom_sort` | Generates a function that sorts a list of strings first by length, then alphabetically. This tests the ability to handle multiple constraints in natural language. |
| **Natural Language** | `filtered_list` | Tests the model's ability to follow complex logical instructions (return even numbers, but not 8) and adhere to a strict output format. **The model must return only the resulting list as a string, without generating any Python code.** This rigorously tests instruction-following capabilities. |
| **Symbolic (S-Expression)** | `roundtrip` | Transpiles an S-expression script defining a Fibonacci sequence generator into a Python function, testing symbolic language translation. |
| **Symbolic Suite** | `diagnosis_s_expr`, `diagnosis_json`, `diagnosis_tsv`, `diagnosis_token_test` | Generates a Python function that implements a simple medical diagnosis logic based on rules defined in four different symbolic formats (S-expression, JSON, TSV, and a custom token-based language). |
| **Symbolic Suite** | `einstein_s_expr`, `einstein_json` | Solves Einstein's Riddle by interpreting the puzzle's rules and constraints defined in S-expressions and JSON, respectively. |
| **Symbolic (Token-based)** | `einstein_token_test` | An extremely challenging test of a model's advanced capabilities. It requires the model to: 1) learn the grammar of an unknown, custom token-based language on the fly from rules provided in the prompt, 2) learn an efficient backtracking algorithm from a single example (Few-Shot), and 3) apply this knowledge to solve the complex Einstein's Riddle. |
| **Structured Natural Language (CoT)** | `einstein_cot_baseline` | Solves Einstein's Riddle using a natural language, Chain-of-Thought (CoT) prompt. This test is conducted across four natural languages (English, Japanese, Esperanto, Lojban). |
| **Lojban Specific** | `lojban_understanding` | A supplementary test to probe the fundamental understanding of Lojban. It includes bidirectional translation tasks (Lojban <=> EN/JA/EO) and a simple Lojban-to-Python code generation task. This test was added to further investigate the low performance on other Lojban tasks. |

## Known Issues and Findings

This section documents key challenges and findings discovered during the development and execution of these benchmarks, which highlight the current limitations of large language models.

*   **`Einstein Riddle - token_test`**: This test remains unsolved by all tested models (as of Dec 2025). While advanced models (e.g., `llama3:8b`) were able to learn the custom language's grammar and mimic the correct backtracking algorithm from the prompt's example, they consistently failed to produce a **bug-free implementation**. The generated code often contained subtle logic errors (e.g., `KeyError`, incorrect state management in recursion), indicating that while models can imitate algorithmic structure, implementing complex, bug-free logic remains a significant hurdle.

*   **`Filtered List (jbo)`**: This test also remains unsolved by all models. The failure is attributed to the task's nature: it requires the model to perform direct logical reasoning and filtering **using Lojban itself** and to output a result without generating any Python code. In contrast, other tests where Lojban was successful (e.g., `Simple Sort`) required the model to "transpile" a Lojban specification into Python code. This suggests that current models have some ability to translate Lojban to a familiar language like Python, but struggle significantly with performing direct, complex reasoning and instruction-following within Lojban.

*   **Lojban Understanding (Supplementary Test)**: Following the poor performance in multi-language tasks, a dedicated Lojban test was conducted. It revealed a **total failure (0% success)** across all 20 models in both basic bidirectional translation and simple code generation from Lojban. Models either repeated the input, hallucinated incorrect translations, or failed to produce any valid code. This strongly indicates that the models lack a foundational, semantic understanding of Lojban, and any prior successes were likely due to superficial pattern matching between Lojban-like syntax and specific code structures in the training data, rather than true comprehension.

## Execution Instructions

### Setting up the Environment

To reproduce the experiments, a Python virtual environment is recommended.

1.  **Create Virtual Environment:**
    ```bash
    python3 -m venv venv
    ```

2.  **Activate Environment:**
    *   macOS / Linux: `source venv/bin/activate`
    *   Windows: `venv\Scripts\activate`

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ollama Server:**
    Ensure an Ollama server is running. The scripts default to `http://127.0.0.1:11434` but can be overridden with the `-u` flag.

### Reproducing All Experiment Suites

The `run_experiments.sh` script in `03_ExperimentalScripts` is the main orchestrator.

*   **Flags:**
    *   `-u <url>`: Ollama server URL.
    *   `-m "<models>"`: Space-separated list of models (e.g., `"gemma:2b tinyllama"`).
    *   `-e <experiments>`: Comma-separated list of keywords: `roundtrip`, `diagnosis`, `einstein`, `simple_tasks`, `filtered_list`. Default: `all`.
    *   `-n <num_runs>`: Number of runs per test. Default: `1`.
    *   `-l "<languages>"`: Space-separated list of languages. Default: `"en ja eo jbo"`.
    *   `-s <style>`: Prompt style for simple tasks (`imperative` or `conversational`). Default: `imperative`.

*   **Example:**
    ```bash
    # Run all 'simple_tasks' for Japanese across all default models
    ./03_ExperimentalScripts/run_experiments.sh -e "simple_tasks" -l "ja"
    ```

### Analyzing Results

Analysis is a two-step process to generate the summary tables used in the paper.

1.  **Generate Detailed Summary:**
    First, use `parse_results.py` to parse the raw log files from a results directory (e.g., `02_RawData/symbolic_run_...`) into a detailed markdown summary. It is recommended to pipe this output to a file.

    ```bash
    python3 ./03_ExperimentalScripts/parse_results.py 02_RawData/your_run_directory_name/ > detailed_summary.md
    ```

2.  **Calculate Overall Ranking:**
    Next, use `calculate_overall_ranking.py` on the generated summary file to produce the final overall performance ranking table, which can be inserted into the paper's analysis section.

    ```bash
    python3 ./03_ExperimentalScripts/calculate_overall_ranking.py detailed_summary.md
    ```