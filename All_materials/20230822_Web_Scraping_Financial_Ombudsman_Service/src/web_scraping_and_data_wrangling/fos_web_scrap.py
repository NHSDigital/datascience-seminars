import datetime
import re
import string
from io import BytesIO

import bs4
import gensim
import pandas as pd
import PyPDF2
import requests
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer, WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer, word_tokenize

all_stopwords = stopwords.words("english")
stemmer = SnowballStemmer("english")

# hi
# Test URL for FOS
# BASE_URL = "https://www.financial-ombudsman.org.uk/decisions-case-studies/ombudsman-decisions/search?Keyword=scam&Business={banking_code}&DateFrom=2022-01-01&DateTo=2022-06-01&{upheld_code}&Sort=relevance"
url_link = "https://www.financial-ombudsman.org.uk/decisions-case-studies/ombudsman-decisions/search?Keyword=scam&IndustrySectorID%5B1%5D=1&DateFrom=2023-01-01&DateTo=2023-06-11&IsUpheld%5B1%5D=1&IsUpheld%5B0%5D=0&Sort=relevance"


# You can see that you can use the search within the parameters of the URL


def get_info_as_soup(url_link: str):
    # Getting the request

    res = requests.get(url_link)

    # Getting into soup
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    return soup


def get_list_of_decision(soup):
    # From the soup to get correct info

    li_section = soup.find_all("li")

    decision_list = []

    for each_li in li_section:

        text_on_web = each_li.get_text()

        if "Decision Reference" in text_on_web:

            decision_list = decision_list + [text_on_web.split("\n")]

    return decision_list


def wrangle_each_decision_list(decision_list):

    list_of_machine_readable_decision = []

    for each_decision in decision_list:

        # Wrangle the list
        each_decision = [re.sub(" +", " ", x) for x in each_decision if (x != "")]

        # Getting the info
        ref_number = each_decision[0][19:]
        date_of_decision = datetime.datetime.strptime(each_decision[1], "%d %b %Y")
        bank = each_decision[2]
        outcome = each_decision[5].replace(" ", "")
        descrp = each_decision[8].split(" ", 2)[2][:190]
        pdf_text = getting_pdf_text(ref_number)

        dict_each_decision = {
            "ref": ref_number,
            "date": date_of_decision,
            "scale_of_lost": finding_scale_of_money(pdf_text),
            "bank": bank,
            "outcome": outcome,
            "background": descrp,
            "all_text": pdf_text,
            "CRM": was_CRM_mentioned(pdf_text),
        }

        list_of_machine_readable_decision = list_of_machine_readable_decision + [
            dict_each_decision
        ]

    return list_of_machine_readable_decision


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

    # Getting the number of pages
    out = soup.find_all("div", {"class": "search-results-holder"})[0]
    number_of_pages = int(out.text.split("\n")[-5].split()[-1])

    # Getting the URL
    list_of_urls = [
        url_link + "&Start=" + str(x * 10) for x in range(1, number_of_pages)
    ]
    list_of_urls = [url_link] + list_of_urls

    return list_of_urls, number_of_pages


def get_complete_decision_list(url_link):

    # Getting all the 0th soup
    soup = get_info_as_soup(url_link)

    links_for_all_lists, _ = getting_number_of_links_and_soup(soup, url_link)

    list_of_decisions = []

    for each_url in links_for_all_lists:

        each_soup = get_info_as_soup(each_url)

        decision_list = get_list_of_decision(each_soup)

        list_of_machine_readable_decision = wrangle_each_decision_list(decision_list)

        list_of_decisions = list_of_decisions + list_of_machine_readable_decision

    return list_of_decisions


def getting_pdf_text(ref_complaint):

    # Getting the pdf link
    url_pdf = (
        "https://www.financial-ombudsman.org.uk/decision/" + ref_complaint + ".pdf"
    )

    # request the download of the pdf and getting the text
    response = requests.get(url_pdf)
    my_raw_data = response.content

    all_text = ""

    with BytesIO(my_raw_data) as data:
        read_pdf = PyPDF2.PdfReader(data)

        for page in range(len(read_pdf.pages)):
            each_page_text = read_pdf.pages[page].extract_text()
            all_text = all_text + each_page_text

    return all_text


def getting_numbers_from_string(string_with_numbers):

    numbers_only = [x for x in string_with_numbers if x.isdigit()]
    numbers_only = "".join(numbers_only)

    return numbers_only


