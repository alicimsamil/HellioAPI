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
                                for i in newsTags.find_all('div',attrs={"class":"diagram-viewer-component"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"class":"table-content-responsive"}):
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




    def basketball():
        def nbaNews():
            try:
                url = "https://www.nba.com/news"
                websiteRequest = requests.get(url, timeout=60, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews= soup.find("body").find("section",{"class":"mt-6"}).find("div",{"class":"lg:flex"}).find("ul").find_all("li")[0].find("a").get("href")
                    secondNews = soup.find("body").find("section",{"class":"mt-6"}).find("div",{"class":"lg:flex"}).find("ul").find_all("li")[1].find("a").get("href")
                    thirdNews = soup.find("body").find("section",{"class":"mt-6"}).find("div",{"class":"lg:flex"}).find("ul").find_all("li")[2].find("a").get("href")

                    url = "https://www.nba.com"

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

                                newsTags = soup.find("section",{"class":"Block_tag__s36Yi"}).find("div", {"class": "Article_article__2Ue3h"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('table'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"class":"wp-caption alignnone"}):
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




        def cavsNation():
            try:
                url = "https://cavsnation.com"
                websiteRequest = requests.get(url, timeout=60, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews= soup.find("div",{"id":"mvp-site"}).find("main",{"id":"mvp-main-wrap"}).find("div",{"id":"mvp-main-body"}).find("div",{"id":"mvp-tab-col1"}).find_all("div",{"class":"mvp-side-tab-story left relative"})[0].find("a").get("href")
                    secondNews = soup.find("div",{"id":"mvp-site"}).find("main",{"id":"mvp-main-wrap"}).find("div",{"id":"mvp-main-body"}).find("div",{"id":"mvp-tab-col1"}).find_all("div",{"class":"mvp-side-tab-story left relative"})[1].find("a").get("href")
                    thirdNews = soup.find("div",{"id":"mvp-site"}).find("main",{"id":"mvp-main-wrap"}).find("div",{"id":"mvp-main-body"}).find("div",{"id":"mvp-tab-col1"}).find_all("div",{"class":"mvp-side-tab-story left relative"})[2].find("a").get("href")

                    url = "https://cavsnation.com"

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

                                newsTags = soup.find("div",{"id":"mvp-site"}).find("div", {"id": "mvp-post-content"}).find("div", {"id": "mvp-content-main"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('table'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div'):
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


        def realGmBasketball():
            try:
                url = "https://basketball.realgm.com"
                websiteRequest = requests.get(url, timeout=60, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews= soup.find("div",{"id":"site-takeover"}).find("div",{"class":"main-container"}).find("div",{"class":"lead-story-container"}).find("a").get("href")
                    secondNews = soup.find("div",{"id":"site-takeover"}).find("div",{"class":"main-container"}).find("div",{"class":"secondary-story-container"}).find_all("div",{"class":"secondary-story"})[0].find("a").get("href")
                    thirdNews = soup.find("div",{"id":"site-takeover"}).find("div",{"class":"main-container"}).find("div",{"class":"secondary-story-container"}).find_all("div",{"class":"secondary-story"})[1].find("a").get("href")

                    url = "https://basketball.realgm.com"

                    firstUrl = url+firstNews
                    secondUrl = url+secondNews
                    thirdUrl = url+thirdNews

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

                                newsTags = soup.find("div",{"id":"site-takeover"}).find("div", {"class": "main-container"}).find("div", {"class": "article-body"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('table'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div'):
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



        def euroLeague():
            try:
                url = "https://www.euroleague.net/news"
                websiteRequest = requests.get(url, timeout=60, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews= soup.find("div",{"id":"wrap"}).find("div",{"id":"main"}).find("div",{"class":"main-content"}).find("div",{"class":"padding-content"}).find_all("div",{"class":"row"})[0].find("a").get("href")
                    secondNews = soup.find("div",{"id":"wrap"}).find("div",{"id":"main"}).find("div",{"class":"main-content"}).find("div",{"class":"padding-content"}).find_all("div",{"class":"row"})[1].find("a").get("href")
                    thirdNews = soup.find("div",{"id":"wrap"}).find("div",{"id":"main"}).find("div",{"class":"main-content"}).find("div",{"class":"padding-content"}).find_all("div",{"class":"row"})[2].find("a").get("href")

                    url = "https://www.euroleague.net"

                    firstUrl = url+firstNews
                    secondUrl = url+secondNews
                    thirdUrl = url+thirdNews

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
                                newsTags = soup.find("div",{"id":"wrap"}).find("div", {"id": "main"}).find("div", {"id": "main-one"}).find("div", {"class": "info"}).find("div", {"class": "wp-field-value"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('h2'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('table'):
                                    i.replace_with("")
                                for i in newsTags.find_all('blockquote',{"class":"twitter-tweet"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('ul'):
                                    i.replace_with("")
                                for i in newsTags.find_all('center'):
                                    i.replace_with("")


                                for x in newsTags.find_all():
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





        def fibaNews():
            try:
                url = "http://www.fiba.basketball/news"
                websiteRequest = requests.get(url, timeout=60, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews= soup.find("div",{"class":"container"}).find("div",{"id":"news_list"}).find("section",{"class":"main_content"}).find("div",{"id":"news_highlighted"}).find("a").get("href")
                    secondNews = soup.find("div",{"class":"container"}).find("div",{"id":"news_list"}).find("section",{"class":"main_content"}).find("div",{"class":"related_articles"}).find_all("div",{"class":"related_row"})[0].find("a").get("href")
                    thirdNews = soup.find("div",{"class":"container"}).find("div",{"id":"news_list"}).find("section",{"class":"main_content"}).find("div",{"class":"related_articles"}).find_all("div",{"class":"related_row"})[1].find("a").get("href")

                    url = "http://www.fiba.basketball"

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
                                newsTags = soup.find("div",{"class":"container"}).find("section", {"id": "content"}).find("div", {"class": "article_content"}).find("div", {"class": "article_text"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
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
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")


                                for x in newsTags.find_all():
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







        nbaNews()
        cavsNation()
        realGmBasketball()
        euroLeague()
        fibaNews()




    def football():
        def skySportsFootball():
            try:
                url = "https://www.skysports.com/football/news"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"class": "site-wrapper"}).find("div", {"class": "grid__col site-layout-secondary__col1"}).find("div", {"class": "page-filters__offset"}).find("div", {"data-view": "news-list"}).find_all("div",attrs={"class":"news-list__item news-list__item--show-thumb-bp30"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"class": "site-wrapper"}).find("div", {"class": "grid__col site-layout-secondary__col1"}).find("div", {"class": "page-filters__offset"}).find("div", {"data-view": "news-list"}).find_all("div",attrs={"class":"news-list__item news-list__item--show-thumb-bp30"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"class": "site-wrapper"}).find("div", {"class": "grid__col site-layout-secondary__col1"}).find("div", {"class": "page-filters__offset"}).find("div", {"data-view": "news-list"}).find_all("div",attrs={"class":"news-list__item news-list__item--show-thumb-bp30"})[2].find("a").get("href")

                    url = "https://www.skysports.com"

                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            try:
                                newsImage = soup.find("meta", {"name": "twitter:image"}).get("content")
                                if newsImage!="":
                                    print(newsImage)
                                else:
                                    print("https://www.skysports.com")
                            except:
                                try:
                                    newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                                    if newsImage != "":
                                        print(newsImage)
                                    else:
                                        print("https://www.skysports.com")
                                except:
                                    print("https://www.skysports.com")

                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            if newsTitle!="":
                                print(newsTitle)
                            else:
                                soup.find("head").find("title").get_text()
                            newsContent = ""

                            try:
                                newsTags = soup.find("div", {"class": "section-wrap"}).find("div", {"data-component-name": "sdc-article-body"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('h3'):
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
                                for i in newsTags.find_all('ul'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")

                                for x in newsTags.find_all():
                                    newsContent = newsContent + " " + x.get_text().strip()
                                print(newsContent.strip())
                            except:
                                try:

                                    newsTags = soup.find("div", {"data-component-name": "sdc-article-livetext"})
                                    for i in newsTags.find_all('img'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('iframe'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('h3'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('figure'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('table'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('blockquote'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('em'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('ul'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('script'):
                                        i.replace_with("")

                                    for x in newsTags.find_all("div",{"class":"sdc-article-livetext__post"}):
                                        newsContent = newsContent + " " + x.find("p").get_text().strip()
                                    print(newsContent.strip())
                                except:
                                    print("Error!")


                        except:
                            print("Error!"+Exception)

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!"+Exception)



        def fifa():
            try:
                url = "https://www.fifa.com/worldcup/news/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"class": "content-wrap fi-basic-template"}).find("section", {"class": "section"}).find("div", {"class": "container-fluid section__body"}).find("div", {"class": "row"}).find_all("div",attrs={"class":"col-xs-12 col-sm-4 col-md-3 col-flex"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"class": "content-wrap fi-basic-template"}).find("section", {"class": "section"}).find("div", {"class": "container-fluid section__body"}).find("div", {"class": "row"}).find_all("div",attrs={"class":"col-xs-12 col-sm-4 col-md-3 col-flex"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"class": "content-wrap fi-basic-template"}).find("section", {"class": "section"}).find("div", {"class": "container-fluid section__body"}).find("div", {"class": "row"}).find_all("div",attrs={"class":"col-xs-12 col-sm-4 col-md-3 col-flex"})[2].find("a").get("href")

                    url = "https://www.fifa.com"

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
                                newsTags = soup.find("div", {"class": "fi-boxed-page"}).find("div", {"class": "d3-o-article__body fi-article__body"}).find_all("div",attrs={"class":"col-xs-12 col-sm-10 col-md-8 col-sm-offset-1 col-md-offset-2 d3-o-article__body-part--text fi-o-article__body-part--text"})

                                for x in newsTags:
                                    for i in x.find_all('img'):
                                        i.replace_with("")
                                    for i in x.find_all('iframe'):
                                        i.replace_with("")
                                    for i in x.find_all('strong'):
                                        i.replace_with("")
                                    for i in x.find_all('figure'):
                                        i.replace_with("")
                                    for i in x.find_all('table'):
                                        i.replace_with("")
                                    for i in x.find_all('blockquote'):
                                        i.replace_with("")
                                    for i in x.find_all('em'):
                                        i.replace_with("")
                                    for i in x.find_all('div'):
                                        i.replace_with("")
                                    for i in x.find_all('center'):
                                        i.replace_with("")
                                    for i in x.find_all('script'):
                                        i.replace_with("")

                                    for b in x.find_all():
                                        newsContent = newsContent + " " + b.get_text().strip()
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



        def bbcFootball():
            try:
                url = "https://www.bbc.com/sport/football"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"class": "sp-qa-top-stories"}).find_all("div",attrs={"class":"gel-layout__item"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"class": "sp-qa-top-stories"}).find_all("div",attrs={"class":"gel-layout__item"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"class": "sp-qa-top-stories"}).find_all("div",attrs={"class":"gel-layout__item"})[2].find("a").get("href")

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
                                newsTags = soup.find("div", {"id": "orb-modules"}).find("div", {"class": "qa-story-body"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('h3'):
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
                                for i in newsTags.find_all('ul'):
                                    i.replace_with("")

                                for x in newsTags.find_all():
                                    newsContent = newsContent + " " + x.get_text().strip()
                                print(newsContent.strip())
                            except:
                                try:
                                    newsTags = soup.find("div", {"id": "orb-modules"}).find("div",{"id": "lx-stream"}).find("ol",{"class": "lx-stream__feed"}).find_all("li",{"class":"lx-stream__post-container"})
                                    for y in newsTags:
                                        for i in y.find_all('img'):
                                            i.replace_with("")
                                        for i in y.find_all('iframe'):
                                            i.replace_with("")
                                        for i in y.find_all('h3'):
                                            i.replace_with("")
                                        for i in y.find_all('figure'):
                                            i.replace_with("")
                                        for i in y.find_all('table'):
                                            i.replace_with("")
                                        for i in y.find_all('blockquote'):
                                            i.replace_with("")
                                        for i in y.find_all('em'):
                                            i.replace_with("")
                                        for i in y.find_all('div'):
                                            i.replace_with("")
                                        for i in y.find_all('section'):
                                            i.replace_with("")
                                        for i in y.find_all('script'):
                                            i.replace_with("")
                                        for i in y.find_all('ul'):
                                            i.replace_with("")
                                        for i in y:
                                            for z in i.find("div",{"class":"lx-stream-post-body"}).find_all("p"):
                                                newsContent = newsContent + " " + z.get_text().strip()
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

        def guardianFootball():
            try:
                url = "https://www.theguardian.com/football"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"class": "l-side-margins"}).find("div", {"class": "fc-container__inner"}).find("div", {"data-title": "Football"}).find("div", {"class": "fc-slice-wrapper"}).find("div", {"data-test-id": "facia-card"}).find("h3").find("a").get("href")
                    secondNews = soup.find("div", {"class": "l-side-margins"}).find("div", {"class": "fc-container__inner"}).find("div", {"data-title": "Football"}).find_all("div", attrs={"class": "fc-slice-wrapper"})[1].find_all("h3")[0].find("a").get("href")
                    thirdNews = soup.find("div", {"class": "l-side-margins"}).find("div", {"class": "fc-container__inner"}).find("div", {"data-title": "Football"}).find_all("div", attrs={"class": "fc-slice-wrapper"})[1].find_all("h3")[1].find("a").get("href")

                    url = "https://www.theguardian.com"

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
                                newsTags = soup.find("div", {"class": "article-body-commercial-selector"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('h3'):
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
                                for i in newsTags.find_all('ul'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")

                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                                print(newsContent.strip())
                            except:
                                    try:
                                        newsTags = soup.find("div", {"class": "from-content-api podcast__body"})
                                        for i in newsTags.find_all('img'):
                                            i.replace_with("")
                                        for i in newsTags.find_all('iframe'):
                                            i.replace_with("")
                                        for i in newsTags.find_all('h3'):
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
                                        for i in newsTags.find_all('ul'):
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







        def marca():
            try:
                url = "https://www.marca.com/en/football.html"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("section", {"class": "row-layout"}).find("ul", {"class": "auto-items"}).find_all("li", attrs={"class": "content-item"})[0].find("a").get("href")
                    secondNews = soup.find("section", {"class": "row-layout"}).find("ul", {"class": "auto-items"}).find_all("li", attrs={"class": "content-item"})[1].find("a").get("href")
                    thirdNews = soup.find("section", {"class": "row-layout"}).find("ul", {"class": "auto-items"}).find_all("li", attrs={"class": "content-item"})[2].find("a").get("href")

                    url = "https://www.marca.com"

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
                                newsTags = soup.find("div", {"class": "ue-c-article__body"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('h3'):
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
                                for i in newsTags.find_all('ul'):
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





        def thesunFootball():
            try:
                url = "https://www.thesun.co.uk/sport/football/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"class": "sun-container__home-section"}).find_all("div", attrs={"class": "teaser__image-container"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"class": "sun-container__home-section"}).find_all("div", attrs={"class": "teaser__image-container"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"class": "sun-container__home-section"}).find_all("div", attrs={"class": "teaser__image-container"})[2].find("a").get("href")

                    url = "https://www.thesun.co.uk"

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
                                newsTags = soup.find("div", {"class": "article__content"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('h3'):
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
                                for i in newsTags.find_all('ul'):
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



















        skySportsFootball()
        fifa()
        bbcFootball()
        guardianFootball()
        marca()
        thesunFootball()










    chess()
    basketball()
    football()






sports()