
import requests
from bs4 import BeautifulSoup

def technology():
    def mobileDevices():
        def phoneArena():
            try:
                url = "https://www.phonearena.com/news"
                hdr={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 OPR/76.0.4017.123'}
                websiteRequest = requests.get(url, timeout=30,headers=hdr)

                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    a=0
                    for i in soup.find("div",{"class":"layout__spot_belowHeader"}).find_all('div',attrs={'class':'widget widget-tileCard news'}):
                        if a==0:
                            firstNews=i.find("a").get("href")
                        elif a==1:
                            secondNews=i.find("a").get("href")
                        elif a==2:
                            thirdNews=i.find("a").get("href")
                        a=a+1


                    url = "https://www.phonearena.com/news"
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
                            try:
                                newsContent=soup.find("div",{"class": "main"}).find("div",{"id": "content"}).find("div",{"id": "article"}).find("div",{"class": "parser-body"})
                                for i in newsContent.find_all('div',attrs={'class':'full-width-element-xs s_media main-image-group full-width-element'}):
                                    i.replace_with("")


                                print(newsContent.text)

                            except:
                                print("Error!")
                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)
            except:
                print("Error!")




        phoneArena()








    mobileDevices()



technology()
