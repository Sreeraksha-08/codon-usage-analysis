import pandas as pd
import matplotlib.pyplot as plt

# File paths
INPUT_FILE = "processed/codon_usage_clean.csv"
FIGURE_DIR = "figures/python/"

# Load cleaned dataset
df = pd.read_csv(INPUT_FILE)
# Convert codon frequency columns to numeric
codon_columns = df.columns[5:]

for col in codon_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

print("Cleaned dataset loaded successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))

# Kingdom counts
print("\nOrganisms per kingdom:")
print(df["Kingdom"].value_counts())

# Codon columns
meta_cols = ["Kingdom", "DNAtype", "SpeciesID", "Ncodons", "SpeciesName"]
codon_cols = [col for col in df.columns if col not in meta_cols]

print("\nNumber of codon columns:", len(codon_cols))

# Calculate average frequency of codons ending in G/C
gc_codons = [col for col in codon_cols if col.endswith(("G", "C"))]
at_codons = [col for col in codon_cols if col.endswith(("A", "U"))]

df["GC_ending_mean"] = df[gc_codons].mean(axis=1, numeric_only=True)
df["AT_ending_mean"] = df[at_codons].mean(axis=1, numeric_only=True)

# Average by kingdom
gc_summary = df.groupby("Kingdom")[["GC_ending_mean", "AT_ending_mean"]].mean()

print("\nAverage codon frequency by kingdom:")
print(gc_summary)

# Create figure
gc_summary.plot(kind="bar", figsize=(9, 5))

plt.title("Average Codon Frequency: GC-ending vs AT/U-ending")
plt.ylabel("Mean codon frequency")
plt.xlabel("Kingdom")
plt.tight_layout()

plt.savefig(FIGURE_DIR + "gc_ending_by_kingdom.png", dpi=150)

print("\nFigure saved successfully!")
print(FIGURE_DIR + "gc_ending_by_kingdom.png")
# Correlation between codon usage frequencies
correlation = df[codon_columns].corr()

plt.figure(figsize=(12, 10))

plt.imshow(correlation, aspect="auto")
plt.colorbar(label="Correlation")

plt.title("Correlation Between Codon Usage Frequencies")
plt.xlabel("Codons")
plt.ylabel("Codons")

plt.tight_layout()

plt.savefig(
    FIGURE_DIR + "codon_correlation_heatmap.png",
    dpi=150
)

plt.close()

print("Correlation heatmap saved successfully!")
print(FIGURE_DIR + "codon_correlation_heatmap.png")