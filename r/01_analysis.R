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