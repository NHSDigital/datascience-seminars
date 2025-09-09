import os
from config import config
import pandas as pd

def list_folders(base_path):
    return [name for name in os.listdir(base_path)
            if os.path.isdir(os.path.join(base_path, name))]

def remove_nth_folder_in_path(base_path,n_th= 2):
    # Remove the first folder in the base_path
    parts = base_path.strip(os.sep).split(os.sep)
    if len(parts) > n_th:
        new_path = os.sep + os.path.join(*parts[n_th:]) + os.sep
    else:
        new_path = base_path
    return new_path


def create_table_from_list_of_folder(folders, base_path):
    # Assuming folder names are in the format 'YYYYMMDD_Title'
    data = []

    #Need to remove the first folder 
    base_path = remove_nth_folder_in_path(base_path)

    for folder in folders:
        parts = folder.split('_', 1)
        if len(parts) == 2:
            date, title = parts
            data.append({config['date_column']: date, 
                         config['title_column']: title,
                         config['link_column']: f"[{title.replace('_', ' ')}]( {os.path.join(base_path, folder)})"
                         })
        else:
            data.append({config['date_column']: '', 
                         config['title_column']: folder,
                         config['link_column']: f"[{folder.replace('_', ' ')}]( {os.path.join(base_path, folder)})"
                         })

    for row in data:
        if row[config['date_column']]:
            try:
                dt = pd.to_datetime(row[config['date_column']], format='%Y%m%d')
                row[config['date_column']] = dt.strftime('%Y-%m-%d')
            except Exception:
                pass

    df = pd.DataFrame(data)
    df = df.sort_values(by=config['date_column'], ascending=True).reset_index(drop=True)

    return df

def create_readme_with_updated_table(df,config):

    readme_file_path = config['readme_path']
    with open(readme_file_path,"r") as f:
        readme_string = f.read()

    readme_selected_text = readme_string.split(config['anchor_in_readme'], 1)[0] + config['anchor_in_readme']

    table_to_markdown = df[[config['date_column'], config['link_column']]].to_markdown(index=False)
    output_string = readme_selected_text + "\n\n" + table_to_markdown

    return output_string


