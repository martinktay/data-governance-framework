# Data Lineage for Water potability

This framework tracks the flow of the Water potability dataset from raw CSV to final reporting.

      ┌──────────────────────────────┐
      │  Source:                     │
      │  water_potability.csv       │
      └──────────────┬───────────────┘
                     │ Extract
                     ▼
      ┌──────────────────────────────┐
      │  Transform & Clean via       │
      │  Python scripts in src/      │
      └──────────────┬───────────────┘
                     │ Load
                     ▼
      ┌──────────────────────────────┐
      │  Database: SQLite or Postgres│
      │  (water_potability table)   │
      └──────────────┬───────────────┘
                     │ Query
                     ▼
      ┌──────────────────────────────┐
      │  Reporting & Analysis via    │
      │  Jupyter notebooks or BI     │
      └──────────────────────────────┘

1. **Extract** the raw CSV (`data/water_potability.csv`).
2. **Transform & Clean** using `src/quality_checks/checks.py` (and/or SQL in `checks.sql`).
3. **Load** cleaned data into your chosen database (e.g. SQLite: `CREATE TABLE water_potability AS SELECT * FROM cleaned_data;`).
4. **Query & Report** using notebooks or BI tools against the `water_potability` table.
