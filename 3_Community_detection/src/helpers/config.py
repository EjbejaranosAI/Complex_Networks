## function to make the model information readable, model_type to the list of files corresponding models
def config_dict(dir:str='./data') -> dict:
    """Returns a dictionary with the models of each type."""
    model_info = {
        "model": f"{dir}/model",
        "real": f"{dir}/real",
        "toy": f"{dir}/toy",
    }
    return model_info
def make_net_file_dict(CONFIG:dict) -> dict:
    """Returns the config, Net files & file dict"""    
    from .dataloader import make_file_dict, get_net_clu_files
    ## getting all the net & clu files 
    NET_FILES = list(map(get_net_clu_files, CONFIG.values()))
    ## make a dictionary to hold them 
    FILE_DICT = list(map(make_file_dict, NET_FILES))
    ## add the NAMES items to the dictionary 
    FILE_DICT = dict(zip(CONFIG.keys(), FILE_DICT))
    return NET_FILES,FILE_DICT
    
    
