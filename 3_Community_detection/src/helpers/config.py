## function to make the model information readable, model_type to the list of files corresponding models
def paths_dict(dir:str='./data') -> dict:
    """Returns a dictionary with the models of each type."""
    model_info = {
        "MODEL": f"{dir}/model/",
        "REAL": f"{dir}/real/",
        "TOY": f"{dir}//toy/",
    }
    return model_info
