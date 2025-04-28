# Data Governance Framework for Water Potability Dataset

A **mini data governance framework** implemented in GitHub, designed to manage, document, and analyse the Water Potability dataset through policy documentation, metadata cataloging, automated quality checks, exploratory data analysis, and machine learning models.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Repository Structure](#repository-structure)
3. [Getting Started](#getting-started)
4. [Data Cleaning & Sampling](#data-cleaning--sampling)
5. [Quality Checks](#quality-checks)
6. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
7. [Model Training](#model-training)
8. [Automation & CI](#automation--ci)
9. [Data Governance Documentation](#data-governance-documentation)
10. [Maintenance & Review](#maintenance--review)
11. [Contributing](#contributing)
12. [License](#license)

---

## Project Overview

The goal of this project is to establish a **lightweight data governance framework** around the Water Potability dataset, focusing on:

- **Policy definition**: Access control, classification, retention policies
- **Metadata catalog**: Structured YAML template and examples
- **Data quality**: Automated checks via Python and SQL
- **EDA**: Notebook-driven analysis of water quality attributes
- **Machine learning**: Baseline and advanced models predicting potability
- **Automation**: CI pipeline for linting and quality checks
- **Maintenance**: Defined cadence for policy and data review

---

## Repository Structure

```
├── data/
│   ├── water_quality_dataset_100k.csv               ← Full raw dataset (ignored by Git)
│   └── water_potability_clean_sample.csv    ← Cleaned + sampled CSV (~5%)
├── docs/
│   ├── policies/                            ← Core governance policies
│   ├── lineage.md                           ← Data lineage flowchart
│   ├── automation.md                        ← CI and tooling instructions
│   ├── roles.md                             ← Data governance role definitions
│   ├── inventory.md                         ← Data asset inventory table
│   └── README.md                            ← Detailed Getting Started guide
├── examples/
│   └── catalog/                             ← Filled metadata catalog examples
├── scripts/
│   ├── clean_and_sample.py                  ← Cleanup, imputation, sampling script
│   └── reduce_data.py                       ← (Optional) column and row sampling
├── src/
│   ├── quality_checks/
│   │   ├── checks.py                        ← Python data quality checks
│   │   └── checks.sql                       ← SQL-based quality checks
│   └── models/
│       ├── train_model.py                   ← Training scripts for four classifiers
│       └── README.md                        ← Model training instructions
├── .github/workflows/ci.yml                 ← GitHub Actions for linting & checks
├── .gitattributes                          ← Git LFS tracking for large CSVs
├── .gitignore                              ← Ignored files
└── README.md                                ← This file
```

---

## Getting Started

### Prerequisites

- **Git** (with [Git LFS](https://git-lfs.github.com/) installed)
- **Python** 3.7+
- **pip** package manager

### Clone the repository

```bash
git clone https://github.com/martinktay/data-governance-framework.git
cd data-governance-framework
```

### Install Python dependencies

```bash
pip install pandas scikit-learn xgboost lightgbm
```

### Prepare the data

1. Ensure Git LFS is set up and the clean sample CSV is downloaded:
   ```bash
   git lfs pull
   ```
2. The raw dataset (`data/water_portability.csv`) is ignored; use the clean sample:
   ```bash
   ls data/water_potability_clean_sample.csv
   ```

---

## Data Cleaning & Sampling

The `scripts/clean_and_sample.py` script:

1. Loads the full CSV (locally, outside of Git).  
2. Drops columns with >3% missing values (`Copper`, `Sulfate`, `Fluoride`, `Odor`).  
3. Imputes remaining nulls (median for numeric, mode for categorical).  
4. Keeps core columns.  
5. Samples 5% of rows.  
6. Writes `data/water_potability_clean_sample.csv`.

```bash
python scripts/clean_and_sample.py
```

---

## Quality Checks

### Python-based checks

Run the checks via:

```bash
python src/quality_checks/checks.py
```

This prints:
- Overall completeness  
- Null counts per column  
- Range validity (e.g., pH between 0–14)  
- Categorical value checks  
- Target distribution

### SQL-based checks

Run against your database:

```bash
sqlite3 water.db < src/quality_checks/checks.sql
```

---

## Exploratory Data Analysis (EDA)

The Jupyter notebook `notebooks/eda_water_potability.ipynb` walks you through:
- Data loading and structure (`df.info()`)  
- Descriptive statistics (`df.describe()`)  
- Distribution plots  
- Correlation matrix  
- Crosstabs by source and target

Launch it with:

```bash
jupyter lab notebooks/eda_water_potability.ipynb
```

---

## Model Training

Train and compare four classifiers in `src/models/train_model.py`:
- RandomForest  
- XGBoost  
- LightGBM  
- MLPClassifier

Run:

```bash
python src/models/train_model.py
```

See `src/models/README.md` for details.

---

## Automation & CI

On each push, GitHub Actions will:
1. Lint all Markdown files  
2. Install pandas and run Python quality checks

View the pipeline in `.github/workflows/ci.yml` under the **Actions** tab.

---

## Data Governance Documentation

- **Roles**: `docs/roles.md`  
- **Policies**: `docs/policies/*.md`  
- **Inventory**: `docs/inventory.md`  
- **Metadata Catalog**: `tools/catalog-template.yml` and `examples/catalog/`  
- **Lineage**: `docs/lineage.md`

---

## Maintenance & Review

See `MAINTENANCE.md` for the quarterly cadence:
1. Review policies  
2. Update metadata catalog  
3. Refine quality checks  
4. Close and open issues

---

## Contributing

1. Fork the repo.  
2. Create a feature branch.  
3. Commit with clear messages.  
4. Push and open a Pull Request.  
5. Tag reviewers.

---

## License

This project is distributed under the MIT License. See `LICENSE` for details.

