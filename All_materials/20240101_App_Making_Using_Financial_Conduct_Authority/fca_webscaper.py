from src.fca_web_scrape import fca_scrape
import bs4
import re

FIRM_REF_NUMBER = 'firm_ref_number'
FIRM_FCA_LINK = 'fca_ref'

soup = fca_scrape.get_soup_of_fca_search('Leeds Building society')

ref_table = fca_scrape.get_dict_of_ordering_firm_listings(soup)

selected_link = ref_table.iloc[0][FIRM_FCA_LINK]

#%%

soup_data_for_firm = fca_scrape.get_soup_without_cookie_notice(selected_link)

#%% 

def get_website_from_fca_profile(soup):
    
    list_if_removed_extension = ['.fca.', '.gov.', '.bankofengland.']
    
    element_list = soup.find_all('a', {'name':'false'}, href=True)
    
    websites = [x['href'] for x in element_list if all(each_ext not in x['href'] for each_ext in list_if_removed_extension)]
    
    return websites

#%%
text_analysis = soup_data_for_firm.prettify()

#element_list = soup_data_for_firm.find_all('div',{'class':'slds-col slds-size_1-of-1 slds-medium-size_6-of-12 slds-p-around_none slds-p-right_small'})

#element_list = soup_data_for_firm.find_all('p', {'aria-hidden':'true'})

element_list = soup_data_for_firm.find_all('a', {'name':'false'}, href=True)

list_if_removed_extension = ['.fca.', '.gov.', '.bankofengland.']

tmp = [x['href'] for x in element_list if all(each_ext not in x['href'] for each_ext in list_if_removed_extension)]

for each_item in tmp:
    print(each_item)