import numpy as np
import networkx as nx


def write_adjacency_matrix_to_edge_list(A, file_name):
    graph = nx.from_numpy_array(A)
    with open(file_name, "w") as f:
        for i, j, w in graph.edges(data = "weight", default = 1):
            f.write(f"{i} {j} {w:.1f}\n")

def load_embedding_from_file(file_name):
    return np.loadtxt(file_name, skiprows = 1)

