#!/bin/bash

# Do not use 'set -e' so the script doesn't stop on error

# --- Default Values ---
OLLAMA_BASE_URL="http://10.5.42.169:11434"
EXPERIMENTS_TO_RUN="all" # Default is to run all experiments
NUM_RUNS=1 # Default number of runs
START_INDEX=1 # Default start index for run numbering
DEFAULT_LANGUAGES=("en" "ja" "eo" "jbo")
LANGUAGES=("${DEFAULT_LANGUAGES[@]}")
DEFAULT_STYLE="imperative" # New default style
STYLE="$DEFAULT_STYLE" # New style variable

# Default to all models mentioned in the paper
DEFAULT_MODELS=(
    "gemma3:270m" "smollm:360m" "qwen:0.5b" "tinyllama:1.1b" "deepseek-r1:1.5b" "stablelm2:1.6b"
    "qwen:1.8b" "gemma:2b" "falcon3:3b" "llama3.2:3b" "phi3:mini" "gemma3:4b" "qwen:4b"
    "yi:6b" "gemma:7b" "mistral:7b" "llama2:7b" "deepseek-llm:7b" "deepseek-r1:8b" "llama3:8b"
)
MODELS=("${DEFAULT_MODELS[@]}")
# Get the absolute path of the script
SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
RAW_DATA_DIR="$SCRIPT_DIR/../02_RawData"
mkdir -p "$RAW_DATA_DIR"

# --- Help Function ---
usage() {
  echo "Usage: $0 [-u <url>] [-m \"<models>\"] [-e \"<experiments>\"] [-n <num_runs>] [-i <start_index>] [-l \"<languages>\"] [-s <style>]"
  echo "  -u  Base URL for the Ollama API (default: http://10.5.42.169:11434)"
  echo "  -m  List of models to use for testing (space-separated). (default: all models from the paper)"
  echo "  -e  List of experiment keywords to run (comma-separated). (default: all)"
  echo "      Available keywords: roundtrip, diagnosis, einstein, simple_tasks, filtered_list"
  echo "  -n  Number of times to run each test (default: 1)."
  echo "  -i  Starting number for run directories (e.g., run_006). (default: 1)."
  echo "  -l  List of languages for CoT tests (space-separated). (default: en ja eo jbo)"
  echo "  -s  Prompt style for simple tasks (imperative or conversational). (default: imperative)"
  exit 1
}

# --- Argument Parsing ---
while getopts ":u:m:e:l:s:n:i:" opt; do
  case ${opt} in
    u )
      OLLAMA_BASE_URL=$OPTARG
      ;;
    m )
      read -r -a MODELS <<< "$OPTARG"
      ;;
    e )
      EXPERIMENTS_TO_RUN=$OPTARG
      ;;
    n )
      NUM_RUNS=$OPTARG
      ;;
    i )
      START_INDEX=$OPTARG
      ;;
    l )
      read -r -a LANGUAGES <<< "$OPTARG"
      ;;
    s )
      if [[ "$OPTARG" != "imperative" && "$OPTARG" != "conversational" ]]; then
        echo "Error: -s requires 'imperative' or 'conversational'." >&2
        usage
      fi
      STYLE=$OPTARG
      ;;
    \? )
      usage
      ;;
    : )
      echo "Error: Option -$OPTARG requires an argument." >&2
      usage
      ;;
  esac
done
shift $((OPTIND -1))

# --- Pre-run Configuration Check ---
OLLAMA_API_URL="${OLLAMA_BASE_URL%/}/api/generate"

echo "Starting experiments with the following settings:"
echo "Ollama API URL:    $OLLAMA_API_URL"
echo "Models to test:    ${MODELS[*]}"
echo "Experiments to run: $EXPERIMENTS_TO_RUN"
echo "Number of runs per test: $NUM_RUNS"
echo "Starting run number:   $START_INDEX"
echo "Languages for CoT: ${LANGUAGES[*]}"
echo "Prompt Style:      $STYLE"
echo "=================================================="

# --- Main Output Directory ---
MAIN_RUN_ID="symbolic_run_$(date +%Y%m%d_%H%M%S)"
MAIN_OUTPUT_DIR="$RAW_DATA_DIR/$MAIN_RUN_ID"
mkdir -p "$MAIN_OUTPUT_DIR"

echo "Main output will be saved in: $MAIN_OUTPUT_DIR"
echo "=================================================="

