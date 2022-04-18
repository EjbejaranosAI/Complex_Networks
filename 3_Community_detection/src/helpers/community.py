## define a class to hold all the community algorithms
import networkx as nx
from .helpers import lol2idx


class NetworkXCommunityAlgs:
    def __init__(
        self, graph: nx.Graph, 
        method: str,
        layout: str,
        params:dict = {'_k':5,'_max_iter':100},
        verbosity: bool = False,
    ) -> None:
        self.method = method
        self.verbosity = verbosity
        self.layout = layout
        self.params = params
        self.algorithm = self._get_algorithm(graph, self.method, self.params)

    ## define a function for the Girvan-Newman algorithm
    @staticmethod
    def _girvan_newman(
        graph: nx.Graph,
    ) -> list:
        """
        Calculate the communities using the Girvan-Newman algorithm.
        """
        ## import community module
        from networkx.algorithms.community import greedy_modularity_communities

        communities = greedy_modularity_communities(graph)
        ## assign sgreedy_modularity_communities(g)
        communities = [c for c in communities]
        ## get the node colors
        nc = lol2idx(communities)
        ncol = list(nc.values())
        return (communities, ncol)

    ## define the function for the asyn_fluid algorithm
    def _greedy(self, graph: nx.Graph) -> list:
        """
        Calculate the communities using the asyn_fluid algorithm.
        """
        from networkx.algorithms.community import greedy_modularity_communities

        communities = greedy_modularity_communities(graph)
        ## assign fluidsgreedy_modularity_communities(g)
        communities = [c for c in communities]
        ## get the node colors
        nc = lol2idx(communities)
        #n_col = list(set([v for c in nc for k,v in c.items()]))
        return communities, nc

    ## define function for the Label Propagation algorithm
    def _label_prop(self, graph: nx.Graph) -> list:
        """
        Calculate the communities using the Label Propagation algorithm.
        """
        from networkx.algorithms.community import label_propagation

        ## get the communities
        communities = label_propagation.label_propagation_communities(graph)
        ## get the node colors
        nc = lol2idx(communities)
        #n_col = list(set([v for c in nc for k,v in c.items()]))
        return communities, nc

    ## define the function for getting the algorithm
    def _get_algorithm(self, graph: nx.Graph, method: str,params:dict) -> list:
        """
        Get the algorithm for the community detection.
        """
        ## get the communities
        if method == "girvan_newman":
            return self._girvan_newman(graph)

        if method == "greedy":
            return self._greedy(graph)

        if method == "label_prop":
            return self._label_prop(graph)

        else:
            raise ValueError(f"Method {method} is not supported.")
