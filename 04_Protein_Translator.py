dna_sequence = input("Enter DNA Sequence: ").upper()

# Checking DNA sequence validity 
valid_nucleotides = "ATGC"
is_valid = True

for nucleotide in dna_sequence:
    if nucleotide not in valid_nucleotides:
        is_valid = False
        print("Invalid nucleotide found:", nucleotide)
        break

if is_valid:
    print("Valid DNA Sequence")

    # Converting DNA sequence into RNA sequence
    rna_sequence = dna_sequence.replace("T" , "U")

    # Codon dictionary for RNA to amino acid conversion
    codon_table = {
    "UUU": "F", "UUC": "F",
    "UUA": "L", "UUG": "L",

    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",

    "UAU": "Y", "UAC": "Y",
    "UAA": "Stop", "UAG": "Stop",

    "UGU": "C", "UGC": "C",
    "UGA": "Stop", "UGG": "W",

    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",

    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",

    "CAU": "H", "CAC": "H",
    "CAA": "Q", "CAG": "Q",

    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",

    "AUU": "I", "AUC": "I", "AUA": "I",
    "AUG": "M",

    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",

    "AAU": "N", "AAC": "N",
    "AAA": "K", "AAG": "K",

    "AGU": "S", "AGC": "S",
    "AGA": "R", "AGG": "R",

    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",

    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",

    "GAU": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",

    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}
    # Translating RNA codons into protein sequence
    protein_sequence = ""
    for i in range(0, len(rna_sequence)-2, 3):
        codon = rna_sequence[i:i+3]
        

        if codon in codon_table:
            amino_acid = codon_table[codon]

            # Stop translation when stop codon is found
            if amino_acid == "Stop":
                break
            protein_sequence += amino_acid
        
        else:
            protein_sequence += "?"

    # Creating final report
    report = f"""
DNA Sequence : {dna_sequence}
RNA Sequence : {rna_sequence}
Protein Sequence : {protein_sequence}

Translation Completed
 """
    print(report)


else:
    print("Invalid DNA Sequence")
    