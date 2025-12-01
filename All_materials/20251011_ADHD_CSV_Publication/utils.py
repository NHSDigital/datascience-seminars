import os
import pandas as pd

def ratio_to_percentage_dp(table, col_name = 'ratio', dp_place = None, removed_empty = True,
                           col_rename = {'ratio':'percentage'} 
                           ):
    
    """
    Convert a ratio column in a pandas DataFrame to a percentage, with optional rounding,
    optional removal of rows containing missing values, and optional column renaming.
    Parameters
    ----------
    table : pandas.DataFrame
        Input DataFrame containing the ratio column to convert. Note: the function
        assigns to columns of this DataFrame (mutating it) and returns the DataFrame
        reference; some operations (e.g. dropna) return a new DataFrame assigned to
        the local variable and returned.
    col_name : str, optional
        Name of the column in `table` that holds ratio values (values expected in
        the range 0..1). Default is 'ratio'.
    dp_place : int or None, optional
        Number of decimal places to round the percentage values to. If None (the
        default), no rounding is performed.
    removed_empty : bool, optional
        If True (default), drop rows that contain any missing values using
        `DataFrame.dropna(how='any')`. If False, missing-value rows are kept.
    col_rename : dict or None, optional
        Dictionary mapping old column names to new names (passed to
        `DataFrame.rename(columns=...)`). If falsy (None or empty dict), no
        renaming is performed. Default is {'ratio': 'percentage'}.
    Returns
    -------
    pandas.DataFrame
        The resulting DataFrame after conversion/rounding/dropping/renaming. This is
        the same object as the input where column assignments occurred, but note that
        operations like `dropna` may produce and return a new DataFrame object.
    Raises
    ------
    KeyError
        If `col_name` is not present in `table`.
    TypeError
        If the specified column cannot be multiplied by 100 or rounded (e.g. non-numeric
        data that does not support these operations).
    pandas-related exceptions
        Any other exceptions raised by underlying pandas operations (e.g. invalid
        arguments passed to `round` or `rename`).
    Examples
    --------
    >>> # Convert 'ratio' to percentage with 1 decimal place, drop rows with any NA,
    >>> # and rename 'ratio' to 'percentage'
    >>> df = ratio_to_percentage_dp(df, col_name='ratio', dp_place=1,
    ...                             removed_empty=True, col_rename={'ratio': 'percentage'})
    >>> # Convert a different column without renaming or dropping
    >>> df = ratio_to_percentage_dp(df, col_name='prop', dp_place=None,
    ...                             removed_empty=False, col_rename=None)
    """
    #getting the percenage
    table[col_name] = table[col_name].multiply(100)

    #Getting the roounding to 1 dp
    if dp_place:
        table[col_name] = table[col_name].round(dp_place)

    if removed_empty:
        table = table.dropna(how = 'any')
    
    #Need to do the rename
    if col_rename:
        table = table.rename(columns = col_rename)

    return table

def save_csv_for_publication(table, name, file_path, front_marker = 'Main_'):
    """
    Save a table to a CSV file prepared for publication.
    This function ensures the provided filename ends with a .csv extension, prefixes
    the filename with a marker (default 'Main_'), constructs the full save path
    using the provided file_path (by default taken from config_param['save_path']),
    and writes the table to disk using the table.to_csv(..., index=False) method.
    Parameters
    ----------
    table :
        An object with a to_csv(path, index=False) method (commonly a pandas.DataFrame).
    name : str
        Desired filename. If the name does not end with ".csv", the extension will be appended.
    front_marker : str, optional
        String to prefix to the filename (default: 'Main_').
    file_path : str, optional
        Directory or path prefix where the file will be saved. The default is
        taken from config_param['save_path'] in the surrounding module.
    Returns
    -------
    None
        The function writes the CSV file to disk and does not return a value.
    Raises
    ------
    AttributeError
        If the `table` object does not implement a to_csv method.
    OSError
        If the file cannot be written due to filesystem issues (e.g., invalid path,
        permission denied, disk full).
    TypeError
        If `name`, `front_marker`, or `file_path` are not strings.
    Notes
    -----
    - The resulting filepath is constructed by concatenating file_path + front_marker + name.
        Ensure file_path ends with the appropriate path separator if needed.
    - The CSV is written with index=False to avoid writing row indices.
    """
    _ , file_extesion = os.path.splitext(name)

    if file_extesion != '.csv':

        name = name + '.csv'

    #Saving the csv
    path_to_save = file_path + front_marker + name

    table.to_csv(path_to_save, index = False)

def pipeline_measure_csv(config_info, key, parameters):
    """
    Process a CSV file through a data pipeline for publication.
    This function loads a CSV file, applies data transformations (ratio to percentage conversion),
    and saves the processed file to a specified output location.
    Args:
        config_info (dict): Configuration dictionary containing file paths, keyed by identifier.
        key (str): Key to access the input CSV file path from config_info.
        parameters (dict): Dictionary containing pipeline parameters, including:
            - 'output_path' (str): Directory path where the processed CSV will be saved.
    Returns:
        None
    Raises:
        KeyError: If key is not found in config_info or 'output_path' not in parameters.
        FileNotFoundError: If the CSV file at config_info[key] does not exist.
        pd.errors.ParserError: If the CSV file cannot be parsed.
    Examples:
        >>> config = {'data': '/path/to/input.csv'}
        >>> params = {'output_path': '/path/to/output/'}
        >>> pipeline_measure_csv(config, 'data', params)
    """

    #Loading the data
    csv_table =  pd.read_csv(config_info[key])

    #Data Wrangling
    csv_table = ratio_to_percentage_dp(csv_table)
    
    #Save the file
    (
        save_csv_for_publication(
            csv_table, 
            config_info[key], 
            parameters['output_path']
            )
    )