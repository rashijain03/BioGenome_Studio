dna_sequence = input("Enter DNA Sequence: ").upper()
k = int(input("Enter K-mer Size: "))

def validate_dna(sequence):
    if len(sequence) == 0:
        print("DNA Sequence cannot be empty.")
        return False

    valid_nucleotides = "ATGC"

    for nucleotide in sequence:
        if nucleotide not in valid_nucleotides:
            print("Invalid nucleotide found:", nucleotide)
            return False

    return True

if validate_dna(dna_sequence):
    print("Valid DNA Sequence")

    if k <= 0 or k > len(dna_sequence):
        print("Invalid K-mer Size")
    else:
        print("Valid K-mer Size")

        kmer_count = {}

        for i in range(len(dna_sequence) - k + 1):
            kmer = dna_sequence[i:i+k]

            if kmer in kmer_count:
                kmer_count[kmer] += 1
            else:
                kmer_count[kmer] = 1
        frequency_report = ""

        for kmer in kmer_count:
            frequency_report += f"{kmer} : {kmer_count[kmer]}\n"

        report = f"""
============= K-mer Analyzer Report ==============

DNA Sequence : {dna_sequence}
K-mer Size   : {k}

K-mer Frequency:
{frequency_report}

Unique K-mers Found : {len(kmer_count)}
Total K-mers Generated : {len(dna_sequence) - k + 1}
"""

        print(report)
     

else:
    print("Invalid DNA Sequence")

