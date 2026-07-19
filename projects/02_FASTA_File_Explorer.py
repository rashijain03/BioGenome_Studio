# Opening the FASTA file
file = open("data/sample.fasta", "r")

# Reading all lines
lines = file.readlines()

# Closing the file
file.close()

# Extracting header and DNA sequence
header = lines[0].strip().replace(">", "")
dna_sequence = lines[1].strip()

# Finding the length of DNA sequence
sequence_length = len(dna_sequence)

report = f"""
Sequence ID: {header}

DNA Sequence:
{dna_sequence}

Sequence Length: {sequence_length} bp

FASTA File Read Successfully
"""

print(report)