### Graph Embeddings

Last update: August 2019.

---

Numpy/CVXPY implementations of a few methods to embed the structure of a graph into its nodes. 
These methods assume access to only an adjacency matrix <img alt="$A \in \{0,1\}^{n,n}$" src="svgs/e909d92b706366ac5f3bbec0d2de7d15.svg" align="middle" width="92.75883704999998pt" height="24.65753399999998pt"/> and admit embeddings <img alt="$X \in \mathbb{R}^{n,d}$" src="svgs/a85c88c064c138925195462541923c5e.svg" align="middle" width="65.74521854999999pt" height="27.91243950000002pt"/>; one for each node.

Note that each methods need to be permutation invariant, i.e.
<p align="center"><img alt="$$&#10;f(A) = f(P A P^\top), \text{ for all permutation matrices} P&#10;$$" src="svgs/02aa76bac0650670f4e681c5143ed759.svg" align="middle" width="356.68431975pt" height="18.88772655pt"/></p>

So far we implement:

- Laplacian eigenmaps [1]. Both normalized and un-normalized versions.

- Locally linear embeddings [2]. We use the fixed adjacency matrix <img alt="$A$" src="svgs/53d147e7f3fe6e47ee05b88b166bd3f6.svg" align="middle" width="12.32879834999999pt" height="22.465723500000017pt"/> as weights.

- Structure-preserving embeddings [3]. Warning: implementation does not scale at all.

Below we show an example of the embeddings for a community dataset on 18 nodes. Notice how prevalent the community structure is within the first two features of each embedding.

![](examples/ex.png)

#### References

[1] Belkin, M., and Niyogi, P. (2003). Laplacian Eigenmaps for Dimensionality Reduction and Data Representation. Neural Computation 15, 1373–1396.

[2] Roweis, S.T., and Saul, L.K. (2000). Nonlinear Dimensionality Reduction by Locally Linear Embedding. Science 290, 2323–2326.

[3] Shaw, B., and Jebara, T. (2009). Structure Preserving Embedding. In Proceedings of the 26th Annual International Conference on Machine Learning, (New York, NY, USA: ACM), pp. 937–944.

#### License

This code is available under the MIT License.

