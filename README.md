# BioGenome_Studio

A collection of Python-based bioinformatics projects developed while learning Python for genomic data science. This repository contains beginner-friendly tools for DNA sequence analysis, FASTA file handling, genome analysis, and other bioinformatics applications.

## Completed Projects

# 01. Genome Quality Analyzer

Features:

* Validates DNA sequences.
* Counts A, T, G, and C nucleotides.
* Calculates GC content.
* Calculates AT content.
* Displays a formatted analysis report.

# 02. FASTA File Explorer

Features:

* Reads a FASTA file.
* Extracts the sequence ID.
* Reads the DNA sequence.
* Calculates the sequence length.
* Displays the sequence information in a formatted report.

# 03. DNA RNA Converter

Features:

* Accepts a DNA sequence from the user.
* Converts lowercase input to uppercase automatically.
* Validates the DNA sequence.
* Converts DNA into RNA by replacing **T** with **U**.
* Displays the DNA sequence and RNA sequence in a formatted report.
* Shows an error message for invalid DNA sequences.

# 04. Protein Translator

Features:

* Accepts a DNA sequence from the user.
* Converts lowercase input to uppercase automatically.
* Validates the DNA sequence.
* Converts DNA into RNA by replacing **T** with **U**.
* Splits RNA sequence into codons (groups of three nucleotides).
* Translates RNA codons into amino acids using a codon dictionary.
* Handles stop codons during translation.
* Displays DNA, RNA, and protein sequences in a formatted report.

# 05. ORF Finder

Features:

* Accepts a DNA sequence from the user.
* Converts lowercase input to uppercase automatically.
* Validates the DNA sequence.
* Finds the start codon (**ATG**).
* Searches for stop codons (**TAA**, **TAG**, **TGA**).
* Extracts the Open Reading Frame (ORF).
* Calculates the ORF length.
* Displays the DNA sequence, ORF sequence, and ORF length in a formatted report.
* Shows appropriate messages if the start codon or stop codon is not found.

# 06. Mutation Variant Detector

Features:

* Accepts the original DNA sequence and mutated DNA sequence from the user.
* Converts lowercase input to uppercase automatically.
* Validates both DNA sequences.
* Checks whether both DNA sequences have the same length.
* Compares the DNA sequences nucleotide by nucleotide.
* Detects mutation positions.
* Displays the original and mutated nucleotides for each mutation.
* Counts the total number of mutations.
* Displays appropriate messages for invalid DNA sequences and different sequence lengths.

# 07. DNA Motif Finder

Features:

* Accepts a DNA sequence and motif from the user.
* Converts lowercase input to uppercase automatically.
* Validates both DNA sequence and motif.
* Searches for the given motif inside the DNA sequence.
* Identifies all positions where the motif occurs.
* Stores motif positions for analysis.
* Counts the total number of motif occurrences.
* Displays DNA sequence, motif, motif positions, and total occurrences in a formatted report.
* Shows an appropriate message if the motif is not found.

# 08. K-mer Analyzer

Features:

* Accepts a DNA sequence from the user.
* Accepts the K-mer size from the user.
* Converts lowercase input to uppercase automatically.
* Validates the DNA sequence.
* Checks for empty DNA sequence.
* Validates the K-mer size.
* Generates all possible K-mers from the DNA sequence.
* Counts the frequency of each unique K-mer using a dictionary.
* Displays the frequency of each K-mer in a formatted report.
* Displays the total number of unique K-mers found.
* Displays the total number of K-mers generated.
* Shows appropriate messages for invalid DNA sequences and invalid K-mer sizes.

# 09. Genome Visualization Dashboard

Features:

* Accepts a DNA sequence from the user.
* Converts lowercase input to uppercase automatically.
* Validates the DNA sequence.
* Checks for an empty DNA sequence.
* Counts the occurrences of A, T, G, and C nucleotides.
* Calculates the sequence length.
* Calculates GC content.
* Calculates AT content.
* Displays the DNA analysis in a formatted report.
* Generates a bar chart showing nucleotide counts.
* Generates a pie chart showing nucleotide percentage distribution.
* Shows appropriate messages for invalid DNA sequences.


# Folder Structure


BioGenome_Studio/
│
├── 01_Genome_Quality_Analyzer.py
├── 02_FASTA_File_Explorer.py
├── 03_DNA_RNA_Converter.py
├── 04_Protein_Translator.py
├── 05_ORF_Finder.py
├── 06_Mutation_Variant_Detector.py
├── 07_DNA_Motif_Finder.py
├── 08_Kmer_Analyzer.py
├── 09_Genome_Visualization_Dashboard.py
├── README.md
├── data/



