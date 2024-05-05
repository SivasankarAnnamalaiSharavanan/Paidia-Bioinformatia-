from Bio.Seq import Seq

def transcribe_dna_to_rna(input_file, output_file):
    with open("rosalind_rna.txt", 'r') as f:
        dna_sequence = f.readline().strip()

    dna_seq = Seq(dna_sequence)


    rna_seq = dna_seq.transcribe()

    with open(output_file, 'w') as f:
        f.write(str(rna_seq))

if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"
    transcribe_dna_to_rna(input_file, output_file)