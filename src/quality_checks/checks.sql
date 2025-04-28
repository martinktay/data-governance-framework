-- checks.sql
-- Run these queries against your database or SQLite dump of water_potability_clean_sample.csv

-- 1) Null count by important columns
SELECT
  SUM(CASE WHEN pH IS NULL THEN 1 ELSE 0 END)             AS missing_pH,
  SUM(CASE WHEN Iron IS NULL THEN 1 ELSE 0 END)           AS missing_Iron,
  SUM(CASE WHEN Nitrate IS NULL THEN 1 ELSE 0 END)        AS missing_Nitrate,
  SUM(CASE WHEN Chloride IS NULL THEN 1 ELSE 0 END)       AS missing_Chloride,
  SUM(CASE WHEN Lead IS NULL THEN 1 ELSE 0 END)           AS missing_Lead,
  SUM(CASE WHEN Zinc IS NULL THEN 1 ELSE 0 END)           AS missing_Zinc,
  SUM(CASE WHEN Turbidity IS NULL THEN 1 ELSE 0 END)      AS missing_Turbidity,
  SUM(CASE WHEN Target IS NULL THEN 1 ELSE 0 END)         AS missing_Target
FROM water_potability;

-- 2) Range validity checks
--   a) pH should be between 0 and 14
SELECT
  COUNT(*) AS invalid_pH_count
FROM water_potability
WHERE pH < 0 OR pH > 14;

--   b) Nitrate should be non-negative
SELECT
  COUNT(*) AS invalid_Nitrate_count
FROM water_potability
WHERE Nitrate < 0;

--   c) Turbidity should be non-negative
SELECT
  COUNT(*) AS invalid_Turbidity_count
FROM water_potability
WHERE Turbidity < 0;

-- 3) Potability class distribution
SELECT
  Target,
  COUNT(*) AS count
FROM water_potability
GROUP BY Target
ORDER BY Target;

