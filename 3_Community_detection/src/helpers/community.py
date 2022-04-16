## define a class to hold all the community algorithms 
import networkx as nx 


class CommunityAlgs:
    def __init__(self, graph:nx.Graph, method:str):
        self.graph = graph
        self.method = method
        self.mapper = self._get_mapper(self.graph)
        self.algorithm = self._get_algorithm(self.graph, self.method) 
    
    ## define a function for the Girvan-Newman algorithm
    def _girvan_newman(self, graph:nx.Graph, verbosity:bool) -> list:
        """
        Calculate the communities using the Girvan-Newman algorithm.
        """
        ## import community module
        from networkx.algorithms.community.centrality import girvan_newman
        from helpers import lol2idx
        ## get the communities
        communities = list(girvan_newman(graph))
        num_coms = len(communities)
        if verbosity:
            ## print the number of communities 
            print(f"Number of communities: {num_coms}")
        ## map the communities to the nodes
        node_colors = [lol2idx(comms) for comms in communities]
        ## return the communities
        return (communities,node_colors)
        
    ## define the function for getting the algorithm 
    def _get_algorithm(self, graph:nx.Graph, method:str) -> list:
        """
        Get the algorithm for the community detection.
        """
        ## get the communities
        if method == "girvan_newman":
            return self._girvan_newman(graph, verbosity=False)
        if method == 'fastgreedy':
            return self._fastgreedy(graph, verbosity=False)
        if method == 'label_propagation':
            return self._label_propagation(graph, verbosity=False)
        if method == 'walktrap':
            return self._walktrap(graph, verbosity=False)
        else:
            raise ValueError(f"Method {method} is not supported.")
    
    @staticmethod
    def _get_mapper(graph:nx.Graph) -> dict:
        """
        Get the mapper from the graph.
        """
        ## get the mapper
        mapper = {name:idx for idx, name in  enumerate(graph.nodes())}
        return mapper