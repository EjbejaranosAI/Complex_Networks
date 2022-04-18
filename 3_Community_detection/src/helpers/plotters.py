## imports 
import networkx as nx 
import matplotlib.pyplot as plt
## progress bar 
from tqdm import tqdm 
from src.helpers.helpers import read_clu,load_graph_coords


def plot_graph_partition_original(data:dict,
                                  net_type:str,
                                  data_dir:str,
                                  figure_size:tuple,
                                  save_dir:str,
                                  visualize:bool=False) -> None:
    """Function which plots the graphs and the partition.
    Steps: 
    1. iterate over the keys in the data-dictionary (our data holder)
    2. Adjusts the file name 
    3. Dynamic adjustment of the graph based on the number of partitions 
    4. Loads the graph and the coordinates of the network 
    5. Iterates over the keys (partitions) of each network 
    6. Plots the original graph and its partitions 
    7. Saves to the specified directory
    """
    ## iterate over the keys 
    for k, v in tqdm(data.items()):
        ## if there is no partition, only plot the original graph 
        if len(v) <= 0:
            ## load the graph 
            g, pos = load_graph_coords(file_path = fn)
            ## draw the original graph 
            nx.draw(g, pos=pos)
            ## save it 
            ## add the title 
            plt.title(f"{net_type.upper()} Networks & Partitions ({k})")
            if visualize and save_dir is not None: 
                plt.show()
                ## save the images 
                plt.savefig(f"{save_dir}/{net_type}/network_{k}_partitions_{len(v)}.png")
            else: 
                plt.savefig(f"{save_dir}/{net_type}/network_{k}_partitions_{len(v)}.png")
        else:     
            ## the key is the current filename 
            fn = f"{data_dir}/{net_type}/{k}.net"
            ## need to create a figure and axis with the corresponding length
            ## corr_length = key + len(values)
            _dim = 1
            num_plots = len(v) + 1 if len(v) > 0 else 1
            ## checking if to adjust the size of the graph 
            ## assuming that a length of 4 is too large for a (1xN) graph, convert it to a (2xN//2)
            if num_plots >= 4:
                _dim = 2
                num_plots = num_plots // 2
                figure_size = (30,20)
            fig, axs = plt.subplots(_dim, num_plots, figsize=figure_size)
            ## if there is no partition, plot the original
            axs = axs.ravel()
            ## load the graph 
            g, pos = load_graph_coords(file_path = fn)
            ## draw the original graph 
            nx.draw(g, pos=pos, ax=axs[0])
            ## add the corresponding title 
            axs[0].set_title(f"Original Network: {k}")
            ## iterate over the partitions 
            for idx,part in enumerate(v):
                ## get the actual name of the partition 
                pn = part.split('/')[-1].split('.')[0]
                ## idx = idx + 1 because we omit the first column
                idx = idx + 1
                ## load the partition
                cl = dict(read_clu(part)) # original partition 
                ## plot to the corresponding axs 
                nx.draw(g,pos=pos,node_color=list(cl.values()), ax=axs[idx])
                ## add the corresponding title 
                axs[idx].set_title(f"Partition: {pn}")
            ## add the title 
            plt.suptitle(f"{net_type.upper()} Networks & Partitions ({k})")
            ## save the images 
            plt.savefig(f"{save_dir}/{net_type}/network_{k}_partitions_{len(v)}.png")
        if visualize:
            plt.show()
        else: 
            plt.clf()
            plt.cla()
            plt.close()