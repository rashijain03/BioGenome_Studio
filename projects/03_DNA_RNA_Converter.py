dna_sequence = input("Enter DNA Sequence: ").upper()
valid_nucleotides = "ATGC"
is_valid = True
for nucleotide in dna_sequence:
    if nucleotide not in valid_nucleotides:
        is_valid = False
        print("Invalid nucleotide found:" , nucleotide)
        break
if is_valid:
    rna_sequence = dna_sequence.replace("T","U")

    report = f"""
    DNA Sequence : {dna_sequence}

    RNA Sequence : {rna_sequence}

    Conversion Successful
    """
    print(report)

else:
    print("Please enter a DNA sequence containing only A, T, G, and C.")


