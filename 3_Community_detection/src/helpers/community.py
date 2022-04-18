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
        from networkx.algorithms.community.centrality import girvan_newman

        ## get the communities
        communities = girvan_newman(graph)
        ## map the communities to the nodes
        node_colors = [lol2idx(comms) for comms in communities]
        ## node colors 
        n_col = list(set([v for c in node_colors for _,v in c.items()]))
        ## return the communities
        return (communities, n_col)

    ## define the function for the asyn_fluid algorithm
    def _asyn_fluid(self, graph: nx.Graph,params:dict) -> list:
        """
        Calculate the communities using the asyn_fluid algorithm.
        """
        from networkx.algorithms.community import asyn_fluid

        ## assign fluids
        fluids = asyn_fluid.asyn_fluidc(G=graph, k=params['_k'], max_iter=params['_max_iter'])
        ## get the communities
        communities = [fluid for fluid in fluids]
        ## get the node colors
        nc = lol2idx(communities)
        #n_col = list(set([v for c in nc for k,v in c.items()]))
        return communities, nc

    ## define function for the Label Propagation algorithm
    def _label_prop(self, graph: nx.Graph, _max_iter: int = 100) -> list:
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
    
    ## Clauset-Newman-Moore algorithm (Greedy)
    def _cn_moore(self, graph: nx.Graph, params:dict) -> list:
        """
        Calculate the communities using the Clauset-Newman-Moore algorithm.
        """
        n_comm = params['n_comm']
        from networkx.algorithms.community import greedy_modularity_communities
        communities = greedy_modularity_communities(graph, n_comm)
        nc = lol2idx(communities)
        #n_col = list(set([v for c in nc for k,v in c.items()]))
        return communities,nc

    ## define the function for getting the algorithm
    def _get_algorithm(self, graph: nx.Graph, method: str,params:dict) -> list:
        """
        Get the algorithm for the community detection.
        """
        ## get the communities
        if method == "girvan_newman":
            return self._girvan_newman(graph)

        if method == "asyn_fluid":
            return self._asyn_fluid(graph,params)

        if method == "label_prop":
            return self._label_prop(graph)
        
        if method == 'cn_moore':
            return self._cn_moore(graph,params)

        else:
            raise ValueError(f"Method {method} is not supported.")
