import requests
from bs4 import BeautifulSoup


def bc_license(url):
    try:
        htmlResponse = requests.get(url).text
        soup = BeautifulSoup(htmlResponse, "lxml")
        anchorTags = soup.find(
            "div", class_="ms-rte-embedcode ms-rte-embedwp").find_all("a", class_="ext-noicon")
        if len(anchorTags) > 0:
            for tag in anchorTags:
                link = tag["href"]
                if ".pdf" in link:
                    pdfLink = link
                    break
                else:
                    pdfLink = None
        else:
            pdfLink = None
    except:
        pdfLink = None

    print(pdfLink)