def finding_scale_of_money(string_text):

    # Need to separation the stings
    string_splint = string_text.split()

    money_mentions = [x for x in string_splint if "£" in x]
    money_mentions = [getting_numbers_from_string(x) for x in money_mentions]

    multiple_of_lost = [len(x) for x in money_mentions]

    if multiple_of_lost:

        # Need to have a scale format
        string_scale = "10^" + str(max(multiple_of_lost) - 1)
        return string_scale

    else:

        return "10^?"


def was_CRM_mentioned(string_text):

    tokenizer = RegexpTokenizer(r"\w+")

    list_of_strings = tokenizer.tokenize(string_text.lower())

    mentioned_CRM = [x for x in list_of_strings if "crm" in x]

    if mentioned_CRM:

        return True

    else:

        return False


def finding_scale_of_lost_in_complaint(ref_complaint):

    all_text = getting_pdf_text(ref_complaint)

    scale_of_lost = finding_scale_of_money(all_text)

    return scale_of_lost


def is_CRM_used(binary_take):

    if binary_take:
        return "YES"
    else:
        return "NO"


def lemmatize_stemming(text):
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos="v"))


# Tokenize and lemmatize
def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(lemmatize_stemming(token))

    return result


def date_format_as_string_in_tweet(date_info):

    # getting the date
    date_of_compl = date_info.strftime("%m%d%y")

    return date_of_compl


def getting_a_single_tweet_from_complaint(single_series):

    # Need to construct the extract
    full_text_complaint = single_series["all_text"]
    text_without_stopwords = word_tokenize(full_text_complaint)
    text_without_stopwords = [
        word for word in text_without_stopwords if not word in all_stopwords
    ]
    text_without_stopwords = (" ").join(text_without_stopwords)

    # Need to get a 1/4 of the point
    index_start = round(len(text_without_stopwords) / 4)
    text_without_stopwords = text_without_stopwords[index_start:]

    string_construction = (
        date_format_as_string_in_tweet(single_series["date"])
        + "\n"
        + single_series["ref"]
        + "\n"
        + "~£"
        + single_series["scale_of_lost"]
        + "\n"
        + single_series["outcome"]
        + "\n"
        + "CRM?"
        + is_CRM_used(single_series["CRM"])
        + "\n"
        + "..."
        + text_without_stopwords
    )

    # Crop
    string_construction = string_construction[:279]

    return string_construction, text_without_stopwords[:400]


def list_of_summary(list_of_complaints):

    # Convert to pandas
    fos_scam_records = pd.DataFrame.from_dict(list_of_complaints)

    # Adding summary
    fos_scam_records["summary"] = ""

    separator_string = "\n" + "\n" + "--------------------------------" + "\n" + "\n"

    list_of_all_tweets = separator_string

    list_of_strings = []

    for index, each_row in fos_scam_records.iterrows():

        tweet_string, summary_text = getting_a_single_tweet_from_complaint(each_row)

        list_of_all_tweets = list_of_all_tweets + tweet_string + separator_string

        list_of_strings = list_of_strings + [tweet_string]

        fos_scam_records.at[index, "summary"] = summary_text

    # Getting a pandas data frame
    pandas_of_tweets = pd.DataFrame(list_of_strings, columns=["list_of_summary"])

    return list_of_all_tweets, pandas_of_tweets, fos_scam_records


def saving_the_tweets(complete_list_of_decisions, url_link):

    # Getting the save file name
    name_of_file = url_link.translate(str.maketrans("", "", string.punctuation))
    # Crop the start
    name_of_file = name_of_file[75:]

    to_tweet, pandas_of_tweets = list_of_summary(complete_list_of_decisions)

    # Need to remove some uni code characters
    to_tweet = to_tweet.replace("\uf0b7", "")

    # Saving the string to text
    with open(name_of_file + ".txt", "w") as text_file:
        text_file.write(to_tweet)

    # Saving CSV
    pandas_of_tweets = pandas_of_tweets.to_csv(
        name_of_file + ".csv", index=False, encoding="utf-8-sig"
    )

    return


def getting_URL_with_date_range(start_date, end_date, search_term="scam"):

    # Setting up the URL strings
    start_date_sting = start_date.strftime("%Y-%m-%d")
    end_date_sting = end_date.strftime("%Y-%m-%d")

    webscrape_URL = (
        "https://www.financial-ombudsman.org.uk/decisions-case-studies/ombudsman-decisions/search?Keyword="
        + search_term
        + "&DateFrom="
        + start_date_sting
        + "&DateTo="
        + end_date_sting
        + "&Sort=relevance"
    )

    return webscrape_URL


def run():
    """
    Main orchestration function

    :return: number of search results
    """
