from .community import NetworkXCommunityAlgs
def calculate_partitions(g, pos):
    ca1 = NetworkXCommunityAlgs(g, method='girvan_newman',layout=pos, verbosity=False)
    _, ca1_nc = ca1.algorithm
    ##ASYN_FLUID: PARAMETERS: k=5, max_iter=100
    params = {'_k':5, '_max_iter':100}
    ca2 = NetworkXCommunityAlgs(g, method='asyn_fluid',layout=pos, verbosity=False, params=params)
    _, ca2_nc = ca2.algorithm
    ## Label Propagation
    ca3 = NetworkXCommunityAlgs(g, method='label_prop',layout=pos, verbosity=False)
    _, ca3_nc = ca3.algorithm
    ## CN-Moore  
    params = {'n_comm':3} ## number of communities 
    ca4 = NetworkXCommunityAlgs(g, method='cn_moore',layout=pos, verbosity=False, params=params)
    _, ca4_nc = ca4.algorithm
    return [[ca1_nc,ca1.method],[ca2_nc,ca2.method],[ca3_nc,ca3.method],[ca4_nc,ca1.method]]