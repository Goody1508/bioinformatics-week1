🧬 Week 1 – Bioinformatics Starter Project

Project: Nucleotide Composition & GC Content Analysis of the Human Hemoglobin Beta (HBB) Gene

📌 Background

This project is part of a personal bioinformatics learning roadmap. The goal for Week 1 is to get comfortable working with FASTA files and sequence analysis using Python + Biopython.

The HBB gene (Hemoglobin subunit beta) encodes one of the subunits of hemoglobin, the protein that carries oxygen in red blood cells. Mutations in this gene are associated with diseases like sickle cell anemia.

⚙️ Methods

Data retrieval

The nucleotide sequence was fetched from NCBI Nucleotide using its accession number NM_000518.5.

BioPython’s Entrez.efetch was used to download and parse the sequence.

Analysis performed

Extracted sequence metadata (ID, description, length).

Counted nucleotide frequencies (A, T, C, G).

Calculated GC content (%) using Bio.SeqUtils.gc_fraction.

Translated DNA sequence to amino acids.

Saved results in a FASTA file for reproducibility.

Visualization

A simple bar chart of nucleotide composition was generated using matplotlib.

📊 Results

Example terminal output:

Sequence ID: NM_000518.5
Description: NM_000518.5 Homo sapiens hemoglobin subunit beta (HBB), mRNA
Length (bp): 628
Nucleotide counts: {'A': 139, 'T': 167, 'C': 157, 'G': 165}
GC Content: 51.27%
Saved plot: nucleotide_counts.png
Saved FASTA: hbb_downloaded.fasta

Generated plot: nucleotide_counts.png

📂 Files in This Repository

analyze_hbb.py → main analysis script

hbb_downloaded.fasta → downloaded FASTA sequence (HBB)

nucleotide_counts.png → bar chart of nucleotide composition

README.md → project documentation

🚀 How to Run

Clone this repo and run the script:

git clone https://github.com/<your-username>/bioinformatics-week1.git
cd bioinformatics-week1
python3 analyze_hbb.py


Requirements:

Python 3.8+

Biopython, matplotlib

Install dependencies:

pip install biopython matplotlib