import pandas as pd

INPUT_FILE = "data/raw/codon_usage.csv"
OUTPUT_FILE = "processed/codon_usage_clean.csv"

# Load dataset
df = pd.read_csv(INPUT_FILE)

print("Dataset loaded successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nColumn names:")
print(df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

print("\nData types:")
print(df.dtypes)

# Save a copy for now
df.to_csv(OUTPUT_FILE, index=False)

print("\nCleaned dataset saved to:")
print(OUTPUT_FILE)
