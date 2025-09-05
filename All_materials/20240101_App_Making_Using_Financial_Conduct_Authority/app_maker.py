import streamlit as st
from src.fca_web_scrape import fca_scrape
import bs4
import re

#st.write('Enter institution')
x = st.text_input('Enter institution')

if st.button("Click Me"):

    soup = fca_scrape.get_soup_of_fca_search(x)

    ref_table = fca_scrape.get_dict_of_ordering_firm_listings(soup)
    
    first_firm_link = ref_table.iloc[0]['fca_ref']

    name, phone_number, website = fca_scrape.get_general_info_for_a_profile(first_firm_link)
     
    st.write(f"The name of the firm is `{name}`")
    st.write(f"The wesbite of the firm is `{website}`")
    st.write(f"The phone number is `{phone_number}`")