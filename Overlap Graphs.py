from Bio import SeqIO
def overlap_graph(fasta_file, k)
    sequences = {}
    for record in SeqIO.parse(fasta_file, "fasta"):
        sequences[record.id] = record.seq

    graph = {}
    for seq_id1, seq1 in sequences.items():
        suffix = seq1[-k:]
        for seq_id2, seq2 in sequences.items():
            if seq_id1 != seq_id2:
                prefix = seq2[:k]
                if suffix == prefix:
                    if seq_id1 not in graph:
                        graph[seq_id1] = []
                    graph[seq_id1].append(seq_id2)
    return graph

def write_adjacency_list(graph, output_file):
    with open(output_file, "w") as f:
        for node, neighbors in graph.items():
            for neighbor in neighbors:
                f.write(f"{node} {neighbor}\n")

if __name__ == "__main__":
    fasta_file = "rosalind_grph.txt"
    k = 3
    graph = overlap_graph(fasta_file, k)
    write_adjacency_list(graph, "output2.txt")