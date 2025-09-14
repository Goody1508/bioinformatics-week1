# analyze_hbb.py
from Bio import Entrez, SeqIO
from Bio.SeqUtils import gc_fraction
import matplotlib.pyplot as plt
import sys

# ---- Config ----
Entrez.email = "goodnessowunmi@gmail.com"  
ACCESSION = "NM_000518.5"  # HBB (human beta-globin) mRNA

def fetch_fasta(accession: str):
    with Entrez.efetch(db="nucleotide", id=accession, rettype="fasta", retmode="text") as handle:
        record = SeqIO.read(handle, "fasta")
    return record

def main():
    try:
        record = fetch_fasta(ACCESSION)
    except Exception as e:
        print("Error fetching sequence:", e, file=sys.stderr)
        sys.exit(1)

    dna = record.seq

    # Basic summary
    print("Sequence ID:", record.id)
    print("Description:", record.description)
    print("Length (bp):", len(dna))

    # Nucleotide counts & GC
    bases = "ATCG"
    counts = {b: dna.count(b) for b in bases}
    gc = gc_fraction(dna) * 100
    print("Nucleotide counts:", counts)
    print(f"GC Content: {gc:.2f}%")

    # Save FASTA locally for your repo
    SeqIO.write(record, "hbb_downloaded.fasta", "fasta")

    # Bar chart
    plt.figure()
    plt.bar(list(counts.keys()), list(counts.values()))
    plt.title("Nucleotide Composition: HBB (NM_000518.5)")
    plt.xlabel("Base")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("nucleotide_counts.png", dpi=200)
    print("Saved plot: nucleotide_counts.png")
    print("Saved FASTA: hbb_downloaded.fasta")

if __name__ == "__main__":
    main()
