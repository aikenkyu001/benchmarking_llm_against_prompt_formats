This is the initial public release of the complete experimental environment, dataset, and manuscript for the research paper: **"Benchmarking LLM Sensitivity to Prompt Formats: A Contamination-Free Approach."**

This repository provides all the necessary artifacts to fully reproduce the experiments and validate the findings presented in the paper. We hope this work contributes to a more rigorous and nuanced understanding of Large Language Model capabilities.

#### What's Included in this Release:

*   📄 **Manuscript**: The full research paper in both LaTeX (`.tex`) and PDF (`.pdf`) formats, meticulously revised for clarity and academic rigor.
*   🧪 **Experimental Framework**: A complete, self-contained suite of Python scripts (`03_ExperimentalScripts/`) and `pytest` definitions (`06_TestDefinitions/`) to run all benchmark tests from scratch.
*   📊 **Raw Data**: The complete, unprocessed raw logs from all benchmark runs, available in the `02_RawData/` directory, ensuring full transparency.
*   📈 **Analysis Scripts**: Python scripts to parse the raw data (`parse_results.py`) and generate the summary tables and rankings (`calculate_overall_ranking.py`) presented in the paper.
*   🎨 **Figure Sources**: The complete source code for all figures in the paper, including PlantUML (`.pu`) and Vega-Lite (`.json` in `figure5_en.md`) definitions.

#### DOI and Archiving

This repository release is permanently archived on Zenodo to ensure long-term availability and to provide a citable digital object identifier (DOI).

*   **DOI**: `https://doi.org/10.5281/zenodo.18043860`

#### How to Cite This Work

If you use this software, dataset, or refer to our findings in your research, please cite this release:

```
Fumio Miyata. (2025). Benchmarking LLM Sensitivity to Prompt Formats: A Contamination-Free Approach (v1.0.0) [Software]. Zenodo. https://doi.org/10.5281/zenodo.18043860
```