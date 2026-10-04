import pandas as pd

df = pd.read_csv("processed/codon_usage_clean.csv")

bacteria = df[df["Kingdom"] == "bct"]

bacteria["UUU"] = pd.to_numeric(bacteria["UUU"], errors="coerce")
bacteria["UUC"] = pd.to_numeric(bacteria["UUC"], errors="coerce")

print(bacteria[["UUU", "UUC"]])

codon_means = bacteria[["UUU", "UUC"]].mean()

print("\nMean frequency:")
print(codon_means)

codon_means.to_csv("results/tables/bacteria_phenylalanine_means.csv")


# Convert UUU and UUC to numeric for the entire dataset
df[["UUU", "UUC"]] = df[["UUU", "UUC"]].apply(
    pd.to_numeric,
    errors="coerce"
)

# Compare UUU and UUC across all organism groups
group_means = df.groupby("Kingdom")[["UUU", "UUC"]].mean()

print("\nMean UUU and UUC frequency by group:")
print(group_means)
group_means.to_csv(
    "results/tables/phenylalanine_by_group.csv"
)