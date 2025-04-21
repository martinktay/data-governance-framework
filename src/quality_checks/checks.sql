-- checks.sql
-- Run these queries against your database or SQLite dump of water_portability.csv

-- 1) Null count by column
SELECT
  SUM(CASE WHEN ph IS NULL THEN 1 ELSE 0 END) AS missing_ph,
  SUM(CASE WHEN Turbidity IS NULL THEN 1 ELSE 0 END) AS missing_turbidity
FROM water_portability;

-- 2) Range validity for pH
SELECT COUNT(*) AS invalid_ph_count
FROM water_portability
WHERE ph < 0 OR ph > 14;
