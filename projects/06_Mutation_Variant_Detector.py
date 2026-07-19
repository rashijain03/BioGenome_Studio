original_dna = input("Enter Original DNA Sequence: ").upper()
mutated_dna = input("Enter Mutated DNA Sequence: ").upper()

# Validating DNA sequences
valid_nucleotides = "ATGC"
is_valid = True

for sequence in [original_dna, mutated_dna]:
    for nucleotide in sequence:
        if nucleotide not in valid_nucleotides:
            is_valid = False
            print("Invalid nucleotide found:", nucleotide)
            break

    if not is_valid:
        break

if is_valid:

    if len(original_dna) == len(mutated_dna):
        print("Both DNA sequences have the same length")

        mutation_count = 0

        # Comparing both DNA sequences
        for i in range(len(original_dna)):

            if original_dna[i] != mutated_dna[i]:
                mutation_count += 1

                print("Mutation found at Position", i + 1)
                print(original_dna[i], "→", mutated_dna[i])

        if mutation_count == 0:
             print("No mutations found")

        else:
            print("Total Mutations :", mutation_count)

    else:
         print(" Both DNA sequences are not the same length")

else:
    print("Invalid DNA Sequence")