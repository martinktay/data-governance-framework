# Data Lineage for Water Portability

This framework tracks the flow of the Water Portability dataset from raw CSV to final reporting.

      ┌──────────────────────────────┐
      │  Source:                     │
      │  water_portability.csv       │
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
      │  (water_portability table)   │
      └──────────────┬───────────────┘
                     │ Query
                     ▼
      ┌──────────────────────────────┐
      │  Reporting & Analysis via    │
      │  Jupyter notebooks or BI     │
      └──────────────────────────────┘

1. **Extract** the raw CSV (`data/water_portability.csv`).
2. **Transform & Clean** using `src/quality_checks/checks.py` (and/or SQL in `checks.sql`).
3. **Load** cleaned data into your chosen database (e.g. SQLite: `CREATE TABLE water_portability AS SELECT * FROM cleaned_data;`).
4. **Query & Report** using notebooks or BI tools against the `water_portability` table.
