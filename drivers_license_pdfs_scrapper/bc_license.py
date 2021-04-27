import requests
from bs4 import BeautifulSoup
from db_write import dbWrite


def bcLicense(province_name, url):
    pdfLinks = []
    try:
        print("scraping.</br>")
        htmlResponse = requests.get(url).text
        soup = BeautifulSoup(htmlResponse, "lxml")
        anchorTags = soup.find(
            "div", class_="ms-rte-embedcode ms-rte-embedwp").find_all("a", class_="ext-noicon")
        if len(anchorTags) > 0:
            for tag in anchorTags:
                link = tag["href"]
                if ".pdf" in link:
                    pdfLink = link
                    pdfLinks = [pdfLink]
                    break
                else:
                    pdfLink = None
        else:
            print("not found.</br>")
            pdfLink = None
    except:
        print("fail.</br>")
        pdfLink = None

    dbWrite(pdfLinks, province_name, "\w*-*\w*.pdf$")
    print(f"{pdfLinks}</br>")

    # test purpose
    # dbWrite(
    #     ["http://www.icbc.com/driver-licensing/Documents/driver-full.pdf"], province_name, "\w*-*\w*.pdf$")
