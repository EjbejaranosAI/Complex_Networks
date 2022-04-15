import glob
## define the function to load the files 
def get_file_list(dir_to_files: str) -> list:
    """
    get the list of files in the directory 
    """
    return glob.glob(dir_to_files+"/*")

## define a function that matches the .net file with the corresponing .clu file 
def get_clu_file(file_information:list) -> dict:
    """
    get a dictionary with the following structure: 
    For each model type (e.g. MODEL, REAL, TOY), there will be three keys: 
    - 'model_type': the model type
    - 'model_file': the model file
    - 'clu_file': the corresponding .clu file
    """
    ## get the file name

## define function to iterate through a list of files and returns get_file_list
def get_file_list_iter(model_info: str) -> list:
    """
    get the list of files in the directory and store them as a dictionary
    d = {'model_type': file_list}
    """
    ## get the list of files
    list_of_files = list(map(get_file_list, model_info.values()))
    ## dictionary 
    model_dict = {k:v for k,v in zip(model_info.keys(), list_of_files)}
    return model_dict