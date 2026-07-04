# WL-Literature-study
# Automated Literature Text Mining & Bibliometric Analytics

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An automated text-mining pipeline designed to parse, extract, and synthesize structured insights from large-scale scientific literature cohorts. 

By leveraging regular expressions (Regex) and natural language heuristics, this toolkit extracts critical study metadata—such as biomedical biological data sources, cohort sample sizes, and specific machine learning methodologies—directly from publication abstracts.

---

## Project Workflow & Architecture

The repository is structured to cleanly separate the text-mining backend from the downstream data visualization dashboard:

```text
WL-Literature-study/
│
├── notebooks/
│   └── literature_visualization.ipynb 
├── src/
│   └── literature_miner.py            # Core Regex-based information extraction script
│
├── .gitignore                         # Prevents tracking of raw literature sheets
├── LICENSE                            # MIT License
└── README.md                          # Project documentation
