from bs4 import BeautifulSoup
import requests

from db_write import dbWrite, link_types


def bcLicense(province_name, url):
    pdfLinksDict = {}  # {"pdfTitle": "pdfLink"}
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
                    pdfTitle = tag.text
                    pdfLink = link
                    pdfLinksDict = [pdfLink]
                    break
                else:
                    pdfLink = None
        else:
            print("not found.</br>")
            pdfLink = None
    except:
        print("fail.</br>")
        pdfLink = None

    dbWrite(pdfLinksDict, province_name, "[\w+\-*]+.pdf")
    print(f"{pdfLinksDict}</br></br>")

    # test purpose
    # dbWrite(
    #     ["http://www.icbc.com/driver-licensing/Documents/driver-full.pdf"], province_name, "[\w+\-*]+.pdf")
