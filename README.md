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
## Day 3 – SQL Database and PCA Analysis

### SQLite Database

- Created a SQLite database at `database/codon_usage.db`.
- Created `organisms` and `codon_frequencies` tables.
- Loaded 13,028 organisms into the database.
- Loaded 833,789 codon-frequency records.

### SQL Analysis

- Created SQL analysis queries for organism counts and codon frequencies.
- Saved query results in `results/tables/`.
- Generated five CSV result tables.

### PCA Analysis

- Performed PCA on standardized codon-frequency data.
- Used the first two principal components for visualization.
- PC1 explained approximately 29.82% of the variance.
- PC2 explained approximately 18.61% of the variance.
- Generated `figures/python/pca_kingdom_clusters.png`.