import os
from config import config
import pandas as pd

def list_folders(base_path):
    """
    Lists all folders in the specified base directory.

    Args:
        base_path (str): The path to the directory in which to list folders.

    Returns:
        list: A list of folder names (str) present in the base directory.

    Raises:
        FileNotFoundError: If the base_path does not exist.
        NotADirectoryError: If the base_path is not a directory.
        PermissionError: If there is a permission issue accessing base_path.
    """
    return [name for name in os.listdir(base_path)
            if os.path.isdir(os.path.join(base_path, name))]

def remove_nth_folder_in_path(base_path,n_th= 2):
    """
    Removes the first `n_th` folders from a given file path.

    Args:
        base_path (str): The original file path.
        n_th (int, optional): The number of leading folders to remove from the path. Defaults to 2.

    Returns:
        str: The modified path with the first `n_th` folders removed. If the path has fewer than `n_th` folders, returns the original path.

    Example:
        remove_nth_folder_in_path('/home/user/project/data/file.txt', n_th=2)
        # Returns: '/project/data/file.txt/'
    """
    # Remove the first folder in the base_path
    parts = base_path.strip(os.sep).split(os.sep)
    if len(parts) > n_th:
        new_path = os.sep + os.path.join(*parts[n_th:]) + os.sep
    else:
        new_path = base_path
    return new_path


def create_table_from_list_of_folder(folders, base_path):
    """
    Generates a pandas DataFrame representing a table of contents from a list of folder names.
    Assumes folder names are in the format 'YYYYMMDD_Title'. Extracts the date and title from each folder name,
    formats the date to 'YYYY-MM-DD', and creates a Markdown link to each folder.
    Args:
        folders (list of str): List of folder names, typically in the format 'YYYYMMDD_Title'.
        base_path (str): Base directory path containing the folders.
    Returns:
        pandas.DataFrame: DataFrame with columns for date, title, and Markdown link, sorted by date.
    Notes:
        - Relies on a global 'config' dictionary for column names: 'date_column', 'title_column', 'link_column'.
        - Uses a helper function 'remove_nth_folder_in_path' to modify the base path.
        - If a folder name does not match the expected format, the date column is left empty.
        - Requires pandas and os modules.
    """

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
    """
    Updates the README file content by inserting a markdown table generated from the given DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame containing the data to be included in the markdown table.
        config (dict): Configuration dictionary with the following keys:
            - 'readme_path' (str): Path to the README file.
            - 'anchor_in_readme' (str): Anchor string in the README file where the table should be inserted.
            - 'date_column' (str): Name of the column in the DataFrame representing dates.
            - 'link_column' (str): Name of the column in the DataFrame containing links.

    Returns:
        str: The updated README content with the markdown table inserted after the specified anchor.
    """

    readme_file_path = config['readme_path']
    with open(readme_file_path,"r") as f:
        readme_string = f.read()

    readme_selected_text = readme_string.split(config['anchor_in_readme'], 1)[0] + config['anchor_in_readme']

    table_to_markdown = df[[config['date_column'], config['link_column']]].to_markdown(index=False)
    output_string = readme_selected_text + "\n\n" + table_to_markdown

    return output_string


