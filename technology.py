
import requests
from bs4 import BeautifulSoup

def technology():
    def mobileDevices():
        def cNET():
            try:
                url = "https://www.cnet.com/topics/mobile/"
                websiteRequest = requests.get(url, timeout=30)
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    a = 0
                    for i in soup.find("div",{"class":"container"}).find("div",{"class":"row"}).find("div",{"class":"col-8"}).find("section",{"class":"listing"}).find_all('div',attrs={'class':'row asset'}):
                        if a==0:
                            firstNews = i.find("div",{"class":"col-6 assetBody"}).find("a").get("href")
                        elif a==1:
                            secondNews =i.find("div",{"class":"col-6 assetBody"}).find("a").get("href")
                        elif a==2:
                            thirdNews =i.find("div",{"class":"col-6 assetBody"}).find("a").get("href")
                        a=a+1
                    url = "https://www.cnet.com"
                    firstUrl = url + firstNews
                    secondUrl = url + secondNews
                    thirdUrl = url + thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=30)
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            print(newsImage)
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            print(newsTitle)
                            newsContent = ""
                            newsTags = soup.find("div", {"class": "contentWrap"}).find("div",{"class": "container"})
                            a = 0

                            for i in newsTags.find_all('figure', attrs={'section': 'shortcodeImage'}):
                                i.replace_with("")
                            for i in newsTags.find_all('div', attrs={'class': 'newsletter-subscribe-form desktop -inline'}):
                                i.replace_with("")

                            for new in newsTags.find_all('div',{'class':'row'}):
                                if a==3:
                                    for i in new.find("div",{"class":"col-12"}).find("article",{"id":"article-body"}).find("div",{"class":"col-7 article-main-body row"}).find_all('p'):
                                        newsContent = newsContent + " " + i.text
                                a=a+1
                            print(newsContent)

                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")


        def techRadar():
            try:
                url = "https://www.techradar.com/news/phone-and-communications"
                websiteRequest = requests.get(url, timeout=30 , headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    a=0
                    firstNews = soup.find("div",{"id":"content"}).find("section",{"class":"listingResultsWrapper"}).find("div",{"class":"listingResults"}).find("div",{"class":"listingResult small result1"}).find("a").get("href")
                    secondNews = soup.find("div",{"id":"content"}).find("section",{"class":"listingResultsWrapper"}).find("div",{"class":"listingResults"}).find("div",{"class":"listingResult small result2"}).find("a").get("href")
                    thirdNews = soup.find("div",{"id":"content"}).find("section",{"class":"listingResultsWrapper"}).find("div",{"class":"listingResults"}).find("div",{"class":"listingResult small result3"}).find("a").get("href")

                    url = "https://www.techradar.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=30)
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            print(newsImage)
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            print(newsTitle)
                            newsContent = ""
                            newsTags = soup.find("section", {"class": "content-wrapper"}).find("div",{"id": "article-body"})
                            a = 0
                            for i in newsTags.find_all('div', attrs={'class': 'see-more'}):
                                i.replace_with("")

                            for i in newsTags.find_all('a', attrs={'class': 'view-deal button'}):
                                i.replace_with("")

                            for new in newsTags.find_all('p'):
                                newsContent=newsContent+" "+new.get_text()

                            print(newsContent)

                        except:
                            print("Error!"+Exception)

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!"+Exception)











        cNET()
        techRadar()








    mobileDevices()



technology()
