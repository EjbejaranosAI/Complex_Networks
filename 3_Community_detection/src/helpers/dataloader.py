## getting all the NET Files and .CLU Files 
def get_net_clu_files(data_dir:str) -> tuple:
    """Finds the .NET and .CLU files in a given directory"""
    import glob 
    net_files,clu_files = glob.glob(data_dir+'/*.net'),glob.glob(data_dir+'/*.clu')
    return (net_files, clu_files)

## order all the data
from collections import defaultdict
## make a dictionary: {Model_name: [Partitions]}
def make_file_dict(net_partition_files:tuple, verbose:bool=False) -> defaultdict:
    """Returns a defaultdict(list) for the names and the respective partition
    net_partition_files: tuple (net, clu)
    """
    ## first get the names of the net_partitions_files 
    ## get the corresponding .net and .clu files, if any 
    names = [x.split("/")[-1].split(".")[0] for x in net_partition_files[0]]
    d = defaultdict(list)
    for k in names:
        for v in net_partition_files[1]:
            _name = v.split("/")[-1]
            if k in _name and v not in d[k]:
                d[k].append(v)
            else:
                d[k]
    if verbose: 
        for k, v in d.items():
            print(f"\nModel Name:\t{k} |\tN_Partitions: {len(v)}\nPartitions: {v}")
    return d