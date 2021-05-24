import requests
from bs4 import BeautifulSoup

from db_write import dbWrite, link_types
from base import headers


def nlLicense(province_name, url):
    pdfLinksDict = {}  # {"pdfTitle": "pdfLink"}
    try:
        print("</br>scraping.</br>")
        htmlResponse = requests.get(url, headers=headers).text
        soup = BeautifulSoup(htmlResponse, "lxml")
        anchorTags = soup.find(
            "article")
    except:
        print("fail.</br>")
        pdfLink = None
