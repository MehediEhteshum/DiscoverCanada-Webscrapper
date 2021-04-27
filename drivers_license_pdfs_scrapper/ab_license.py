from db_write import dbWrite
from bs4 import BeautifulSoup
import requests


def abLicense(province_name, url):
    # pdfLinks = []
    # try:
    #     print("scraping.</br>")
    #     htmlResponse = requests.get(url).text
    #     soup = BeautifulSoup(htmlResponse, "lxml")
    #     anchorTags = soup.find("div", id="goa-grid25734").findAll("a")
    #     if len(anchorTags) > 0:
    #         for aTag in anchorTags:
    #             aTagUrl = aTag["href"]
    #             res = requests.get(aTagUrl).text
    #             resSoup = BeautifulSoup(res, "lxml")
    #             pdfLink = resSoup.find(
    #                 "section", id="dataset-resources").find("a")["href"]
    #             pdfLinks.append(pdfLink)
    # except:
    #     print("fail.</br>")
    #     pdfLink = None

    # dbWrite(pdfLinks, province_name, "[\w+\-*]+.pdf")
    # print(f"{pdfLinks}</br></br>")

    # test purpose
    dbWrite(
        ['https://open.alberta.ca/dataset/485a5480-45b7-4416-a06f-38ab2191a9fd/resource/cd3aa450-04ef-4729-b0e9-81e387514ae2/download/trans-commercial-drivers-guide-trucks-buses-emergency-responders-taxis-2020-07.pdf', 'https://open.alberta.ca/dataset/c2e7d260-292c-4f5c-b7ad-ee5309c232d0/resource/4c05aa19-cb40-4be3-a76e-4fb642a833b2/download/goa-riders-guide-07-2019.pdf', 'https://open.alberta.ca/dataset/ddca813d-5463-4daa-afc9-093807a1bb6a/resource/e72fcd84-c5e9-4241-b907-4b1ef00dbce7/download/trans-drivers-guide-cars-light-trucks-2021-01.pdf'], province_name, "[\w+\-*]+.pdf")
