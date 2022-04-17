## define a class to hold all the community algorithms
import networkx as nx
from .helpers import lol2idx
from igraph import Graph
import igraph as ig
from matplotlib import pyplot as plt

class NetworkXCommunityAlgs:
    def __init__(
        self, graph: nx.Graph, 
        method: str,
        layout: str,
        params:dict = {'_k':5,'_max_iter':100},
        verbosity: bool = False,
    ) -> None:
        self.graph = graph
        self.method = method
        self.mapper = self._get_mapper(self.graph)
        self.verbosity = verbosity
        self.layout = layout
        self.params = params
        self.algorithm = self._get_algorithm(self.graph, self.method, self.params)
        

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



     
class IgraphCommunityAlgs:
    def __init__(
        self, graph: Graph, 
        method: str,
        layout: str,
        params:dict = {'_k':5,'_max_iter':100},
        verbosity: bool = False,
    ) -> None:
        self.graph = graph
        self.method = method
        #self.mapper = self._get_mapper(self.graph)
        self.verbosity = verbosity
        self.layout = layout
        self.params = params
        self.algorithm = self._get_algorithm(self.graph, self.method)
        

    # 1.Girvan newman algorithm
    def _girvan_newman(self, graph):
        # Use edge betweenness to detect communities
        communities = graph.community_edge_betweenness()
        # ... and convert into a VertexClustering for plotting
        communities = communities.as_clustering()

        # Color each vertex and edge based on its community membership
        num_communities = len(communities)
        palette = ig.RainbowPalette(n=num_communities)
        for i, community in enumerate(communities):
            graph.vs[community]["color"] = i
            community_edges = graph.es.select(_within=community)
            community_edges["color"] = i


            # FUNCTION TO DRAW COMMUNITIES    
        
        # Plot with only vertex and edge coloring
        fig, ax = plt.subplots()
        ig.plot(
            communities,
            palette=palette,
            edge_width=1,
            target=ax,
            vertex_size=13,
        )
        legend_handles = []
        for i in range(num_communities):
            handle = ax.scatter(
                [], [],
                s=100,
                facecolor=palette.get(i),
                edgecolor="k",
                label=i,
            )
            legend_handles.append(handle)

        ax.legend(
            handles=legend_handles,
            title='Community:',
            bbox_to_anchor=(0, 0),
            bbox_transform=ax.transAxes,
        )
        plt.show()
        return (communities, palette, num_communities,fig)

    # 2.fast_gredy algorithm
 
    def _fast_greedy(self, graph):
        # Use edge betweenness to detect communities
        communities = graph.community_fastgreedy()
        # ... and convert into a VertexClustering for plotting
        communities = communities.as_clustering()

        # Color each vertex and edge based on its community membership
        num_communities = len(communities)
        palette = ig.RainbowPalette(n=num_communities)
        for i, community in enumerate(communities):
            graph.vs[community]["color"] = i
            community_edges = graph.es.select(_within=community)
            community_edges["color"] = i


            # FUNCTION TO DRAW COMMUNITIES    
        
        # Plot with only vertex and edge coloring
        fig, ax = plt.subplots()
        ig.plot(
            communities,
            palette=palette,
            edge_width=1,
            target=ax,
            vertex_size=13,
        )
        legend_handles = []
        for i in range(num_communities):
            handle = ax.scatter(
                [], [],
                s=100,
                facecolor=palette.get(i),
                edgecolor="k",
                label=i,
            )
            legend_handles.append(handle)

        ax.legend(
            handles=legend_handles,
            title='Community:',
            bbox_to_anchor=(0, 0),
            bbox_transform=ax.transAxes,
        )
        plt.show()
        return (communities, palette, num_communities,fig)


    # 3. Label propagation algorithm
    def _label_prop(self, graph):
        # Use edge betweenness to detect communities
        communities = graph.community_label_propagation()
        # ... and convert into a VertexClustering for plotting
        #communities = communities.as_clustering()

        # Color each vertex and edge based on its community membership
        num_communities = len(communities)
        palette = ig.RainbowPalette(n=num_communities)
        for i, community in enumerate(communities):
            graph.vs[community]["color"] = i
            community_edges = graph.es.select(_within=community)
            community_edges["color"] = i


            # FUNCTION TO DRAW COMMUNITIES    
        
        # Plot with only vertex and edge coloring
        fig, ax = plt.subplots()
        ig.plot(
            communities,
            palette=palette,
            edge_width=1,
            target=ax,
            vertex_size=13,
        )
        legend_handles = []
        for i in range(num_communities):
            handle = ax.scatter(
                [], [],
                s=100,
                facecolor=palette.get(i),
                edgecolor="k",
                label=i,
            )
            legend_handles.append(handle)

        ax.legend(
            handles=legend_handles,
            title='Community:',
            bbox_to_anchor=(0, 0),
            bbox_transform=ax.transAxes,
        )
        plt.show()
        return (communities, palette, num_communities,fig)


    ## define the function for getting the algorithm
    def _get_algorithm(self, graph: Graph, method: str) -> list:
        """
        Get the algorithm for the community detection.
        """
        ## get the communities
        if method == "girvan_newman":
            return self._girvan_newman(graph)

        if method == "fastgreedy":
            return self._fastgreedy(graph)

        if method == "label_prop":
            return self._label_prop(graph)
        
        if method == 'cn_moore':
            return self._cn_moore(graph)

        else:
            raise ValueError(f"Method {method} is not supported.")

        
    '''    @staticmethod
    def _get_mapper(graph: Graph) -> dict:
        """
        Get the mapper from the graph.
        """
        ## get the mapper
        mapper = {name: idx for idx, name in enumerate(graph.nodes())}
        return mapper'''    
    

