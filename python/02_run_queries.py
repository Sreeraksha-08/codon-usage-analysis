import sqlite3
import pandas as pd
import os

DB_PATH = "database/codon_usage.db"
OUTPUT_DIR = "results/tables"

os.makedirs(OUTPUT_DIR, exist_ok=True)

conn = sqlite3.connect(DB_PATH)

# Query 1
query1 = """
SELECT kingdom, COUNT(*) AS n_organisms
FROM organisms
GROUP BY kingdom
ORDER BY n_organisms DESC;
"""

result1 = pd.read_sql_query(query1, conn)
result1.to_csv(f"{OUTPUT_DIR}/query1_organisms_by_kingdom.csv", index=False)


# Query 2
query2 = """
SELECT o.kingdom, AVG(cf.frequency) AS avg_ggc_freq
FROM organisms o
JOIN codon_frequencies cf
    ON o.organism_id = cf.organism_id
WHERE cf.codon = 'GGC'
GROUP BY o.kingdom
ORDER BY avg_ggc_freq DESC;
"""

result2 = pd.read_sql_query(query2, conn)
result2.to_csv(f"{OUTPUT_DIR}/query2_avg_ggc_by_kingdom.csv", index=False)


# Query 3
query3 = """
SELECT o.kingdom, AVG(cf.frequency) AS avg_uuu_freq
FROM organisms o
JOIN codon_frequencies cf
    ON o.organism_id = cf.organism_id
WHERE cf.codon = 'UUU'
GROUP BY o.kingdom
ORDER BY avg_uuu_freq DESC;
"""

result3 = pd.read_sql_query(query3, conn)
result3.to_csv(f"{OUTPUT_DIR}/query3_avg_uuu_by_kingdom.csv", index=False)


# Query 4
query4 = """
SELECT codon, AVG(frequency) AS avg_frequency
FROM codon_frequencies
GROUP BY codon
ORDER BY avg_frequency DESC
LIMIT 10;
"""

result4 = pd.read_sql_query(query4, conn)
result4.to_csv(f"{OUTPUT_DIR}/query4_top_10_codons.csv", index=False)


# Query 5
query5 = """
SELECT o.kingdom, COUNT(cf.freq_id) AS codon_records
FROM organisms o
JOIN codon_frequencies cf
    ON o.organism_id = cf.organism_id
GROUP BY o.kingdom
ORDER BY codon_records DESC;
"""

result5 = pd.read_sql_query(query5, conn)
result5.to_csv(f"{OUTPUT_DIR}/query5_codon_records_by_kingdom.csv", index=False)

conn.close()

print("All queries completed successfully!")
print("Results saved in:", OUTPUT_DIR)