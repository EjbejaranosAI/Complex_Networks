import igraph 
import pandas as pd
class AirportDescriptor:
    """
                        1.Degree *
                        2.Strength*
                        3.Clustering coefficient - NO SE SI ESTA BIEN
                        4.Average path length (average distance to the rest of the nodes)*
                        5.Maximum path length (maximum distance to the rest of the nodes)*
                        6.Betweenness*
                        7.Eigenvector centrality -FALTA ESCOGER SOLO LOS VALORES DE LOS AEROPUERTOS
                        8.PageRank*
                        
    Degree --> DONE
    Strength --> DONE
    Clustering coefficient --> DONE
    Average path length (average distance to the rest of the nodes) --> DONE
    Maximum path length (maximum distance to the rest of the nodes) --> DONE
    Betweenness --> DONE!!
    Eigenvector centrality --> DONE!!!
    PageRank

    
    """
    def __init__(self, loaded_graph:igraph.Graph,) -> pd.DataFrame:
        """Object to calculate all the descriptors for the real graph"""
        self.model = loaded_graph 
        # pass the list of airports 
        self.names = [x['name'] for x in self.model.vs()]
        # weights 
        self.weights = [x['weight'] for x in self.model.es()]
        # degrees 
        self.degree = [round(self.model.degree(vertices=v['id']), 8) for v in self.model.vs()]
        # strenghts 
        #self.strength = [round(self.model.degree(vertices=v['id']), 8) for v in self.model.vs()]
        self.strength = [round(self.model.strength(vertices=v['id']), 8) for v in self.model.vs()]
        ## clustering coefficient 
        self.cluster_coef = [round(self.model.transitivity_local_undirected(vertices=v['id']),8) for v in self.model.vs()]
        ## average path length 
        self.average_path = 0
        
        ## eigenvector centrality 
        self.eigen_centrality = self.model.eigenvector_centrality(directed=False)
        self.eigen_cent_rounded = list(map(lambda x: round(x, 8),self.eigen_centrality))
        
        
        # betweenness 
        self.between = self.model.betweenness(self.names, directed=False)
    

    
    def _summary(self):
        
        network_dict = {
                        "Degree":self.degree,
                        "Strength":self.strength, 
                        "Cluster_Coefficient":self.cluster_coef,
                        
                        "Betweenness": self.between,
            
                        }
        
        return network_dict