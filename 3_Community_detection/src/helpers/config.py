## function to make the model information readable, model_type to the list of files corresponding models
def config_dict(dir:str='./data') -> dict:
    """Returns a dictionary with the models of each type."""
    model_info = {
        "model": f"{dir}/model",
        "real": f"{dir}/real",
        "toy": f"{dir}/toy",
    }
    return model_info
