import pandas as pd
import os
import bs4
import requests
from io import BytesIO
import boto3
import PyPDF2
import logging
from nltk.tokenize import RegexpTokenizer
import re
from datetime import datetime
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# These are pre-determined for now but can be overwritten
BANKING_CODES = {
    "Barclays": 0,
    "Natwest": 23,
    "Nationwide": 4
}

#hi
# Test URL for FOS
#BASE_URL = "https://www.financial-ombudsman.org.uk/decisions-case-studies/ombudsman-decisions/search?Keyword=scam&Business={banking_code}&DateFrom=2022-01-01&DateTo=2022-06-01&{upheld_code}&Sort=relevance"
url_link = 'https://www.financial-ombudsman.org.uk/decisions-case-studies/ombudsman-decisions/search?Keyword=scam&IndustrySectorID%5B1%5D=1&DateFrom=2023-01-01&DateTo=2023-06-11&IsUpheld%5B1%5D=1&IsUpheld%5B0%5D=0&Sort=relevance'


# You can see that you can use the search within the parameters of the URL


def determine_banking_codes(use_specified: bool = True, additional_key_values: dict = {}):
    """
    Function that can scrap the FOS website for the banking codes and keys
    
    :param use_specified: Bool, use default, pre-specified banking code
    :param additional_key_values: dict, if we use pre-specified code, we can add extra key and values
    :return: dict, key and value of bank and banking code
    """


    if use_specified:
        banking_codes = BANKING_CODES
        if len(additional_key_values) > 0:
            for key, value in additional_key_values:
                banking_codes[key] = value
    else:
        # Need to add a webscraping function tograb from FOS website
        print("Need to implement")


    return banking_codes


def upheld_vs_not_upheld(banking_codes: dict) -> pd.DataFrame:
    """
    Function to grab the upheld vs not upheld cases

    :param banking_codes: dict, codes of the banks
    :return: pd.DataFrame
    """
    
    if len(banking_codes) == 0:
        logger.error("No banking codes")
        raise


    search_results = {}


    for key, value in banking_codes.items():
        logger.info("Bank: %s - Start", key)
        search_results[key] = {}
        search_results[key]["upheld"] = obtain_number_results(url=BASE_URL, banking_code=str(value), is_upheld=True)
        search_results[key]["not_upheld"] = obtain_number_results(url=BASE_URL, banking_code=str(value), is_upheld=False)
        search_results[key]["proportion"] = search_results[key]["upheld"]/(search_results[key]["not_upheld"] + search_results[key]["upheld"])
        logger.info("Bank: %s - End", key)


    df = pd.DataFrame(search_results).T


    return df


def get_info_as_soup(url_link: str):
    #Getting the request
    
    res = requests.get(url_link)
    
    #Getting into soup
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    
    return soup


def get_list_of_deision(soup):
    #From the soup to get coorect info
    
    li_section = soup.find_all('li')
    
    desison_list = []

    for each_li in li_section:
        
        text_on_web = each_li.get_text()
        
        if 'Decision Reference' in text_on_web:
            
            desison_list = desison_list + [text_on_web.split('\n')]
            
    return desison_list

def wrangle_each_deision_list(desison_list):
    
    list_of_machine_readable_deision = []
    
    for each_deison in desison_list:
        
        #Wrangle the list
        each_deison = [re.sub(' +', ' ', x) for x in each_deison if
                       (x != '')]
        
        #Getting the info
        ref_number = each_deison[0][19:]
        date_of_desision = datetime.strptime(each_deison[1], '%d %b %Y')
        bank = each_deison[2]
        outcome = each_deison[5].replace(" ", "")
        descrp = each_deison[8].split(' ', 2)[2][:190]
        pdf_text = getting_pdf_text(ref_number)
        
        dict_each_deision = {
            'ref':ref_number,
            'date':date_of_desision,
            'scale_of_lost': finding_scale_of_money(pdf_text),
            'bank':bank,
            'outcome':outcome,
            'background':descrp,
            'all_text': pdf_text,
            'CRM':was_CRM_mentioned(pdf_text)
            }
        
        list_of_machine_readable_deision = list_of_machine_readable_deision + [dict_each_deision]
        
    return list_of_machine_readable_deision

