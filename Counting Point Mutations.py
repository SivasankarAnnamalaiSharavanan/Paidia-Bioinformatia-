from Bio.Seq import Seq
from Bio.SeqUtils import nt_search

def calculate_hamming_distance(seq1, seq2):
    assert len(seq1) == len(seq2), "Sequences are not of equal length."

    distance = sum(1 for nucleotide1, nucleotide2 in zip(seq1, seq2) if nucleotide1 != nucleotide2)
    return distance

with open('rosalind_hamm.txt', 'r') as file:
    lines = file.readlines()
    seq1 = Seq(lines[0].strip())
    seq2 = Seq(lines[1].strip())

hamming_distance = calculate_hamming_distance(seq1, seq2)
print(f"The Hamming distance is: {hamming_distance}")