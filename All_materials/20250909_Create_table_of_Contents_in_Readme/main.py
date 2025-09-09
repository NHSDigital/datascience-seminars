import os
from config import config
import pandas as pd
from utils import *

if __name__ == "__main__":

    #Table creation
    base_path = config['base_path']
    folders = list_folders(base_path)

    #Getting the table
    table_name = create_table_from_list_of_folder(folders,config['base_path'])

    #Editing the readme
    output_string = create_readme_with_updated_table(table_name, config)

    with open(config['readme_path'], "w") as f:
        f.write(output_string)