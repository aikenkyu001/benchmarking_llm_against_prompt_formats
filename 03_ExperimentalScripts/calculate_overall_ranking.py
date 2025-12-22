import sys
import re
from collections import defaultdict

def calculate_ranking(file_path):
    """
    Parses a markdown file containing experiment result tables, calculates
    the overall success rate for each model, and prints a sorted markdown table.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}", file=sys.stderr)
        sys.exit(1)

    # --- Data Extraction ---
    # defaultdict is useful for accumulating scores
    model_scores = defaultdict(lambda: {'success': 0, 'total': 0})

    # Use a more specific regex anchored to the start of the line.
    # This ensures we only match lines that are actual data rows in the table.
    model_regex = r"^\s*\|\s*`([^`]+)`"
    
    lines = content.split('\n')
    for line in lines:
        match = re.search(model_regex, line)
        if match:
            model_name = match.group(1).strip()
            
            # Find all score fractions 'X/Y' in the rest of the line
            scores = re.findall(r'(\d+)/(\d+)', line)
            
            for success, total in scores:
                model_scores[model_name]['success'] += int(success)
                model_scores[model_name]['total'] += int(total)

    # --- Calculation and Sorting ---
    if not model_scores:
        print("No model scores found in the file.", file=sys.stderr)
        sys.exit(1)

    calculated_ranks = []
    for model, scores in model_scores.items():
        if scores['total'] > 0:
            rate = (scores['success'] / scores['total']) * 100
            calculated_ranks.append((model, rate))

    # Sort by success rate (descending)
    sorted_ranks = sorted(calculated_ranks, key=lambda item: item[1], reverse=True)

    # --- Markdown Table Generation ---
    print("#### 5.4.1. 総合性能ランキング")
    print("\n全テストを横断した各モデルの平均成功率を示す。全体的なタスク遂行能力を測る基本的な指標となる。")
    print("\n| モデル              |   総合成功率 |")
    print("|:-----------------|-----------:|")
    for model, rate in sorted_ranks:
        # Pad model name for alignment
        print(f"| {model:<16} | {rate:>8.2f}% |")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python calculate_overall_ranking.py <path_to_summary_file.md>", file=sys.stderr)
        sys.exit(1)
    
    markdown_file = sys.argv[1]
    calculate_ranking(markdown_file)