END_INDEX=$(($START_INDEX + $NUM_RUNS - 1))
for i in $(seq -f "%03g" $START_INDEX $END_INDEX); do
  echo ""
  echo "**************************************************"
  echo "### Starting Run $i ###"
  echo "**************************************************"

  # --- Main Loop per Model ---
  for MODEL in "${MODELS[@]}"; do
    echo ""
    echo "##################################################"
    echo "### Starting all experiments for model: $MODEL (Run $i) ###"
    echo "##################################################"

    MODEL_CLEAN=$(echo "$MODEL" | sed 's|[/:]|_|g')

    # --- Experiment 0: Simple Natural Language Tasks ---
    if [[ "$EXPERIMENTS_TO_RUN" == "all" || "$EXPERIMENTS_TO_RUN" == *"simple_tasks"* ]]; then
      SIMPLE_TASKS=("return_one" "copy_list" "simple_sort" "reverse_sort" "length_sort" "custom_sort")

      for TASK in "${SIMPLE_TASKS[@]}"; do
        for LANG in "${LANGUAGES[@]}"; do
          # --- Conditionally run tasks based on whether they support the --style argument ---
          if [ "$TASK" == "custom_sort" ]; then
            echo ""
            echo ">>> Experiment: Running Simple Task ($TASK, lang: $LANG, run: $i)..."
            BASE_DEST_DIR="$MAIN_OUTPUT_DIR/simple_task_${TASK}_${LANG}_${MODEL_CLEAN}"
            RUN_DEST_DIR="$BASE_DEST_DIR/run_${i}"
            mkdir -p "$RUN_DEST_DIR"
            (python3 "$SCRIPT_DIR/run_${TASK}_test.py" \
              --ollama-url "$OLLAMA_API_URL" \
              --output-dir "$RUN_DEST_DIR" \
              --model "$MODEL" \
              --lang "$LANG") > "$RUN_DEST_DIR/execution.log" 2>&1 || echo "   [!] Simple Task ($TASK, $LANG, run: $i) failed. Continuing..."
            echo ">>> Simple Task ($TASK, $LANG, run: $i) finished. See results in $RUN_DEST_DIR"
          else
            echo ""
            echo ">>> Experiment: Running Simple Task ($TASK, lang: $LANG, style: $STYLE, run: $i)..."
            BASE_DEST_DIR="$MAIN_OUTPUT_DIR/simple_task_${TASK}_${LANG}_${STYLE}_${MODEL_CLEAN}"
            RUN_DEST_DIR="$BASE_DEST_DIR/run_${i}"
            mkdir -p "$RUN_DEST_DIR"
            (python3 "$SCRIPT_DIR/run_${TASK}_test.py" \
              --ollama-url "$OLLAMA_API_URL" \
              --output-dir "$RUN_DEST_DIR" \
              --model "$MODEL" \
              --lang "$LANG" \
              --style "$STYLE") > "$RUN_DEST_DIR/execution.log" 2>&1 || echo "   [!] Simple Task ($TASK, $LANG, $STYLE, run: $i) failed. Continuing..."
            echo ">>> Simple Task ($TASK, $LANG, $STYLE, run: $i) finished. See results in $RUN_DEST_DIR"
          fi
          sleep 1
        done
      done
    fi

    # --- Experiment 1: Round-Trip Test (Fibonacci) ---
    if [[ "$EXPERIMENTS_TO_RUN" == "all" || "$EXPERIMENTS_TO_RUN" == *"roundtrip"* ]]; then
      echo ""
      echo ">>> Experiment: Running Round-Trip Test (Fibonacci S-Expr, run: $i)..."
      BASE_DEST_DIR="$MAIN_OUTPUT_DIR/roundtrip_${MODEL_CLEAN}"
      RUN_DEST_DIR="$BASE_DEST_DIR/run_${i}"
      mkdir -p "$RUN_DEST_DIR"
      (python3 "$SCRIPT_DIR/run_final_symbolic_benchmark.py" \
        --ollama-url "$OLLAMA_API_URL" \
        --output-dir "$RUN_DEST_DIR" \
        --model "$MODEL") > "$RUN_DEST_DIR/execution.log" 2>&1 || echo "   [!] Round-Trip Test (run: $i) failed. Continuing..."
      echo ">>> Round-Trip Test (run: $i) finished. See results in $RUN_DEST_DIR"
      sleep 1
    fi

    # --- Experiment 2: Diagnosis Logic Test (All Variants) ---
    if [[ "$EXPERIMENTS_TO_RUN" == "all" || "$EXPERIMENTS_TO_RUN" == *"diagnosis"* ]]; then
      DIAGNOSIS_TEST_TYPES=("s_expr" "json" "tsv" "token_test")

      for TEST_TYPE in "${DIAGNOSIS_TEST_TYPES[@]}"; do
        echo ""
        echo ">>> Experiment: Running Diagnosis Logic Test ($TEST_TYPE, run: $i)..."
        BASE_DEST_DIR="$MAIN_OUTPUT_DIR/diagnosis_${TEST_TYPE}_${MODEL_CLEAN}"
        RUN_DEST_DIR="$BASE_DEST_DIR/run_${i}"
        mkdir -p "$RUN_DEST_DIR"
        (python3 "$SCRIPT_DIR/run_diagnosis_logic_test.py" \
          --ollama-url "$OLLAMA_API_URL" \
          --output-dir "$RUN_DEST_DIR" \
          --model "$MODEL" \
          --test-type "$TEST_TYPE") > "$RUN_DEST_DIR/execution.log" 2>&1 || echo "   [!] Diagnosis Logic Test ($TEST_TYPE, run: $i) failed. Continuing..."
        echo ">>> Diagnosis Logic Test ($TEST_TYPE, run: $i) finished. See results in $RUN_DEST_DIR"
        sleep 1
      done
    fi

    # --- Experiment 3: Einstein's Riddle (All Variants) ---
    if [[ "$EXPERIMENTS_TO_RUN" == "all" || "$EXPERIMENTS_TO_RUN" == *"einstein"* ]]; then
      EINSTEIN_TEST_TYPES=("s_expr" "token_test" "cot_baseline" "json")

      for TEST_TYPE in "${EINSTEIN_TEST_TYPES[@]}"; do
        if [ "$TEST_TYPE" == "cot_baseline" ]; then
          # Loop through languages for CoT baseline
          for LANG in "${LANGUAGES[@]}"; do
            echo ""
            echo ">>> Experiment: Running Einstein's Riddle ($TEST_TYPE, lang: $LANG, run: $i)..."
            BASE_DEST_DIR="$MAIN_OUTPUT_DIR/einstein_${TEST_TYPE}_${LANG}_${MODEL_CLEAN}"
            RUN_DEST_DIR="$BASE_DEST_DIR/run_${i}"
            mkdir -p "$RUN_DEST_DIR"
            (python3 "$SCRIPT_DIR/run_einstein_riddle_test.py" \
              --ollama-url "$OLLAMA_API_URL" \
              --output-dir "$RUN_DEST_DIR" \
              --model "$MODEL" \
              --test-type "$TEST_TYPE" \
              --lang "$LANG") > "$RUN_DEST_DIR/execution.log" 2>&1 || echo "   [!] Einstein Riddle ($TEST_TYPE, $LANG, run: $i) failed. Continuing..."
            echo ">>> Einstein Riddle ($TEST_TYPE, $LANG, run: $i) finished. See results in $RUN_DEST_DIR"
            sleep 1
          done
        else
          # Run non-CoT tests once
          echo ""
          echo ">>> Experiment: Running Einstein's Riddle ($TEST_TYPE, run: $i)..."
          BASE_DEST_DIR="$MAIN_OUTPUT_DIR/einstein_${TEST_TYPE}_${MODEL_CLEAN}"
          RUN_DEST_DIR="$BASE_DEST_DIR/run_${i}"
          mkdir -p "$RUN_DEST_DIR"
          (python3 "$SCRIPT_DIR/run_einstein_riddle_test.py" \
            --ollama-url "$OLLAMA_API_URL" \
            --output-dir "$RUN_DEST_DIR" \
            --model "$MODEL" \
            --test-type "$TEST_TYPE") > "$RUN_DEST_DIR/execution.log" 2>&1 || echo "   [!] Einstein Riddle ($TEST_TYPE, run: $i) failed. Continuing..."
          echo ">>> Einstein Riddle ($TEST_TYPE, run: $i) finished. See results in $RUN_DEST_DIR"
          sleep 1
        fi
      done
    fi





    # --- Experiment 4: Filtered List Test ---
    if [[ "$EXPERIMENTS_TO_RUN" == "all" || "$EXPERIMENTS_TO_RUN" == *"filtered_list"* ]]; then
      for LANG in "en" "ja" "eo" "jbo"; do # Assuming all 4 languages are supported for this test.
        echo ""
        echo ">>> Experiment: Running Filtered List Test (lang: $LANG, run: $i)..."
        BASE_DEST_DIR="$MAIN_OUTPUT_DIR/filtered_list_${LANG}_${MODEL_CLEAN}"
        RUN_DEST_DIR="$BASE_DEST_DIR/run_${i}"
        PROMPT_FILE_PATH="$SCRIPT_DIR/../04_Prompts/$LANG/prompt_filtered_list_${LANG}.txt"
        mkdir -p "$RUN_DEST_DIR"
        (python3 "$SCRIPT_DIR/run_filtered_list_test.py" \
          --ollama-url "$OLLAMA_API_URL" \
          --output-dir "$RUN_DEST_DIR" \
          --model "$MODEL" \
          --prompt-file "$PROMPT_FILE_PATH") > "$RUN_DEST_DIR/execution.log" 2>&1 || echo "   [!] Filtered List Test ($LANG, run: $i) failed. Continuing..."
        echo ">>> Filtered List Test ($LANG, run: $i) finished. See results in $RUN_DEST_DIR"
        sleep 1
      done
    fi

    echo "### All experiments for model: $MODEL (Run $i) finished ###"
  done
done

echo ""
echo "=================================================="
echo "All runs have completed."
echo "Check the results in $MAIN_OUTPUT_DIR"

