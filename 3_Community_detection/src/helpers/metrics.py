## will hold the collection of metrics
import numpy as np
import networkx as nx



def compute_metrics(l1,l2):
    ## normalized mutual information
    _nmi = nmi(l1,l2)
    ## jaccard index 
    jac_idx = jaccard_index(l1,l2)
    ## randindex 
    rand_id = rand_index(l1,l2)
    ## nvi = normalized variation of information
    _nvi = nvi_from_nmi(l1,l2,len(l1))

    ## feedback 
    print(f"NMI: {_nmi:.2f}")
    print(f"Jaccard index: {jac_idx:.2f}")
    print(f"Rand index: {rand_id:.2f}")
    print(f"NVI: {_nvi:.2f}")
    tracker_metrics = {'nmi':_nmi,
                    'jaccard_index':jac_idx,
                    'rand_index':rand_id,
                    'nvi':_nvi}

    return tracker_metrics



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


## Normalized Variation of Information
def nvi(
    community1,
    community2,
):
    """Implement the Normalized Variation of Information from igraph.
    Which uses the community and variation of information between two clusters.

    Variation of information is defined as the difference between the entropy of the two clusters
    and the entropy of the joint distribution.
    """
    pass


## define the function to calculate the entropy of two clusters


def modularity(g: nx.Graph, community: list) -> float:
    """Calculate the modularity of a graph given a community."""
    import networkx.algorithms.community as nx_comm

    ## calculate the modularity
    return nx_comm.modularity(g, community)
