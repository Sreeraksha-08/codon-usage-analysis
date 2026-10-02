CREATE TABLE IF NOT EXISTS organisms (
    organism_id INTEGER PRIMARY KEY AUTOINCREMENT,
    species_id INTEGER,
    species_name TEXT NOT NULL,
    kingdom TEXT NOT NULL,
    dna_type INTEGER,
    n_codons INTEGER
);

CREATE TABLE IF NOT EXISTS codon_frequencies (
    freq_id INTEGER PRIMARY KEY AUTOINCREMENT,
    organism_id INTEGER NOT NULL,
    codon TEXT NOT NULL,
    frequency REAL NOT NULL,
    FOREIGN KEY (organism_id) REFERENCES organisms(organism_id)
);

CREATE INDEX IF NOT EXISTS idx_kingdom
ON organisms(kingdom);

CREATE INDEX IF NOT EXISTS idx_organism_codon
ON codon_frequencies(organism_id, codon);