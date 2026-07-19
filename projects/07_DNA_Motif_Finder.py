dna_sequence = input("Enter DNA Sequence: ").upper()
motif = input("Enter DNA Motif: ").upper()

def validate_dna(sequence):
    valid_nucleotides = "ATGC"
    for nucleotide in sequence:
        if nucleotide not in valid_nucleotides:
            print("Invalid nucleotides found: " , nucleotide)
            return False
    return True
if validate_dna(dna_sequence) and validate_dna(motif):
    print("Valid DNA Sequence")

    motif_count = 0
    motif_positions = []

    for i in range(len(dna_sequence) - len(motif) + 1):
        current_part = dna_sequence[i:i+len(motif)]
        if current_part == motif:
            motif_count += 1
            motif_positions.append(i+1)

    if motif_count == 0:
        print("Motif not found")
            
              
    else:
        position_report = ""
        for position in motif_positions:
            position_report += f"Position {position}\n"

        report = f"""
============= DNA Motif Finder Report ===============

DNA Sequence : {dna_sequence}
Motif        : {motif}

Motif Positions:
{position_report}

Total Motifs Found : {motif_count}
"""
        print(report)

else:
    print("Invalid DNA Sequence")
        