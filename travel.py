
from bs4 import BeautifulSoup
import requests

def travel():
    def rvNews():
        def rvdealerNews():
            try:
                url = "http://rvldealernews.com"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find_all("div",{"class":"td-block-span12"})[0].find("a").get("href")
                    secondNews = soup.find_all("div",{"class":"td-block-span12"})[1].find("a").get("href")
                    thirdNews = soup.find_all("div",{"class":"td-block-span12"})[2].find("a").get("href")

                    url = "http://rvldealernews.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            print(newsImage)
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            print(newsTitle)
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"role": "main"}).find("div", {"class": "td-post-content"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('aside'):
                                    i.replace_with("")
                                for i in newsTags.find_all('h2'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('table'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div'):
                                    i.replace_with("")
                                for i in newsTags.find_all('blockquote'):
                                    i.replace_with("")
                                for i in newsTags.find_all('em'):
                                    i.replace_with("")
                                for i in newsTags.find_all('section'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                                print(newsContent.strip())
                            except:
                                print("Error!")


                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")








        def motorHome():
            try:
                url = "https://www.motorhome.com"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"class": "td-big-grid-wrapper"}).find_all("div",{"class":"td-module-thumb"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"class": "td-big-grid-wrapper"}).find_all("div",{"class":"td-module-thumb"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"class": "td-big-grid-wrapper"}).find_all("div",{"class":"td-module-thumb"})[2].find("a").get("href")

                    url = "https://www.motorhome.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            print(newsImage)
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            print(newsTitle)
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"role": "main"}).find("div", {"class": "td-post-content"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('aside'):
                                    i.replace_with("")
                                for i in newsTags.find_all('h2'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('table'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div'):
                                    i.replace_with("")
                                for i in newsTags.find_all('blockquote'):
                                    i.replace_with("")
                                for i in newsTags.find_all('em'):
                                    i.replace_with("")
                                for i in newsTags.find_all('section'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                                print(newsContent.strip())
                            except:
                                print("Error!")


                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")







        def trailerLife():
            try:
                url = "https://www.trailerlife.com"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"class": "td-big-grid-wrapper"}).find_all("div",{"class":"td-module-thumb"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"class": "td-big-grid-wrapper"}).find_all("div",{"class":"td-module-thumb"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"class": "td-big-grid-wrapper"}).find_all("div",{"class":"td-module-thumb"})[2].find("a").get("href")

                    url = "https://www.trailerlife.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            print(newsImage)
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            print(newsTitle)
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"role": "main"}).find("div", {"class": "td-post-content"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('aside'):
                                    i.replace_with("")
                                for i in newsTags.find_all('h2'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('table'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div'):
                                    i.replace_with("")
                                for i in newsTags.find_all('blockquote'):
                                    i.replace_with("")
                                for i in newsTags.find_all('em'):
                                    i.replace_with("")
                                for i in newsTags.find_all('section'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                                print(newsContent.strip())
                            except:
                                print("Error!")


                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")










        def rvPro():
            try:
                url = "https://rv-pro.com/news/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("ul", {"class": "posts-items"}).find_all("li",{"class":"post-item"})[0].find("a").get("href")
                    secondNews = soup.find("ul", {"class": "posts-items"}).find_all("li",{"class":"post-item"})[1].find("a").get("href")
                    thirdNews = soup.find("ul", {"class": "posts-items"}).find_all("li",{"class":"post-item"})[2].find("a").get("href")

                    url = "https://rv-pro.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            print(newsImage)
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            print(newsTitle)
                            newsContent = ""
                            try:
                                newsTags = soup.find("article", {"id": "the-post"}).find("div", {"class": "entry-content entry clearfix"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('aside'):
                                    i.replace_with("")
                                for i in newsTags.find_all('h2'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('table'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div'):
                                    i.replace_with("")
                                for i in newsTags.find_all('blockquote'):
                                    i.replace_with("")
                                for i in newsTags.find_all('em'):
                                    i.replace_with("")
                                for i in newsTags.find_all('section'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                                print(newsContent.strip())
                            except:
                                print("Error!")


                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")





        def rvNews():
            try:
                url = "https://www.rvnews.com/category/news/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"class": "elementor-posts-container"}).find_all("article",{"class":"elementor-post"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"class": "elementor-posts-container"}).find_all("article",{"class":"elementor-post"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"class": "elementor-posts-container"}).find_all("article",{"class":"elementor-post"})[2].find("a").get("href")

                    url = "https://www.rvnews.com/category/news/"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            print(newsImage)
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            print(newsTitle)
                            newsContent = ""
                            try:

                                newsTags = soup.find("div", {"data-widget_type": "theme-post-content.default"}).find("div", {"class": "elementor-widget-container"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('aside'):
                                    i.replace_with("")
                                for i in newsTags.find_all('h2'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('table'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div'):
                                    i.replace_with("")
                                for i in newsTags.find_all('blockquote'):
                                    i.replace_with("")
                                for i in newsTags.find_all('em'):
                                    i.replace_with("")
                                for i in newsTags.find_all('section'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                                print(newsContent.strip())
                            except:
                                print("Error!")


                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")







        rvdealerNews()
        motorHome()
        trailerLife()
        rvPro()
        rvNews()







    def airTravel():
        def bbcAirTravel():
            try:
                url = "https://www.bbc.com/news/topics/crz4004j5zet/air-travel"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"id": "lx-stream"}).find_all("li",{"class":"lx-stream__post-container"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"id": "lx-stream"}).find_all("li",{"class":"lx-stream__post-container"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"id": "lx-stream"}).find_all("li",{"class":"lx-stream__post-container"})[2].find("a").get("href")

                    url = "https://www.bbc.com"
                    firstUrl = url+firstNews
                    secondUrl = url+secondNews
                    thirdUrl = url+thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            print(newsImage)
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            print(newsTitle)
                            newsContent = ""
                            try:
                                newsTags = soup.find("article", {"class": "ssrcss-1072xwf-ArticleWrapper"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('aside'):
                                    i.replace_with("")
                                for i in newsTags.find_all('h2'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('table'):
                                    i.replace_with("")
                                for i in newsTags.find_all('blockquote'):
                                    i.replace_with("")
                                for i in newsTags.find_all('em'):
                                    i.replace_with("")
                                for i in newsTags.find_all('section'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all("div",attrs={"data-component":"text-block"}):
                                    for a in x.find_all("p"):
                                        newsContent = newsContent + " " + a.get_text().strip()
                                print(newsContent.strip())
                            except:
                                try:
                                    newsTags = soup.find("div", {"id": "story-content"}).find("div", {"class": "body-content"})
                                    for i in newsTags.find_all('img'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('iframe'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('aside'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('h2'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('figure'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('table'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('blockquote'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('em'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('div'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('section'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('script'):
                                        i.replace_with("")
                                    for x in newsTags.find_all("p"):
                                        newsContent = newsContent + " " + x.get_text().strip()
                                    print(newsContent.strip())
                                except:
                                    print("Error!")


                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")








        def independentAirTravel():
            try:
                url = "https://www.independent.co.uk/topic/air-travel"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"id": "sectionContent"}).find_all("div",{"class":"content"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"id": "sectionContent"}).find_all("div",{"class":"content"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"id": "sectionContent"}).find_all("div",{"class":"content"})[2].find("a").get("href")

                    url = "https://www.independent.co.uk"
                    firstUrl = url+firstNews
                    secondUrl = url+secondNews
                    thirdUrl = url+thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            print(newsImage)
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            print(newsTitle)
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"id": "main"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('aside'):
                                    i.replace_with("")
                                for i in newsTags.find_all('h2'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('table'):
                                    i.replace_with("")
                                for i in newsTags.find_all('blockquote'):
                                    i.replace_with("")
                                for i in newsTags.find_all('em'):
                                    i.replace_with("")
                                for i in newsTags.find_all('section'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                                print(newsContent.strip())
                            except:
                                print("Error!")


                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")





        def travelPulseAirTravel():
            try:
                url = "https://www.travelpulse.com/news/airlines"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"id": "all_news"}).find("ul", {"class": "clear"}).find_all("li")[0].find("a").get("href")
                    secondNews = soup.find("div", {"id": "all_news"}).find("ul", {"class": "clear"}).find_all("li")[1].find("a").get("href")
                    thirdNews = soup.find("div", {"id": "all_news"}).find("ul", {"class": "clear"}).find_all("li")[2].find("a").get("href")

                    url = "https://www.travelpulse.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            print(newsImage)
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            print(newsTitle)
                            newsContent = ""
                            try:
                                newsTags = soup.find("article", {"class": "news detail"}).find("div", {"class": "content aqua_links clear"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('aside'):
                                    i.replace_with("")
                                for i in newsTags.find_all('h2'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('table'):
                                    i.replace_with("")
                                for i in newsTags.find_all('blockquote'):
                                    i.replace_with("")
                                for i in newsTags.find_all('em'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div'):
                                    i.replace_with("")
                                for i in newsTags.find_all('section'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                                print(newsContent.strip())
                            except:
                                print("Error!")


                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")






        def ndtvAirTravel():
            try:
                url = "https://www.ndtv.com/topic/air-travel"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"id": "news_list"}).find("ul").find_all("li")[0].find("a").get("href")
                    secondNews = soup.find("div", {"id": "news_list"}).find("ul").find_all("li")[1].find("a").get("href")
                    thirdNews = soup.find("div", {"id": "news_list"}).find("ul").find_all("li")[2].find("a").get("href")

                    url = "https://www.ndtv.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            print(newsImage)
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            print(newsTitle)
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"itemprop": "articleBody"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('aside'):
                                    i.replace_with("")
                                for i in newsTags.find_all('h2'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('table'):
                                    i.replace_with("")
                                for i in newsTags.find_all('blockquote'):
                                    i.replace_with("")
                                for i in newsTags.find_all('em'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div'):
                                    i.replace_with("")
                                for i in newsTags.find_all('section'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                                print(newsContent.strip())
                            except:
                                print("Error!")


                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")




        bbcAirTravel()
        independentAirTravel()
        travelPulseAirTravel()
        ndtvAirTravel()









    def hotelNews():
        def breakingTravelNewsHotel():
            try:
                url = "https://www.breakingtravelnews.com/news/category/hotel/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"class": "widget-content clearfix"}).find_all("header",{"class":"title"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"class": "widget-content clearfix"}).find_all("header",{"class":"title"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"class": "widget-content clearfix"}).find_all("header",{"class":"title"})[2].find("a").get("href")

                    url = "https://www.breakingtravelnews.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            print(newsImage)
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            print(newsTitle)
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"class": "post-entry"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('aside'):
                                    i.replace_with("")
                                for i in newsTags.find_all('h2'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('table'):
                                    i.replace_with("")
                                for i in newsTags.find_all('blockquote'):
                                    i.replace_with("")
                                for i in newsTags.find_all('em'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div'):
                                    i.replace_with("")
                                for i in newsTags.find_all('section'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                                print(newsContent.strip())
                            except:
                                print("Error!")


                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")









        def travelWeeklyHotel():
            try:
                url = "https://www.travelweekly.com/Travel-News/Hotel-News/Articles"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"class": "featured featured-list"}).find_all("div",{"class":"feature"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"class": "featured featured-list"}).find_all("div",{"class":"feature"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"class": "featured featured-list"}).find_all("div",{"class":"feature"})[2].find("a").get("href")

                    url = "https://www.travelweekly.com"
                    firstUrl = url+firstNews
                    secondUrl = url+secondNews
                    thirdUrl = url+thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            print(newsImage)
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            print(newsTitle)
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"itemprop": "articleBody"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('aside'):
                                    i.replace_with("")
                                for i in newsTags.find_all('h2'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('table'):
                                    i.replace_with("")
                                for i in newsTags.find_all('blockquote'):
                                    i.replace_with("")
                                for i in newsTags.find_all('em'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div'):
                                    i.replace_with("")
                                for i in newsTags.find_all('section'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                                print(newsContent.strip())
                            except:
                                print("Error!")


                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")










        def skiftHotel():
            try:
                url = "https://skift.com/rooms/hotels/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"id": "archive-stories"}).find_all("div",{"class":"story-wrap"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"id": "archive-stories"}).find_all("div",{"class":"story-wrap"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"id": "archive-stories"}).find_all("div",{"class":"story-wrap"})[2].find("a").get("href")

                    url = "https://skift.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            print(newsImage)
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            print(newsTitle)
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"class": "post-copy"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('aside'):
                                    i.replace_with("")
                                for i in newsTags.find_all('h2'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('table'):
                                    i.replace_with("")
                                for i in newsTags.find_all('blockquote'):
                                    i.replace_with("")
                                for i in newsTags.find_all('em'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div'):
                                    i.replace_with("")
                                for i in newsTags.find_all('section'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                                print(newsContent.strip())
                            except:
                                try:
                                    newsTags = soup.find("div", {"class": "take-copy"})
                                    for i in newsTags.find_all('img'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('iframe'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('aside'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('h2'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('figure'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('table'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('blockquote'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('em'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('div'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('section'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('script'):
                                        i.replace_with("")
                                    for x in newsTags.find_all("p"):
                                        newsContent = newsContent + " " + x.get_text().strip()
                                    print(newsContent.strip())
                                except:
                                    print("Error!")


                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")












        def topHotelNews():
            try:
                url = "https://tophotel.news"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find_all("article",{"class":"brbl-post-tile-inner"})[0].find("a").get("href")
                    secondNews = soup.find_all("article",{"class":"brbl-post-tile-inner"})[1].find("a").get("href")
                    thirdNews = soup.find_all("article",{"class":"brbl-post-tile-inner"})[2].find("a").get("href")

                    url = "https://tophotel.news"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            print(newsImage)
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            print(newsTitle)
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"class": "et_pb_module et_pb_text et_pb_text_0 et_pb_text_align_left et_pb_bg_layout_light"}).find("div", {"class": "et_pb_text_inner"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('aside'):
                                    i.replace_with("")
                                for i in newsTags.find_all('h2'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('table'):
                                    i.replace_with("")
                                for i in newsTags.find_all('blockquote'):
                                    i.replace_with("")
                                for i in newsTags.find_all('em'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div'):
                                    i.replace_with("")
                                for i in newsTags.find_all('section'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                                print(newsContent.strip())
                            except:
                                print("Error!")


                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")










        def travelPulseHotelTravel():
            try:
                url = "https://www.travelpulse.com/news/hotels-and-resorts"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"id": "all_news"}).find("ul", {"class": "clear"}).find_all("li")[0].find("a").get("href")
                    secondNews = soup.find("div", {"id": "all_news"}).find("ul", {"class": "clear"}).find_all("li")[1].find("a").get("href")
                    thirdNews = soup.find("div", {"id": "all_news"}).find("ul", {"class": "clear"}).find_all("li")[2].find("a").get("href")

                    url = "https://www.travelpulse.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            print(newsImage)
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            print(newsTitle)
                            newsContent = ""
                            try:
                                newsTags = soup.find("article", {"class": "news detail"}).find("div", {"class": "content aqua_links clear"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('aside'):
                                    i.replace_with("")
                                for i in newsTags.find_all('h2'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('table'):
                                    i.replace_with("")
                                for i in newsTags.find_all('blockquote'):
                                    i.replace_with("")
                                for i in newsTags.find_all('em'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div'):
                                    i.replace_with("")
                                for i in newsTags.find_all('section'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                                print(newsContent.strip())
                            except:
                                print("Error!")


                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")





        breakingTravelNewsHotel()
        travelWeeklyHotel()
        skiftHotel()
        topHotelNews()
        travelPulseHotelTravel()







    def foodBlogs():
        def bucketListJourney():
            try:
                url = "https://bucketlistjourney.net/tag/food-drink/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"id": "posts-container"}).find_all("h2",{"class":"entry-title"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"id": "posts-container"}).find_all("h2",{"class":"entry-title"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"id": "posts-container"}).find_all("h2",{"class":"entry-title"})[2].find("a").get("href")

                    url = "https://bucketlistjourney.net"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            print(newsImage)
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            print(newsTitle)
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"class": "fusion-text fusion-text-1"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('aside'):
                                    i.replace_with("")
                                for i in newsTags.find_all('h2'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('table'):
                                    i.replace_with("")
                                for i in newsTags.find_all('hr'):
                                    i.replace_with("")
                                for i in newsTags.find_all('blockquote'):
                                    i.replace_with("")
                                for i in newsTags.find_all('em'):
                                    i.replace_with("")
                                for i in newsTags.find_all('section'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all():
                                    newsContent = newsContent + " " + x.get_text().strip()
                                print(newsContent.strip())
                            except:
                                print("Error!")


                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")









        def katieParla():
            try:
                url = "https://katieparla.com/category/food-wine/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"id": "posts-container"}).find_all("h2",{"class":"entry-title"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"id": "posts-container"}).find_all("h2",{"class":"entry-title"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"id": "posts-container"}).find_all("h2",{"class":"entry-title"})[2].find("a").get("href")

                    url = "https://katieparla.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            print(newsImage)
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            print(newsTitle)
                            newsContent = ""
                            try:
                                newsTags = soup.find("section", {"id": "content"}).find("div", {"class": "post-content"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('aside'):
                                    i.replace_with("")
                                for i in newsTags.find_all('h2'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('table'):
                                    i.replace_with("")
                                for i in newsTags.find_all('hr'):
                                    i.replace_with("")
                                for i in newsTags.find_all('blockquote'):
                                    i.replace_with("")
                                for i in newsTags.find_all('em'):
                                    i.replace_with("")
                                for i in newsTags.find_all('section'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all():
                                    newsContent = newsContent + " " + x.get_text().strip()
                                print(newsContent.strip())
                            except:
                                print("Error!")


                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")















        def willTravelForFood():
            try:
                url = "http://willtravelforfood.com"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"id": "content"}).find_all("div",{"class":"single-post"})[0].find("div",{"id":"title"}).find("a").get("href")
                    secondNews = soup.find("div", {"id": "content"}).find_all("div",{"class":"single-post"})[1].find("div",{"id":"title"}).find("a").get("href")
                    thirdNews = soup.find("div", {"id": "content"}).find_all("div",{"class":"single-post"})[2].find("div",{"id":"title"}).find("a").get("href")

                    url = "http://willtravelforfood.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            print(newsImage)
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            print(newsTitle)
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"class": "post-content"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('aside'):
                                    i.replace_with("")
                                for i in newsTags.find_all('h2'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('table'):
                                    i.replace_with("")
                                for i in newsTags.find_all('hr'):
                                    i.replace_with("")
                                for i in newsTags.find_all('blockquote'):
                                    i.replace_with("")
                                for i in newsTags.find_all('em'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div'):
                                    i.replace_with("")
                                for i in newsTags.find_all('section'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                                print(newsContent.strip())
                            except:
                                print("Error!")


                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")








        def iAmAIleen():
            try:
                url = "https://iamaileen.com/category/travel/food-drinks/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"class": "et_pb_section et_pb_section_4_tb_body et_section_regular"}).find_all("div",{"class":"post-content"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"class": "et_pb_section et_pb_section_4_tb_body et_section_regular"}).find_all("div",{"class":"post-content"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"class": "et_pb_section et_pb_section_4_tb_body et_section_regular"}).find_all("div",{"class":"post-content"})[2].find("a").get("href")

                    url = "https://iamaileen.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            print(newsImage)
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            print(newsTitle)
                            newsContent = ""
                            try:
                                newsTags = soup.find_all("div", attrs={"class": "wp-block-group__inner-container"})
                                for x in newsTags:
                                    for i in x.find_all('img'):
                                        i.replace_with("")
                                    for i in x.find_all('iframe'):
                                        i.replace_with("")
                                    for i in x.find_all('aside'):
                                        i.replace_with("")
                                    for i in x.find_all('h2'):
                                        i.replace_with("")
                                    for i in x.find_all('figure'):
                                        i.replace_with("")
                                    for i in x.find_all('table'):
                                        i.replace_with("")
                                    for i in x.find_all('span'):
                                        i.replace_with("")
                                    for i in x.find_all('hr'):
                                        i.replace_with("")
                                    for i in x.find_all('blockquote'):
                                        i.replace_with("")
                                    for i in x.find_all('em'):
                                        i.replace_with("")
                                    for i in x.find_all('div'):
                                        i.replace_with("")
                                    for i in x.find_all('section'):
                                        i.replace_with("")
                                    for i in x.find_all('script'):
                                        i.replace_with("")
                                    for c in x.find_all("p"):
                                        newsContent = newsContent + " " + c.get_text().strip()
                                print(newsContent.strip())
                            except:
                                print("Error!")


                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")






        bucketListJourney()
        katieParla()
        willTravelForFood()
        iAmAIleen()









    def cruiseTravel():
        def breakingTravelNewsCruise():
            try:
                url = "https://www.breakingtravelnews.com/news/category/cruise/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"class": "widget-content clearfix"}).find_all("div",{"class":"sec-desc"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"class": "widget-content clearfix"}).find_all("div",{"class":"sec-desc"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"class": "widget-content clearfix"}).find_all("div",{"class":"sec-desc"})[2].find("a").get("href")

                    url = "https://www.breakingtravelnews.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            print(newsImage)
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            print(newsTitle)
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"class": "post-entry"})

                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('aside'):
                                    i.replace_with("")
                                for i in newsTags.find_all('h2'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('table'):
                                    i.replace_with("")
                                for i in newsTags.find_all('span'):
                                    i.replace_with("")
                                for i in newsTags.find_all('hr'):
                                    i.replace_with("")
                                for i in newsTags.find_all('blockquote'):
                                    i.replace_with("")
                                for i in newsTags.find_all('em'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div'):
                                    i.replace_with("")
                                for i in newsTags.find_all('section'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                                print(newsContent.strip())
                            except:
                                print("Error!")


                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")








        def travelPulseCruiseTravel():
            try:
                url = "https://www.travelpulse.com/news/cruise"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"id": "all_news"}).find("ul", {"class": "clear"}).find_all("li")[0].find("a").get("href")
                    secondNews = soup.find("div", {"id": "all_news"}).find("ul", {"class": "clear"}).find_all("li")[1].find("a").get("href")
                    thirdNews = soup.find("div", {"id": "all_news"}).find("ul", {"class": "clear"}).find_all("li")[2].find("a").get("href")

                    url = "https://www.travelpulse.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            print(newsImage)
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            print(newsTitle)
                            newsContent = ""
                            try:
                                newsTags = soup.find("article", {"class": "news detail"}).find("div", {"class": "content aqua_links clear"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('aside'):
                                    i.replace_with("")
                                for i in newsTags.find_all('h2'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('table'):
                                    i.replace_with("")
                                for i in newsTags.find_all('blockquote'):
                                    i.replace_with("")
                                for i in newsTags.find_all('em'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div'):
                                    i.replace_with("")
                                for i in newsTags.find_all('section'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                                print(newsContent.strip())
                            except:
                                print("Error!")


                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")






        def travelWeeklyCruise():
            try:
                url = "https://www.travelweekly.com/Cruise-Travel"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"class": "stories top-stories"}).find_all("div",{"class":"story"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"class": "stories top-stories"}).find_all("div",{"class":"story"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"class": "stories top-stories"}).find_all("div",{"class":"story"})[2].find("a").get("href")

                    url = "https://www.travelweekly.com"
                    firstUrl = url+firstNews
                    secondUrl = url+secondNews
                    thirdUrl = url+thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            print(newsImage)
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            print(newsTitle)
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"itemprop": "articleBody"})

                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('aside'):
                                    i.replace_with("")
                                for i in newsTags.find_all('h2'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('table'):
                                    i.replace_with("")
                                for i in newsTags.find_all('span'):
                                    i.replace_with("")
                                for i in newsTags.find_all('hr'):
                                    i.replace_with("")
                                for i in newsTags.find_all('blockquote'):
                                    i.replace_with("")
                                for i in newsTags.find_all('em'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div'):
                                    i.replace_with("")
                                for i in newsTags.find_all('section'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                                print(newsContent.strip())
                            except:
                                print("Error!")


                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")



        breakingTravelNewsCruise()
        travelPulseCruiseTravel()
        travelWeeklyCruise()







    def railTravel():
        def bbcRailNews():
            try:
                url = "https://www.bbc.com/news/topics/ce2gz914l5mt/rail-travel"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"id": "lx-stream"}).find_all("li", {"class": "lx-stream__post-container"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"id": "lx-stream"}).find_all("li", {"class": "lx-stream__post-container"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"id": "lx-stream"}).find_all("li", {"class": "lx-stream__post-container"})[2].find("a").get("href")

                    url = "https://www.bbc.com"
                    firstUrl = url + firstNews
                    secondUrl = url + secondNews
                    thirdUrl = url + thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            print(newsImage)
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            print(newsTitle)
                            newsContent = ""
                            try:
                                newsTags = soup.find("article", {"class": "ssrcss-1072xwf-ArticleWrapper"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('aside'):
                                    i.replace_with("")
                                for i in newsTags.find_all('h2'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('table'):
                                    i.replace_with("")
                                for i in newsTags.find_all('blockquote'):
                                    i.replace_with("")
                                for i in newsTags.find_all('em'):
                                    i.replace_with("")
                                for i in newsTags.find_all('section'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all("div", attrs={"data-component": "text-block"}):
                                    for a in x.find_all("p"):
                                        newsContent = newsContent + " " + a.get_text().strip()
                                print(newsContent.strip())
                            except:
                                try:
                                    newsTags = soup.find("div", {"id": "story-content"}).find("div",{"class": "body-content"})
                                    for i in newsTags.find_all('img'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('iframe'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('aside'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('h2'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('figure'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('table'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('blockquote'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('em'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('div'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('section'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('script'):
                                        i.replace_with("")
                                    for x in newsTags.find_all("p"):
                                        newsContent = newsContent + " " + x.get_text().strip()
                                    print(newsContent.strip())
                                except:
                                    print("Error!")


                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")







        def interRailNews():
            try:
                url = "https://www.interrail.eu/en/about-us/interrail-news"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div",{"class":"root responsivegrid"}).find_all("div",{"class":"eurail-block-component aem-GridColumn aem-GridColumn--default--12"})[0].find_all("p")[-1].find("a").get("href")
                    secondNews = soup.find("div",{"class":"root responsivegrid"}).find_all("div",{"class":"eurail-block-component aem-GridColumn aem-GridColumn--default--12"})[1].find_all("p")[-1].find("a").get("href")
                    thirdNews = soup.find("div",{"class":"root responsivegrid"}).find_all("div",{"class":"eurail-block-component aem-GridColumn aem-GridColumn--default--12"})[2].find_all("p")[-1].find("a").get("href")

                    url = "https://www.interrail.eu"
                    firstUrl = url+firstNews
                    secondUrl = url+secondNews
                    thirdUrl = url+thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            print(newsImage)
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            print(newsTitle)
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"class": "section aem-GridColumn aem-GridColumn--default--12"}).find("div", {"class": "e-text"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('aside'):
                                    i.replace_with("")
                                for i in newsTags.find_all('h2'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('table'):
                                    i.replace_with("")
                                for i in newsTags.find_all('span'):
                                    i.replace_with("")
                                for i in newsTags.find_all('hr'):
                                    i.replace_with("")
                                for i in newsTags.find_all('blockquote'):
                                    i.replace_with("")
                                for i in newsTags.find_all('em'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div'):
                                    i.replace_with("")
                                for i in newsTags.find_all('p',{"style":"text-align: right;"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('section'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                                print(newsContent.strip())
                            except:
                                print("Error!")


                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")






        bbcRailNews()
        interRailNews()













    rvNews()
    airTravel()
    hotelNews()
    foodBlogs()
    cruiseTravel()
    railTravel()



travel()
