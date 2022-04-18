from .community import NetworkXCommunityAlgs
import community
def calculate_partitions(g, pos):
    ## girvan 
    ca1 = NetworkXCommunityAlgs(g, method='girvan_newman',layout=pos, verbosity=False)
    _, ca1_nc = ca1.algorithm
    ##greedy (modularity):
    ca2 = NetworkXCommunityAlgs(g, method='greedy',layout=pos, verbosity=False)
    _, ca2_nc = ca2.algorithm
    ## Label Propagation
    ca3 = NetworkXCommunityAlgs(g, method='label_prop',layout=pos, verbosity=False)
    _, ca3_nc = ca3.algorithm
    return [[ca1_nc,ca1.method],[ca2_nc,ca2.method],[ca3_nc,ca3.method]]

def make_best_partition(graph):
  ## 
  part = community.community_louvain.best_partition(graph)
  ## communities
  comms = [part.get(node) for node in graph.nodes()]
  return comms