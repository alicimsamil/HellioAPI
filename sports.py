import requests

from bs4 import BeautifulSoup

def sports():
    def chess():
        def chessCom():
            try:
                url = "https://www.chess.com/news"
                websiteRequest = requests.get(url, timeout=60, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")

                    firstNews= soup.find("main", {"class": "layout-component"}).find("div", {"id": "view-news-index"}).find("div", {"class": "post-preview-list-component"}).find_all("article",attrs={"class":"post-preview-component"})[0].find("a").get("href")
                    secondNews = soup.find("main", {"class": "layout-component"}).find("div", {"id": "view-news-index"}).find("div", {"class": "post-preview-list-component"}).find_all("article",attrs={"class":"post-preview-component"})[1].find("a").get("href")
                    thirdNews = soup.find("main", {"class": "layout-component"}).find("div", {"id": "view-news-index"}).find("div", {"class": "post-preview-list-component"}).find_all("article",attrs={"class":"post-preview-component"})[2].find("a").get("href")

                    url = "https://www.chess.com"

                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60,headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            print(newsImage)
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            print(newsTitle)
                            newsContent = ""

                            try:
                                newsTags = soup.find("main", {"class": "layout-component"}).find("article", {"class": "post-view-component"}).find("div", {"class": "post-view-content"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('header'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('hr'):
                                    i.replace_with("")
                                for i in newsTags.find_all('ins'):
                                    i.replace_with("")
                                for i in newsTags.find_all('em'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for i in newsTags.find_all('blockquote',attrs={"class":"twitter-tweet"}):
                                    i.replace_with("")

                                for x in newsTags.find_all():
                                    newsContent=newsContent+" "+x.get_text().strip()
                            except:
                                print("Error!")
                            print(newsContent.strip())

                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")



        def chess24():
            try:
                url = "https://chess24.com/en/read/news"
                websiteRequest = requests.get(url, timeout=60, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")

                    firstNews= soup.find("div", {"class": "pageContent"}).find("div", {"class": "contentWrap"}).find("div", {"class": "contentContainer"}).find("div", {"class": "topNewsHeadline hasManagementButtons"}).find("a").get("href")
                    secondNews = soup.find("div", {"class": "pageContent"}).find("div", {"class": "contentWrap"}).find("div", {"class": "contentContainer"}).find("ul", {"class": "topNews"}).find_all("li",attrs={"class":"hasManagementButtons"})[0].find("a").get("href")
                    thirdNews = soup.find("div", {"class": "pageContent"}).find("div", {"class": "contentWrap"}).find("div", {"class": "contentContainer"}).find("ul", {"class": "topNews"}).find_all("li",attrs={"class":"hasManagementButtons"})[1].find("a").get("href")

                    url = "https://chess24.com"

                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60,headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            print(newsImage)
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            print(newsTitle)
                            newsContent = ""

                            try:
                                newsTags = soup.find("div", {"class": "pageContent"}).find("div", {"class": "pageWrap"}).find("div", {"class": "contentWrap"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")


                                for x in newsTags.find_all("p",attrs={"class":"p1"}):
                                    newsContent=newsContent+" "+x.get_text().strip()
                            except:
                                print("Error!")
                            print(newsContent.strip())

                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")



        def chessBase():
            try:
                url = "https://en.chessbase.com"
                websiteRequest = requests.get(url, timeout=60, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews= soup.find_all("div", attrs={"class": "blog-news-container"})[1].find_all("div",attrs={"class":"blog-content"})[0].find("a").get("href")
                    secondNews = soup.find_all("div", attrs={"class": "blog-news-container"})[1].find_all("div",attrs={"class":"blog-content"})[1].find("a").get("href")
                    thirdNews = soup.find_all("div", attrs={"class": "blog-news-container"})[1].find_all("div",attrs={"class":"blog-content"})[2].find("a").get("href")

                    url = "https://en.chessbase.com"

                    firstUrl = url + firstNews
                    secondUrl = url + secondNews
                    thirdUrl = url + thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60,headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            print(newsImage)
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            print(newsTitle)
                            newsContent = ""

                            try:
                                newsTags = soup.find_all("section", attrs={"id": "ContentArea"})[1].find("div", {"id": "top-content-area"}).find("div", {"class": "full-story"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('h4'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"class":"cbdiagram"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"id":"cbadsmaindiv_full"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"class":"hidden-xs"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('p',attrs={"class":"blog-photo-subtitle"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"class":"cbtable"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"class":"cbreplay"}):
                                    i.replace_with("")

                                for i in newsTags.find_all('ul'):
                                    i.replace_with("")


                                for x in newsTags.find_all("p"):
                                    newsContent=newsContent+" "+x.get_text().strip()
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



        def fide():
            try:
                url = "https://www.fide.com/news"
                websiteRequest = requests.get(url, timeout=60, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews= soup.find("app-news").find_all("a",attrs={"class":"first-section-news"})[0].get("href")
                    secondNews = soup.find("app-news").find_all("a",attrs={"class":"first-section-news"})[1].get("href")
                    thirdNews = soup.find("app-news").find_all("a",attrs={"class":"third-section-news"})[0].get("href")

                    url = "https://www.fide.com"

                    firstUrl = url + firstNews
                    secondUrl = url + secondNews
                    thirdUrl = url + thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60,headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            print(newsImage)
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            print(newsTitle)
                            newsContent = ""

                            try:
                                newsTags = soup.find("app-client").find("app-news").find("div", {"class": "text padding-block"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('table'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"class":"cbdiagram"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('ul'):
                                    i.replace_with("")


                                for x in newsTags.find_all("p"):
                                    newsContent=newsContent+" "+x.get_text().strip()
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








        chessCom()
        chess24()
        chessBase()
        fide()






    chess()






sports()