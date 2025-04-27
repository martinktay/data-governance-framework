# scripts/clean_and_sample.py

import pandas as pd

# 1) Load the full dataset
df = pd.read_csv('data/water_quality_dataset_100k.csv')

# 2) Drop columns with >3% missing values
df = df.drop(columns=['Copper', 'Sulfate', 'Fluoride', 'Odor'])

# 3) Impute remaining nulls:
num_cols = df.select_dtypes(include=['float64','int64']).columns
cat_cols = df.select_dtypes(include=['object']).columns

for col in num_cols:
    df[col].fillna(df[col].median(), inplace=True)
for col in cat_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

# 4) Keep only core columns (optional)
keep = [
    'pH','Iron','Nitrate','Chloride','Lead','Zinc',
    'Color','Turbidity','Conductivity','Chlorine',
    'Manganese','Total Dissolved Solids','Source',
    'Water Temperature','Air Temperature',
    'Month','Day','Time of Day','Target'
]
df = df[keep]

# 5) Sample 10% of rows
sample_df = df.sample(frac=0.10, random_state=42)

# 6) Save the cleaned, sampled CSV
out_path = 'data/water_potability_clean_sample.csv'
sample_df.to_csv(out_path, index=False)
print(f"Saved {len(sample_df)} rows × {df.shape[1]} cols to {out_path}")