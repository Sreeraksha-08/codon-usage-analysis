import pandas as pd
import sqlite3

INPUT_FILE = "processed/codon_usage_clean.csv"
DB_PATH = "database/codon_usage.db"

# Load cleaned dataset
df = pd.read_csv(INPUT_FILE)

# Connect to SQLite database
conn = sqlite3.connect(DB_PATH)

# Create tables using schema.sql
with open("sql/schema.sql", "r") as f:
    schema = f.read()

conn.executescript(schema)

# Insert organism information
organisms = df[
    ["SpeciesID", "SpeciesName", "Kingdom", "DNAtype", "Ncodons"]
].copy()

organisms.columns = [
    "species_id",
    "species_name",
    "kingdom",
    "dna_type",
    "n_codons"
]

organisms.to_sql(
    "organisms",
    conn,
    if_exists="append",
    index=False
)

# Get generated organism IDs
organism_ids = pd.read_sql_query(
    "SELECT organism_id FROM organisms",
    conn
)["organism_id"]

# Codon columns
codon_columns = df.columns[5:]

# Convert codon data to long format
codon_data = []

for i, organism_id in enumerate(organism_ids):
    for codon in codon_columns:
        frequency = pd.to_numeric(
            df.iloc[i][codon],
            errors="coerce"
        )

        if pd.notna(frequency):
            codon_data.append(
                (organism_id, codon, frequency)
            )

# Create DataFrame
codon_df = pd.DataFrame(
    codon_data,
    columns=["organism_id", "codon", "frequency"]
)

# Insert codon frequencies
codon_df.to_sql(
    "codon_frequencies",
    conn,
    if_exists="append",
    index=False
)

conn.close()

print("Database created successfully!")
print("Organisms loaded:", len(organisms))
print("Codon frequency records loaded:", len(codon_df))
print("Database:", DB_PATH)