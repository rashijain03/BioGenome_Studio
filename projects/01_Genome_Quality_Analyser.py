dna_sequence=input("Enter a Dna sequence:").upper()
valid_nucleotides="ATGC"
is_valid=True
for nucleotide in dna_sequence:
    if nucleotide not in valid_nucleotides:
        is_valid=False
        print("Invalid nucleotide found:",nucleotide)
if is_valid:
    print("valid Dna sequence")
    # Finding length of DNA sequence 
    sequence_length=len(dna_sequence)
    # Counting nucleotides
    count_a=dna_sequence.count("A")
    count_t=dna_sequence.count("T")
    count_g=dna_sequence.count("G")
    count_c=dna_sequence.count("C")  
    # Calculating GC content 
    gc_content = ((count_g + count_c)/sequence_length)*100
    # Calculating AT content
    at_content = ((count_a + count_t)/sequence_length)*100
    # Creating final report
    report=f"""
    Genome Quality Report

    Sequence Length : {sequence_length} bp

    Nucleotide Count:
    A = {count_a}
    T = {count_t}
    G = {count_g}
    C = {count_c}

    GC Content: {round(gc_content,2)}%
    AT Content: {round(at_content,2)}%

    Analysis Completed 
    """
    print(report)
    
else:
    print("Invalid Dna sequence")

