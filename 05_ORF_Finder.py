dna_sequence = input("Enter DNA Sequence: ").upper()

valid_nucleotides = "ATGC"
is_valid = True

for nucleotide in dna_sequence:
    if nucleotide not in valid_nucleotides:
        is_valid = False
        print("Invalid nucleotide found:", nucleotide)
        break

if is_valid:
    print("Valid DNA Sequence")
    start_codon = "ATG"
    stop_codons = ["TAA" , "TAG" , "TGA"]

    # Finding the start codon 
    start_index = dna_sequence.find(start_codon)

    # Checking if start codon is present 
    if start_index != -1:
        print("Start codon found")
    
        stop_found = False 

        # Searching for stop codon after the start codon
        for i in range(start_index+3, len(dna_sequence), 3):
            codon = dna_sequence[i:i+3]

            if codon in stop_codons:
                stop_index = i
                stop_found = True 
                print("Stop codon found ")
                break
        if stop_found:
            # Extracting ORF Sequence 
            orf_sequence = dna_sequence[start_index:stop_index+3]
            # Calculating ORF Length
            orf_length = len(orf_sequence)

            report = f"""
DNA Sequence : {dna_sequence}

ORF Sequence : {orf_sequence}

ORF Length : {orf_length} nucleotides

ORF Found Successfully 
            """
            print(report)
        else:
            print("Stop codon not found")
    else:
        print("Start codon not found")
 
else:
    print("Invalid DNA Sequence")
