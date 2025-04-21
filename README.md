# Data Governance Framework

## Running the SQL checks

1. Load `data/water_portability.csv` into your database (e.g. SQLite, Postgres).
2. Run:
   ```bash
   sqlite3 water.db < src/quality_checks/checks.sql
   ```
