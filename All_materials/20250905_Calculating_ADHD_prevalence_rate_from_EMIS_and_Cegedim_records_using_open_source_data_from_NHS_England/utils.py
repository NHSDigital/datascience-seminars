import pandas as pd
import requests
from config import config
import os
import zipfile

def getting_start_ends_dates(each_key):
    """
    Given a string key representing a financial year in the format 'YYZZ', returns the start and end dates
    of the financial year in 'YYYY-MM-DD' format.

    Args:
        each_key (str): A string representing the financial year, where the first two characters are the
                        starting year (last two digits) and the last two characters are the ending year
                        (last two digits). For example, '1920' for the 2019-2020 financial year.

    Returns:
        tuple: A tuple containing two strings:
            - start_date (str): The start date of the financial year in 'YYYY-MM-DD' format (April 1st).
            - end_date (str): The end date of the financial year in 'YYYY-MM-DD' format (March 31st).

    Example:
        >>> getting_start_ends_dates('1920')
        ('2019-04-01', '2020-03-31')
    """

    start_date = '20' + each_key[:2] + '-04-01'
    end_date = '20' + each_key[-2:] + '-03-31'

    return start_date, end_date

def wrangling_table_to_opensafely_form(each_csv,each_key,config):
    """
    Transforms and aggregates a DataFrame to match the output format required by OpenSAFELY.
    This function performs the following steps:
    1. Selects columns of interest from the input DataFrame.
    2. Renames the values in the sex column according to the provided mapping.
    3. Filters and aggregates rows to compute numerator and denominator counts based on indicator values.
    4. Merges the aggregated numerator and denominator counts on specified groupby indices.
    5. Calculates the ratio of numerator to denominator for each group.
    6. Adds interval start and end dates based on the provided key.
    7. Reorders and selects columns to match the OpenSAFELY output specification.
    Args:
        each_csv (pd.DataFrame): The input DataFrame containing raw data.
        each_key (Any): A key used to determine the interval start and end dates.
        config (dict): A configuration dictionary specifying column names, mappings, and other parameters.
    Returns:
        pd.DataFrame: A DataFrame formatted according to OpenSAFELY requirements, including computed ratios and interval dates.
    """

    #Wrangle the file to match opensafely's outputs

    #Getting the correct cols
    each_csv = each_csv[config['cols_of_interest']]

    #Rename the Sex col
    each_csv[config['nhs_sex_col']] = each_csv[config['nhs_sex_col']].replace(config['sex_rename'])

    #Computing the ratio
    each_adhd_counts = each_csv[each_csv[config['nhs_indicator_col']].isin(config['numerator'])]
    each_all_counts = each_csv[each_csv[config['nhs_indicator_col']].isin(config['denominator'])]
    #Need to correct the age bands
    each_all_counts = each_all_counts.replace({config['nhs_ageband_col']:config['age_band_correction']})

    each_adhd_counts = each_adhd_counts.groupby(config['groupby_index'], as_index=False)[config['nhs_vaule_col']].sum()
    each_adhd_counts = each_adhd_counts.rename(columns=config['rename_col_for_numerator'])

    each_all_counts = each_all_counts.groupby(config['groupby_index'], as_index=False)[config['nhs_vaule_col']].sum()
    each_all_counts = each_all_counts.rename(columns=config['rename_col_for_denominator'])

    #Join
    each_ratio = each_all_counts.merge(each_adhd_counts, how='left', on=config['groupby_index'])
    each_ratio = each_ratio.rename(columns=config['rename_cols_indices'])

    #Computing the ratio
    each_ratio[config['nhs_ratio_col']] = each_ratio[config['nhs_numerator_col']]/each_ratio[config['nhs_denominator_col']]

    #Need to set out the year
    start_date, end_date = getting_start_ends_dates(each_key)

    each_ratio[config['interval_start']] = start_date
    each_ratio[config['interval_end']] = end_date

    each_ratio = each_ratio[config['cols_in_opensafely']]

    return each_ratio

def create_source_files_from_nhs_england(config):
    """
    Downloads files from URLs specified in the config dictionary, saves them to a specified directory,
    and extracts any ZIP files found in that directory.

    Args:
        config (dict): A configuration dictionary containing:
            - Keys with 'url' in their name, each mapping to a file URL to download.
            - 'file_path_to_save' (str): Directory path where files will be saved and extracted.

    Raises:
        KeyError: If 'file_path_to_save' is not present in the config.
        requests.exceptions.RequestException: If a download request fails.
        zipfile.BadZipFile: If a ZIP file is corrupted or invalid.

    Side Effects:
        - Downloads files from the specified URLs and saves them to disk.
        - Extracts all ZIP files in the target directory.
    """

    # Need to save the data
    keys_in_config_dict = list(config.keys())
    url_keys = [x for x in keys_in_config_dict if ('url' in x)]

    for each_url_key in url_keys:
        url = config[each_url_key]
        response = requests.get(url)
        filename = config['file_path_to_save'] + os.path.basename(url)
        with open(filename, "wb") as f:
            f.write(response.content)

    zip_files = [f for f in os.listdir(config['file_path_to_save']) if f.endswith('.zip')]

    for each_zip_file in zip_files:
        zip_path = os.path.join(config['file_path_to_save'], each_zip_file)
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(config['file_path_to_save'])