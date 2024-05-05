from Bio import SeqIO

def calculate_gc_content(seq_record):
    gc_count = sum([1 for base in seq_record.seq if base in ['G', 'C']])
    total_bases = len(seq_record.seq)
    gc_content = (gc_count / total_bases) * 100
    return gc_content

def find_sequence_with_highest_gc_content(input_file):
    max_gc_content = 0
    max_gc_id = ""

    for seq_record in SeqIO.parse(input_file, "fasta"):
        gc_content = calculate_gc_content(seq_record)
        if gc_content > max_gc_content:
            max_gc_content = gc_content
            max_gc_id = seq_record.id

    return max_gc_id, max_gc_content

if __name__ == "__main__":
    input_file = "rosalind_gc.txt"
    output_file = "output.txt"
    max_gc_id, max_gc_content = find_sequence_with_highest_gc_content(input_file)
    with open(output_file, 'w') as f:
        f.write(f"{max_gc_id}\n")
        f.write(f"{max_gc_content:.6f}")