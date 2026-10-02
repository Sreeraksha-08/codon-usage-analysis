import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

DB_PATH = "database/codon_usage.db"
FIGURE_PATH = "figures/python/pca_kingdom_clusters.png"

# Connect to database
conn = sqlite3.connect(DB_PATH)

# Get codon frequencies in wide format
query = """
SELECT
    o.organism_id,
    o.kingdom,
    cf.codon,
    cf.frequency
FROM organisms o
JOIN codon_frequencies cf
    ON o.organism_id = cf.organism_id;
"""

df = pd.read_sql_query(query, conn)
conn.close()

print("Data loaded from SQLite!")
print("Rows:", len(df))

# Convert long format to wide format
codon_table = df.pivot(
    index="organism_id",
    columns="codon",
    values="frequency"
)

# Get kingdom information
kingdoms = df.drop_duplicates("organism_id").set_index(
    "organism_id"
)["kingdom"]

# Make sure codon columns are numeric
codon_table = codon_table.apply(
    pd.to_numeric,
    errors="coerce"
)

# Replace missing values with column means
codon_table = codon_table.fillna(
    codon_table.mean()
)

# Standardize codon frequencies
scaler = StandardScaler()
scaled_data = scaler.fit_transform(codon_table)

# PCA
pca = PCA(n_components=2)
principal_components = pca.fit_transform(scaled_data)

print("Explained variance ratio:")
print(pca.explained_variance_ratio_)

# Create PCA DataFrame
pca_df = pd.DataFrame(
    principal_components,
    columns=["PC1", "PC2"]
)

pca_df["kingdom"] = kingdoms.values

# Plot PCA
plt.figure(figsize=(10, 7))

for kingdom in pca_df["kingdom"].unique():
    subset = pca_df[pca_df["kingdom"] == kingdom]

    plt.scatter(
        subset["PC1"],
        subset["PC2"],
        label=kingdom,
        alpha=0.6
    )

plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA of Codon Usage by Kingdom")
plt.legend(
    bbox_to_anchor=(1.05, 1),
    loc="upper left"
)

plt.tight_layout()

plt.savefig(FIGURE_PATH, dpi=300)

print("PCA plot saved to:", FIGURE_PATH)