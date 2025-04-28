import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report

# 1) Load clean sample
df = pd.read_csv('data/water_portability_clean_sample.csv')

# 2) feature/target split
df = df.dropna()
X = df.drop('Target', axis=1).select_dtypes(include=['int64','float64'])
y = df['Target']

# 3) Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# 4) Define the models
models = {
    'RandomForest': RandomForestClassifier(n_estimators=50, random_state=42),
    'XGBoost':      XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42),
    'LightGBM':     LGBMClassifier(random_state=42),
    'MLP':          MLPClassifier(hidden_layer_sizes=(100,50), max_iter=200, random_state=42),
}

# 5) Train & evaluate each
for name, model in models.items():
    print(f"\n=== {name} ===")
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    print(classification_report(y_test, preds))