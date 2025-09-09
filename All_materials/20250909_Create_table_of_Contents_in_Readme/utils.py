import os
from config import config
import pandas as pd

def list_folders(base_path):
    return [name for name in os.listdir(base_path)
            if os.path.isdir(os.path.join(base_path, name))]

def create_table_from_list_of_folder(folder, base_path):
    # Assuming folder names are in the format 'YYYYMMDD_Title'
    data = []
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

# def create_markdown_link(table_name,config):

#     #Making a new row
#     table_name[config['link_column']] = table_name[config['title_column']].apply(lambda x: f"[{x}]({x})")

#     return table_name

if __name__ == "__main__":

    #Table creation
    base_path = config['base_path']
    folders = list_folders(base_path)
    print(folders)

    #Getting the table
    table_name = create_table_from_list_of_folder(folders,config['base_path'])

    
