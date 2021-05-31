from bs4 import BeautifulSoup
import requests

from db_write import dbWrite, link_types
from base import headers


def prScrapper(topic_name, url):
    webLinksDict = {}  # {"webTitle": "webLink"}{}  # {"webTitle": "webLink"}
    try:
        print("</br>scraping.</br>")
        htmlResponse = requests.get(url, headers=headers).text
        soup = BeautifulSoup(htmlResponse, "lxml")
        anchorTags = soup.find("div", class_="wb-eqht row").find_all("a")
        if len(anchorTags) > 0:
            for aTag in anchorTags:
                webTitle = aTag.text.capitalize()
                link = aTag["href"]
                if "http" in link:
                    webLink = link
                else:
                    webLink = "https://www.canada.ca" + aTag["href"]
                webLinksDict[webTitle] = webLink
    except:
        print("fail.</br>")

    print(f"{webLinksDict}</br></br>")
    dbWrite(webLinksDict, None, 1, link_types[1])