def getting_number_of_links_and_soup(soup, url_link):
    """
    Getting the list from soup

    Parameters
    ----------
    soup 
    
    url

    Returns
    -------
    number_of_pages
        Number of pages
    list_of_urls
        The list the URLs

    """
    
    #Getting the number of pages
    out = soup.find_all("div", {"class": "search-results-holder"})[0]
    number_of_pages = int(out.text.split("\n")[-5].split()[-1])
    
    #Getting the URL
    list_of_urls = [url_link + '&Start=' + str(x*10) for x in range(1,number_of_pages)]
    list_of_urls = [url_link] + list_of_urls
    
    return list_of_urls, number_of_pages

def get_complete_desision_list(url_link):
    
    #Getting all the 0th soup
    soup = get_info_as_soup(url_link)
    
    links_for_all_lists, _ = getting_number_of_links_and_soup(soup, url_link)
    
    list_of_deisions = []
    
    for each_url in links_for_all_lists:
        
        each_soup = get_info_as_soup(each_url)
        
        desison_list = get_list_of_deision(each_soup)

        list_of_machine_readable_deision = wrangle_each_deision_list(desison_list)
        
        list_of_deisions = list_of_deisions + list_of_machine_readable_deision
        print(list_of_machine_readable_deision)
        
    return list_of_deisions

def getting_pdf_text(ref_complaint):
    
    #Getting the pdf link
    url_pdf = 'https://www.financial-ombudsman.org.uk/decision/' + ref_complaint + '.pdf'
    
    #request the download of the pdf and getting the text
    response = requests.get(url_pdf)
    my_raw_data = response.content
    
    all_text = ''
    
    with BytesIO(my_raw_data) as data:
        read_pdf = PyPDF2.PdfReader(data)

        for page in range(len(read_pdf.pages)):
            each_page_text = read_pdf.pages[page].extract_text()
            all_text = all_text + each_page_text
            
    return all_text

def getting_numbers_from_string(string_with_numbers):
    
    numbers_only = [x for x in string_with_numbers if x.isdigit()]
    numbers_only = ''.join(numbers_only)
    
    return numbers_only

def finding_scale_of_money(string_text):
    
    #Need to seperation the stings
    string_splint = string_text.split()
    
    money_mentions = [x for x in string_splint if '£' in x]
    money_mentions = [getting_numbers_from_string(x) for x in money_mentions]
    
    multple_of_lost = [len(x) for x in money_mentions]
    
    if multple_of_lost:
        
        #Need to have a scale format
        string_scale = '10^' +  str(max(multple_of_lost)-1)
        return string_scale
    
    else:
        
        return '10^?'
    
def was_CRM_mentioned(string_text):
    
    tokenizer = RegexpTokenizer(r'\w+')
    
    list_of_strings = tokenizer.tokenize(string_text.lower())
    
    mentioned_CRM = [x for x in list_of_strings if 'crm' in x]
    
    if mentioned_CRM:
        
        return True
    
    else:
        
        return False
    
    
def finding_scale_of_lost_in_complaint(ref_complaint):
    
    all_text = getting_pdf_text(ref_complaint)
    
    scale_of_lost = finding_scale_of_money(all_text)
    
    return scale_of_lost
    
    
def run():
    """
    Main orchestration function

    :return: number of search results
    """
    
    soup = get_info_as_soup(url_link)
    
    desison_list = get_list_of_deision(soup)
    
    list_of_machine_readable_deision = wrangle_each_deision_list(desison_list)


#%%

url_link = 'https://www.financial-ombudsman.org.uk/decisions-case-studies/ombudsman-decisions/search?Keyword=scam&IndustrySectorID%5B1%5D=1&DateFrom=2023-06-01&DateTo=2023-06-05&IsUpheld%5B1%5D=1&IsUpheld%5B0%5D=0&Sort=relevance'
complete_list = get_complete_desision_list(url_link)
