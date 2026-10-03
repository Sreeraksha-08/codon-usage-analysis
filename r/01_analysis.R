# Load cleaned codon usage dataset

data <- read.csv("processed/codon_usage_clean.csv")

# Basic information
print("Dataset loaded successfully!")

print("Rows:")
print(nrow(data))

print("Columns:")
print(ncol(data))

# First 5 rows
print("First 5 rows:")
print(head(data))

# Dataset structure
print("Data structure:")
str(data)
# -----------------------------
# Day 4: Statistical Analysis
# -----------------------------

# Summary statistics for Ncodons
print("Summary of Ncodons:")
print(summary(data$Ncodons))

# Mean number of codons by kingdom
kingdom_mean <- aggregate(
  Ncodons ~ Kingdom,
  data = data,
  FUN = mean,
  na.rm = TRUE
)

print("Mean Ncodons by kingdom:")
print(kingdom_mean)
# -----------------------------
# Day 4: R Visualizations
# -----------------------------

# Create figures directory if it does not exist
if (!dir.exists("figures/r")) {
  dir.create("figures/r", recursive = TRUE)
}

# Boxplot of Ncodons by Kingdom
png(
  "figures/r/ncodons_by_kingdom.png",
  width = 1200,
  height = 800
)

boxplot(
  Ncodons ~ Kingdom,
  data = data,
  main = "Ncodons Distribution by Kingdom",
  xlab = "Kingdom",
  ylab = "Number of Codons",
  las = 2
)

dev.off()

# Bar plot of mean Ncodons by Kingdom
png(
  "figures/r/mean_ncodons_by_kingdom.png",
  width = 1200,
  height = 800
)

barplot(
  kingdom_mean$Ncodons,
  names.arg = kingdom_mean$Kingdom,
  main = "Mean Ncodons by Kingdom",
  xlab = "Kingdom",
  ylab = "Mean Ncodons",
  las = 2
)

dev.off()

print("R analysis and visualizations completed successfully!")
# -----------------------------
# Codon Frequency Analysis
# -----------------------------

# Calculate mean frequency of each codon
# Calculate mean frequency of each codon
codon_columns <- names(data)[6:ncol(data)]

# Convert codon frequency columns to numeric
data[codon_columns] <- lapply(
  data[codon_columns],
  function(x) as.numeric(as.character(x))
)

codon_means <- colMeans(
  data[codon_columns],
  na.rm = TRUE
)


print("Mean frequency of each codon:")
print(codon_means)

# Find the 10 codons with the highest mean frequency
top_codons <- sort(
  codon_means,
  decreasing = TRUE
)[1:10]

print("Top 10 codons by mean frequency:")
print(top_codons)
# -----------------------------
# Top 10 Codon Visualization
# -----------------------------

png(
  "figures/r/top_10_codons.png",
  width = 1200,
  height = 800
)

barplot(
  top_codons,
  main = "Top 10 Codons by Mean Frequency",
  xlab = "Codon",
  ylab = "Mean Frequency",
  las = 2
)

dev.off()

print("Top 10 codon plot saved successfully!")
# -----------------------------
# Save R Results
# -----------------------------

if (!dir.exists("results/tables")) {
  dir.create("results/tables", recursive = TRUE)
}

r_results <- data.frame(
  Codon = names(top_codons),
  Mean_Frequency = as.numeric(top_codons)
)

write.csv(
  r_results,
  "results/tables/r_top_10_codons.csv",
  row.names = FALSE
)

print("R results saved successfully!")
