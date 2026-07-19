import subprocess
import sys

print("=" * 45)
print("        BioGenome Studio")
print("=" * 45)

while True:

    print("\n1. Genome Quality Analyser")
    print("2. FASTA File Explorer")
    print("3. DNA RNA Converter")
    print("4. Protein Translator")
    print("5. ORF Finder")
    print("6. Mutation Variant Detector")
    print("7. DNA Motif Finder")
    print("8. K-mer Analyzer")
    print("9. Genome Visualization Dashboard")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == "0":
        print("\nExiting BioGenome Pipeline...")
        break

    elif choice == "1":
        print("\nLaunching Genome Quality Analyzer...")
        subprocess.run([sys.executable, "projects/01_Genome_Quality_Analyser.py"])

    elif choice == "2":
        print("\nLaunching FASTA File Explorer...")
        subprocess.run([sys.executable, "projects/02_FASTA_File_Explorer.py"])

    elif choice == "3":
        print("\nLaunching DNA RNA Converter...")
        subprocess.run([sys.executable, "projects/03_DNA_RNA_Converter.py"])

    elif choice == "4":
        print("\nLaunching Protein Translator...")
        subprocess.run([sys.executable, "projects/04_Protein_Translator.py"])

    elif choice == "5":
        print("\nLaunching ORF Finder...")
        subprocess.run([sys.executable, "projects/05_ORF_Finder.py"])

    elif choice == "6":
        print("\nLaunching Mutation Variant Detector...")
        subprocess.run([sys.executable, "projects/06_Mutation_Variant_Detector.py"])

    elif choice == "7":
        print("\nLaunching DNA Motif Finder...")
        subprocess.run([sys.executable, "projects/07_DNA_Motif_Finder.py"])

    elif choice == "8":
        print("\nLaunching K-mer Analyzer...")
        subprocess.run([sys.executable, "projects/08_Kmer_Analyzer.py"])

    elif choice == "9":
        print("\nLaunching Genome Visualization Dashboard...")
        subprocess.run([sys.executable, "projects/09_Genome_Visualization_Dashboard.py"])

    else:
        print("\nInvalid choice! Please enter a number between 0-9.")