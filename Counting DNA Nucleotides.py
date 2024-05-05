def count_nucleotides(dna_string):
  valid_nucleotides = {'A', 'C', 'G', 'T', 'U'}
  nucleotide_counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0, 'U' : 0}

  for nucleotide in dna_string:
      if nucleotide.isalpha() and nucleotide.isupper():
          if nucleotide in valid_nucleotides:
              nucleotide_counts[nucleotide] += 1
          else:
              print(f"Warning: Invalid nucleotide: {nucleotide}")
      else:
          print(f"Warning: Non-alphabetic character: {nucleotide}")

  return nucleotide_counts

with open("rosalind_dna.txt", "r") as dna_file:
  dna_string = dna_file.read().strip()

nucleotide_counts = count_nucleotides(dna_string)

print(nucleotide_counts)