import pandas as pd
# from ace_tools import display_dataframe_to_user

# Load dataset
df = pd.read_csv(r'C:\Users\User\Documents\projects\data-governance-framework\data\water_portability.csv')

# 1) Completeness
completeness = 100 * (1 - df.isnull().sum().sum() / df.size)
print(f"Completeness: {completeness:.2f}%")

# 2) pH validity (expected range 0–14)
invalid_ph = df[(df['ph'] < 0) | (df['ph'] > 14)].shape[0]
print(f"Invalid pH records: {invalid_ph}")

# 3) Missing Potability labels
missing_label = df['Potability'].isnull().sum()
print(f"Missing Potability labels: {missing_label}")

# 4) Potability class distribution
class_counts = df['Potability'].value_counts(dropna=False)
print("Potability class distribution:")
print(class_counts.to_string())
