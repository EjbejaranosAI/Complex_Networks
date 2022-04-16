## define a class to hold all the community algorithms
import networkx as nx
from .helpers import lol2idx


class CommunityAlgs:
    def __init__(
        self, graph: nx.Graph, method: str, layout: str, verbosity: bool = False
    ) -> None:
        self.graph = graph
        self.method = method
        self.mapper = self._get_mapper(self.graph)
        self.verbosity = verbosity
        self.algorithm = self._get_algorithm(self.graph, self.method)
        self.layout = layout

    ## define a function for the Girvan-Newman algorithm
    def _girvan_newman(
        self,
        graph: nx.Graph,
    ) -> list:
        """
        Calculate the communities using the Girvan-Newman algorithm.
        """
        ## import community module
        from networkx.algorithms.community.centrality import girvan_newman

        ## get the communities
        communities = list(girvan_newman(graph))
        ## map the communities to the nodes
        node_colors = [lol2idx(comms) for comms in communities]
        ## return the communities
        return (communities, node_colors)

    ## define the function for the asyn_fluid algorithm
    def _asyn_fluid(self, graph: nx.Graph, _k: int = 5, _max_iter: int = 100) -> list:
        """
        Calculate the communities using the asyn_fluid algorithm.
        """
        from networkx.algorithms.community import asyn_fluid

        ## assign fluids
        fluids = asyn_fluid.asyn_fluidc(G=graph, k=_k, max_iter=_max_iter)
        ## get the communities
        communities = [fluid for fluid in fluids]
        ## get the node colors
        nc = lol2idx(communities)
        return communities, nc

    ## define function for the Label Propagation algorithm
    def _label_prop(self, graph: nx.Graph, _max_iter: int = 100) -> list:
        """
        Calculate the communities using the Label Propagation algorithm.
        """
        from networkx.algorithms.community import label_propagation

        ## get the communities
        communities = label_propagation.label_propagation_communities(
            graph, max_iter=_max_iter
        )
        ## get the node colors
        nc = lol2idx(communities)
        return communities, nc

    @staticmethod
    def _get_mapper(graph: nx.Graph) -> dict:
        """
        Get the mapper from the graph.
        """
        ## get the mapper
        mapper = {name: idx for idx, name in enumerate(graph.nodes())}
        return mapper

    ## define the function for getting the algorithm
    def _get_algorithm(self, graph: nx.Graph, method: str) -> list:
        """
        Get the algorithm for the community detection.
        """
        ## get the communities
        if method == "girvan_newman":
            return self._girvan_newman(graph)

        if method == "asyn_fluid":
            return self._asyn_fluid(graph)

        if method == "label_prop":
            return self._label_prop(graph)

        else:
            raise ValueError(f"Method {method} is not supported.")
