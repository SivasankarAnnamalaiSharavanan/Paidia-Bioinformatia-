def reverse_complement(dna_string):

  complement_map = {"A": "T", "T": "A", "C": "G", "G": "C"}
  complement_string = ''.join(complement_map[nucleotide] for nucleotide in dna_string[::-1])
  return complement_string

try:
  with open("rosalind_revc.txt", "r") as dna_file:
      dna_string = dna_file.read().strip()

  reverse_complement_string = reverse_complement(dna_string)

  print(reverse_complement_string)

except (FileNotFoundError, IOError) as e:
  print(f"Error reading file: {e}")