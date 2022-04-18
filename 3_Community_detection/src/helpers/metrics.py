## will hold the collection of metrics
import numpy as np
import networkx as nx

## Normalized Mutual Information (NMI)
def nmi(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Calculates the normalized mutual information between two clusterings.
    """
    from sklearn.metrics import normalized_mutual_info_score

    return normalized_mutual_info_score(y_true, y_pred)


## jaccard index
def jaccard_index(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Calculate the jaccard index of two lists."""
    intersection = len(list(set(y_true).intersection(y_pred)))
    union = (len(y_true) + len(y_pred)) - intersection
    return float(intersection / union)


## rand index
def rand_index(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Calculate the rand index of two lists."""
    from sklearn.metrics import adjusted_rand_score

    return adjusted_rand_score(y_true, y_pred)


## Normalized Variation of Information.
def nvi_from_nmi(y_true: np.ndarray, y_pred: np.ndarray, vertices: int) -> float:
    """Calculate the normalized variation of information between two lists."""
    from sklearn.metrics import normalized_mutual_info_score
    return normalized_mutual_info_score(y_true, y_pred) / np.log(vertices)


## define the function to calculate the entropy of two clusters


def modularity(g: nx.Graph, community: list) -> float:
    """Calculate the modularity of a graph given a community."""
    import networkx.algorithms.community as nx_comm
    

    ## calculate the modularity
    return nx_comm.modularity(g, community)



def calculate_metrics(graph, data:list, community_alg:list,community_idx:list):
    """Calculate NVI, NMI & Rand Index"""
    import math
    import igraph as ig
    nvi = ig.compare_communities(data, community_alg,method='vi')/math.log(len(data))
    nmi = ig.compare_communities(data, community_alg,method='nmi')
    rand_idx = ig.compare_communities(data, community_alg, method='rand')
    modularity = graph.modularity(community_idx)
    ## printmetrics rounded to 2 decimal places 
    #print(f"| NVI: {round(nvi,2)} | NMI: {round(nmi,2)} | Rand Index: {round(rand_idx,2)}")
    return (nvi, nmi, rand_idx, modularity)