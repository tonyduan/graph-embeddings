import itertools
import numpy as np
import networkx as nx
from matplotlib import pyplot as plt
from graph_embeddings.methods import *


def gen_graphs(n_graphs, n_nodes, p_intra=0.7, p_inter=0.01):
    """
    Generate community graphs.
    """
    A = np.zeros((n_graphs, n_nodes, n_nodes))
    for idx in range(n_graphs):
        comms = [nx.gnp_random_graph(n_nodes // 2, p_intra),
                 nx.gnp_random_graph((n_nodes + 1) // 2, p_intra)]
        graph = nx.disjoint_union_all(comms)
        graph = nx.to_numpy_array(graph)
        block1 = np.arange(n_nodes // 2)
        block2 = np.arange(n_nodes // 2, n_nodes)
        remaining = list(itertools.product(block1, block2))
        np.random.shuffle(remaining)
        for (i, j) in remaining[:int(p_inter * n_nodes + 1)]:
            graph[i,j], graph[j,i] = 1, 1
        P = np.eye(n_nodes)
        np.random.shuffle(P)
        graph = P.T @ graph @ P
        A[idx, :, :] = graph
    return A


if __name__ == "__main__":

    A = gen_graphs(4, 16)
    E_N2V = [compute_node2vec_embedding(a, 2, 10) for a in A]
    E_LU = [compute_unnormalized_laplacian_eigenmaps(a) for a in A]
    E_LN = [compute_normalized_laplacian_eigenmaps(a) for a in A]
    E_LLE = [compute_locally_linear_embedding(a) for a in A]

    plt.figure(figsize = (8, 6))
    for i in range(4):
        plt.subplot(4, 5, 5 * i + 1)
        nx.draw(nx.from_numpy_array(A[i]), node_size = 20, node_color = "0")
        plt.subplot(4, 5, 5 * i + 2)
        plt.imshow(E_LU[i], vmin = -1, vmax = 1)
        plt.axis("off")
        plt.subplot(4, 5, 5 * i + 3)
        plt.imshow(E_LN[i], vmin = -1, vmax = 1)
        plt.axis("off")
        plt.subplot(4, 5, 5 * i + 4)
        plt.imshow(E_LLE[i], vmin = np.min(E_LLE), vmax = np.max(E_LLE))
        plt.axis("off")
        plt.subplot(4, 5, 5 * i + 5)
        plt.imshow(E_N2V[i], vmin = np.min(E_N2V), vmax = np.max(E_N2V))
        plt.axis("off")

    plt.subplot(4, 5, 1)
    plt.title("Graph")
    plt.subplot(4, 5, 2)
    plt.title("LE (unnormalized)")
    plt.subplot(4, 5, 3)
    plt.title("LE (normalized)")
    plt.subplot(4, 5, 4)
    plt.title("LLE")
    plt.subplot(4, 5, 5)
    plt.title("Node2Vec")
    plt.tight_layout()
    plt.show()

