from src.fca_web_scrape import fca_scrape
import bs4
import re

FIRM_REF_NUMBER = 'firm_ref_number'
FIRM_FCA_LINK = 'fca_ref'

#%% 
soup = fca_scrape.get_soup_of_fca_search('Leeds Building society')

ref_table = fca_scrape.get_dict_of_ordering_firm_listings(soup)


#%%

first_firm_link = ref_table.iloc[0]['fca_ref']

name, phone_number, website = fca_scrape.get_general_info_for_a_profile(first_firm_link)
    
#%% 

selected_link = ref_table.iloc[0][FIRM_FCA_LINK]

soup_data_for_firm = fca_scrape.get_soup_without_cookie_notice(selected_link)

resulting_name , resulting_number, resulting_website = fca_scrape.get_general_info_for_a_profile_via_soup(soup_data_for_firm)

