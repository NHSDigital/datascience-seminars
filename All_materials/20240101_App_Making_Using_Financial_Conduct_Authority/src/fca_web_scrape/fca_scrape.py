from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import bs4
import time
import urllib.parse
import re

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


def get_reference_number(soup):
    
    element_list = soup.find_all('div', {'class':'text-medium slds-text-color_weak'})
    
    list_of_org_ref_number = [x.get_text() for x in element_list]
    list_of_org_ref_number = [re.search(r'\d+', x).group() for x in  list_of_org_ref_number]
    
    return list_of_org_ref_number