import pandas as pd
import requests
from config import config
import os


#Downloading the file
url = config['SNOMED_code_usage_2023_24']
response = requests.get(url)
filename = config['file_path_to_save'] + os.path.basename(url)

with open(filename, "wb") as f:
    f.write(response.content)

#Getting the data
table = pd.read_excel(filename)

adhdrem_codelist = pd.read_csv(config['remission_code_path'])
adhdrem_codelist = adhdrem_codelist[config['code']].tolist()

remission_table = table[table[config['SNOMED_Concept_ID']].isin(adhdrem_codelist)]
remission_table = remission_table[[
    config['SNOMED_Concept_ID'],
    config['Description'],
    config['Usage'],
    ]]

# Need to read in the README.md text file
readme_file_path = config['readme_path']
with open(readme_file_path,"r") as f:
    readme_string = f.read()

readme_selected_text = readme_string.split(config['anchor_in_readme'], 1)[0] + config['anchor_in_readme']

table_to_markdown = remission_table.to_markdown(index=False)
output_string = readme_selected_text + "\n\n" + table_to_markdown

with open(config['readme_path'], "w") as f:
    f.write(output_string)