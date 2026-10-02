# Codon Usage Analysis

## Day 2 – Data Cleaning and Exploratory Data Analysis

### Data Cleaning

- Loaded the raw codon usage dataset using Python and pandas.
- Inspected rows, columns, missing values, and data types.
- Converted codon frequency columns to numeric values.
- Handled non-numeric values using `pd.to_numeric()`.

### Exploratory Data Analysis

- Counted organisms by biological kingdom.
- Identified 64 codon frequency columns.
- Compared average GC-ending and AT-ending codon frequencies by kingdom.
- Generated a GC-ending vs AT-ending frequency graph.
- Generated a codon correlation heatmap.

### Generated Figures

- `figures/python/gc_ending_by_kingdom.png`
- `figures/python/codon_correlation_heatmap.png`