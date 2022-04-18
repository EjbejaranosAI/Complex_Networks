## imports 
import networkx as nx 
import matplotlib.pyplot as plt
## progress bar 
from tqdm import tqdm 
import community 
from termcolor import colored
from .helpers import read_clu,load_graph_coords


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
    for k, v in data.items():
    #for k, v in tqdm(data.items()):
            ## the key is the current filename 
            fn = f"{data_dir}/{net_type}/{k}.net"
            ## need to create a figure and axis with the corresponding length
            ## corr_length = key + len(values)
            dim = 1
            num_plots = len(v) + 1 if len(v) > 0 else 1
            ## checking if to adjust the size of the graph 
            ## assuming that a length of 4 is too large for a (1xN) graph, convert it to a (2xN//2)
            if num_plots >= 4:
                dim = 2
                num_plots = num_plots // 2
                figure_size = (30,20)
            print(f"{len(v)} partition(s) found for {k}")
            if len(v) == 0: # there are no partitions ## plot the original with a good partition Louvain
                ## generating a partition for the graph
                ## import the colored module 
                part = community.community_louvain.best_partition(g)      # Louvain algorithm
                name = 'Louvain algorithm'
                txt2print = f">> Generated a partition for {k} with {name}<<"
                print(colored(txt2print, 'red'))
                comms = [part.get(node) for node in g.nodes()]
                ## create the figure with the original graph 
                fig1, axs1 = plt.subplots(1,2,figsize=figure_size)
                nx.draw(g,pos=pos, ax=axs1[0])
                axs1[0].set_title(f"Original partition for: {k}")
                nx.draw(g,pos=pos,node_color=comms, ax=axs1[1])
                axs1[1].set_title(f"No Partition, showing: {name}")
                plt.suptitle(f"{net_type.upper()} Networks & Partitions ({k})")
                plt.savefig(f"{save_dir}/{net_type}/network_{k}_partitions_{len(v)}.png")
                if visualize:
                    plt.show()
                plt.close()
            else:
                fig, axs = plt.subplots(dim, num_plots, figsize=figure_size)
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
                    cl = read_clu(part) # original partition 
                    ## plot to the corresponding axs 
                    nx.draw(g,pos=pos,node_color=cl, ax=axs[idx])
                    ## add the corresponding title 
                    axs[idx].set_title(f"Partition: {pn}")
                ## add the title 
                plt.suptitle(f"{net_type.upper()} Networks & Partitions ({k})")
                ## save the images 
                plt.savefig(f"{save_dir}/{net_type}/network_{k}_partitions_{len(v)}.png")
                if visualize:
                    plt.show()
                plt.close()