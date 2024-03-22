from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import bs4
import time
import urllib.parse
import re
import pandas as pd


FIRM_REF_NUMBER = 'firm_ref_number'
FIRM_FCA_LINK = 'fca_ref'

def get_soup_of_fca_search(search_term):
    
    #Need to convert to URL
    search_term_url_percentage = urllib.parse.quote(search_term, safe='')
    
    driver = webdriver.Firefox()
    
    driver.get('https://register.fca.org.uk/s/search?q=' + 
               search_term_url_percentage +
               '&type=Companies')
    
    time.sleep(10)
    
    element = driver.find_element(By.XPATH, '//button[@value="no"]')
    driver.execute_script("arguments[0].click();", element)
    
    html_data = driver.page_source
    
    driver.close()
    
    soup = bs4.BeautifulSoup(html_data,'html.parser')
    
    return soup

def get_soup_without_cookie_notice(url_link):
    
    driver = webdriver.Firefox()
    
    driver.get(url_link)
    
    time.sleep(10)
    
    element = driver.find_element(By.XPATH, '//button[@value="no"]')
    driver.execute_script("arguments[0].click();", element)
    
    html_data = driver.page_source
    
    driver.close()
    
    soup = bs4.BeautifulSoup(html_data,'html.parser')
    
    return soup
    

def get_ref_links_from_soup(soup):
    
    element_list = soup.find_all('a', href=True)
    list_of_ref = [x['href'] for x in  element_list if '/s/firm?id=' in x['href']]
    
    return list_of_ref

def get_reference_number(soup):
    
    element_list = soup.find_all('div', {'class':'text-medium slds-text-color_weak'})
    
    list_of_org_ref_number = [x.get_text() for x in element_list]
    list_of_org_ref_number = [re.search(r'\d+', x).group() for x in  list_of_org_ref_number]
    
    return list_of_org_ref_number

def get_dict_of_ordering_firm_listings(soup):
    
    list_of_ref_links = get_ref_links_from_soup(soup)
    list_of_org_ref_number = get_reference_number(soup)
    
    dicts_of_findings = {FIRM_REF_NUMBER:list_of_org_ref_number,
                         FIRM_FCA_LINK:list_of_ref_links}
    
    pandas_ref_table = pd.DataFrame(dicts_of_findings)
    
    return pandas_ref_table

def get_name_from_fca_profile(soup):
    
    element_list = soup.find_all('h1', {'class':'text-display-2 text--bold'})
    
    #Getting the name
    name_of_firm = element_list[0].get_text()
    
    return name_of_firm

def get_phone_number_from_fca_profile(soup):
    
    element_list = soup.find_all('p', {'aria-hidden':'true'})
    
    phone_number = element_list[0].get_text()
    
    return phone_number
