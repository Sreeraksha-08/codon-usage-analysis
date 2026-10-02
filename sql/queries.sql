-- Query 1: Number of organisms in each kingdom
SELECT kingdom, COUNT(*) AS n_organisms
FROM organisms
GROUP BY kingdom
ORDER BY n_organisms DESC;


-- Query 2: Average GGC codon frequency by kingdom
SELECT o.kingdom, AVG(cf.frequency) AS avg_ggc_freq
FROM organisms o
JOIN codon_frequencies cf
    ON o.organism_id = cf.organism_id
WHERE cf.codon = 'GGC'
GROUP BY o.kingdom
ORDER BY avg_ggc_freq DESC;


-- Query 3: Average UUU codon frequency by kingdom
SELECT o.kingdom, AVG(cf.frequency) AS avg_uuu_freq
FROM organisms o
JOIN codon_frequencies cf
    ON o.organism_id = cf.organism_id
WHERE cf.codon = 'UUU'
GROUP BY o.kingdom
ORDER BY avg_uuu_freq DESC;


-- Query 4: Top 10 codons by average frequency
SELECT codon, AVG(frequency) AS avg_frequency
FROM codon_frequencies
GROUP BY codon
ORDER BY avg_frequency DESC
LIMIT 10;


-- Query 5: Number of codon records for each kingdom
SELECT o.kingdom, COUNT(cf.freq_id) AS codon_records
FROM organisms o
JOIN codon_frequencies cf
    ON o.organism_id = cf.organism_id
GROUP BY o.kingdom
ORDER BY codon_records DESC;