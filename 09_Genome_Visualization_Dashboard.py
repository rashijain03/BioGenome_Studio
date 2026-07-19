import matplotlib.pyplot as plt

dna_sequence = input("Enter DNA Sequence: ").upper()


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

    count_A = dna_sequence.count("A")
    count_T = dna_sequence.count("T")
    count_G = dna_sequence.count("G")
    count_C = dna_sequence.count("C")

    sequence_length = len(dna_sequence)

    gc_content = ((count_G + count_C) / sequence_length) * 100
    at_content = ((count_A + count_T) / sequence_length) * 100

    report = f"""
============= Genome Visualization Dashboard ==============

DNA Sequence : {dna_sequence}

Sequence Length : {sequence_length}

A : {count_A}
T : {count_T}
G : {count_G}
C : {count_C}

GC Content : {gc_content:.2f}%
AT Content : {at_content:.2f}%
"""

    print(report)

    print("Displaying Bar Chart...")

    nucleotides = ["A", "T", "G", "C"]
    counts = [count_A, count_T, count_G, count_C]

    plt.bar(nucleotides, counts)

    plt.title("Nucleotide Count")
    plt.xlabel("Nucleotides")
    plt.ylabel("Count")

    plt.show()

    print("Displaying Pie Chart...")

    plt.pie( counts , 
             labels=nucleotides ,
             autopct="%1.1f%%")
    plt.title("Nucleotide Percentage")

    plt.show()




else:
    print("Invalid DNA Sequence")