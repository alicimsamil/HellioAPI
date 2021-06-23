import requests
from bs4 import BeautifulSoup
import databaseTransactions

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
                    firstNews= soup.find("main", {"class": "layout-component"}).find("div", {"id": "view-news-index"}).find_all("article",attrs={"class":"post-preview-component"})[0].find("a").get("href")
                    secondNews = soup.find("main", {"class": "layout-component"}).find("div", {"id": "view-news-index"}).find_all("article",attrs={"class":"post-preview-component"})[1].find("a").get("href")
                    thirdNews = soup.find("main", {"class": "layout-component"}).find("div", {"id": "view-news-index"}).find_all("article",attrs={"class":"post-preview-component"})[2].find("a").get("href")

                    url = "https://www.chess.com"

                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60,headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Sports"
                            subtopic = "Chess"
                            name = "chessCom"
                            iconUrl = "https://miro.medium.com/max/1200/1*j8ihwCTiWsf92Bbemg8VnA.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""

                            try:
                                newsTags = soup.find("main", {"class": "layout-component"}).find("div", {"class": "post-view-content"})
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

                                for x in newsTags.find_all("p"):
                                    newsContent=newsContent+" "+x.get_text().strip()
                            except:
                                print("Error!")
                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
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
                            topic = "Sports"
                            subtopic = "Chess"
                            name = "chess24"
                            iconUrl = "https://upload.wikimedia.org/wikipedia/en/thumb/0/05/Chess24.com_logo.svg/1200px-Chess24.com_logo.svg.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""

                            try:
                                newsTags = soup.find("div", {"class": "pageContent"}).find("div", {"class": "pageWrap"}).find("div", {"class": "contentWrap"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")


                                for x in newsTags.find_all("p",attrs={"class":"p1"}):
                                    newsContent=newsContent+" "+x.get_text().strip()
                            except:
                                print("Error!")
                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
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
                            topic = "Sports"
                            subtopic = "Chess"
                            name = "chessBase"
                            iconUrl = "https://en.chessbase.com/Images/Logos/Chessbase_35_Jahre_en.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
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
                            except:
                                print("Error!")

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
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
                            topic = "Sports"
                            subtopic = "Chess"
                            name = "fide"
                            iconUrl = "https://www.fide.com/assets/img/logo/logo.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
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
                            except:
                                print("Error!")

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
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
                            topic = "Sports"
                            subtopic = "Basketball"
                            name = "nbaNews"
                            iconUrl = "https://cdn.nba.com/manage/2020/10/NBA20Secondary20Logo-784x462.jpg"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
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
                            except:
                                print("Error!")

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
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
                            topic = "Sports"
                            subtopic = "Basketball"
                            name = "cavsNation"
                            iconUrl = "https://cavsnation.com/wp-content/uploads/2016/10/cavsnation.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
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
                            except:
                                print("Error!")

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
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
                            topic = "Sports"
                            subtopic = "Basketball"
                            name = "realGmBasketball"
                            iconUrl = "https://pbs.twimg.com/profile_images/1281824293/RealGM_Retro_400x400.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
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
                            except:
                                print("Error!")

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
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
                            topic = "Sports"
                            subtopic = "Basketball"
                            name = "euroLeague"
                            iconUrl = "https://www.euroleague.net/rs/28081/c0b3b50d-66b5-4a70-9d3b-0cc444335636/b6f/filename/turkish-airlines-euroleague.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""

                            try:

                                newsTags = soup.find("div",{"id":"wrap"}).find("div", {"id": "main"}).find("div", {"id": "main-one"}).find("div", {"class": "info"}).find("div", {"class": "wp-field wp-field-content"})
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
                                for x in newsTags.find_all("p"):
                                    newsContent=newsContent+" "+x.get_text().strip()
                            except:
                                print("Error!")

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
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
                            topic = "Sports"
                            subtopic = "Basketball"
                            name = "fibaNews"
                            iconUrl = "https://upload.wikimedia.org/wikipedia/en/thumb/4/47/International_Basketball_Federation_logo.svg/1200px-International_Basketball_Federation_logo.svg.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
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
                                for x in newsTags.find_all("p"):
                                    newsContent=newsContent+" "+x.get_text().strip()
                            except:
                                print("Error!")

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
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
                            topic = "Sports"
                            subtopic = "Football"
                            name = "skySportsFootball"
                            iconUrl = "https://cdn6.aptoide.com/imgs/9/5/1/951ea6ac9dcafc83f832ba2b013e2add_icon.png"
                            pageurl = url
                            try:
                                newsImage = soup.find("meta", {"name": "twitter:image"}).get("content")
                            except:
                                try:
                                    newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                                except:
                                    pass

                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            if newsTitle=="":
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

                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
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
                                except:
                                    print("Error!")

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")



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
                            topic = "Sports"
                            subtopic = "Football"
                            name = "fifa"
                            iconUrl = "https://img.fifa.com/image/upload/t_fe-auto/assets/img/layout/brand/fifa-logo.jpg"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
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

                                    for b in x.find_all("p"):
                                        newsContent = newsContent + " " + b.get_text().strip()
                            except:
                                print("Error!")

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
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
                            topic = "Sports"
                            subtopic = "Football"
                            name = "bbcFootball"
                            iconUrl = "https://img.icons8.com/ios/452/bbc-logo.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
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
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                            except:
                                try:
                                    newsTags = soup.find("ol",{"class": "lx-stream__feed"}).find_all("li",attrs={"class":"lx-stream__post-container"})
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
                                        for i in y.find_all('section'):
                                            i.replace_with("")
                                        for i in y.find_all('script'):
                                            i.replace_with("")
                                        for i in y.find_all('ul'):
                                            i.replace_with("")
                                        for i in y:
                                            for z in i.find("div",{"class":"lx-stream-post-body"}).find_all("p"):
                                                newsContent = newsContent + " " + z.get_text().strip()
                                except:
                                    print("Error!")

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
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
                            topic = "Sports"
                            subtopic = "Football"
                            name = "guardianFootball"
                            iconUrl = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/The_Guardian_2018.svg/1200px-The_Guardian_2018.svg.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""

                            try:
                                x = soup.find("div", {"class": "article-body-commercial-selector"})
                                for i in x.find_all('img'):
                                    i.replace_with("")
                                for i in x.find_all('iframe'):
                                    i.replace_with("")
                                for i in x.find_all('h3'):
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
                                for i in x.find_all('ul'):
                                    i.replace_with("")
                                for i in x.find_all('script'):
                                    i.replace_with("")
                                for x in x.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                            except:
                                    try:
                                        x = soup.find("div", {"class": "from-content-api podcast__body"})
                                        for i in x.find_all('img'):
                                            i.replace_with("")
                                        for i in x.find_all('iframe'):
                                            i.replace_with("")
                                        for i in x.find_all('h3'):
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
                                        for i in x.find_all('ul'):
                                            i.replace_with("")
                                        for i in x.find_all('script'):
                                            i.replace_with("")
                                        for x in x.find_all("p"):
                                            newsContent = newsContent + " " + x.get_text().strip()
                                    except:
                                        try:
                                            newsTags = soup.find_all("div", {"itemprop": "liveBlogUpdate"})
                                            for x in newsTags:
                                                for i in x.find_all('img'):
                                                    i.replace_with("")
                                                for i in x.find_all('iframe'):
                                                    i.replace_with("")
                                                for i in x.find_all('h3'):
                                                    i.replace_with("")
                                                for i in x.find_all('figure'):
                                                    i.replace_with("")
                                                for i in x.find_all('table'):
                                                    i.replace_with("")
                                                for i in x.find_all('blockquote'):
                                                    i.replace_with("")
                                                for i in x.find_all('em'):
                                                    i.replace_with("")
                                                for i in x.find_all('br'):
                                                    i.replace_with("")
                                                for i in x.find_all('ul'):
                                                    i.replace_with("")
                                                for i in x.find_all('script'):
                                                    i.replace_with("")
                                                for i in x.find_all("div",{"itemprop":"articleBody"}):
                                                    for a in i.find_all("p"):
                                                        newsContent = newsContent + " " + a.get_text().strip()
                                        except:
                                            print("Error!")

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
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
                    firstNews = soup.find("ul", {"class": "auto-items"}).find_all("li", attrs={"class": "content-item"})[0].find("a").get("href")
                    secondNews = soup.find("ul", {"class": "auto-items"}).find_all("li", attrs={"class": "content-item"})[1].find("a").get("href")
                    thirdNews = soup.find("ul", {"class": "auto-items"}).find_all("li", attrs={"class": "content-item"})[2].find("a").get("href")

                    url = "https://www.marca.com"

                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Sports"
                            subtopic = "Football"
                            name = "marca"
                            iconUrl = "https://cdn.freelogovectors.net/wp-content/uploads/2018/03/marca-logo.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
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
                            except:
                                print("Error!")

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
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
                            topic = "Sports"
                            subtopic = "Football"
                            name = "thesunFootball"
                            iconUrl = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/The_Sun.svg/1280px-The_Sun.svg.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
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
                            except:
                                print("Error!")

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
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









    def volleyball():
        def volleyballWorld():
            try:
                url = "https://en.volleyballworld.com/news/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("main", {"id": "main-content"}).find_all("div", attrs={"class": "d3-l-col__col-4"})[0].find("a").get("href")
                    secondNews = soup.find("main", {"id": "main-content"}).find_all("div", attrs={"class": "d3-l-col__col-4"})[1].find("a").get("href")
                    thirdNews = soup.find("main", {"id": "main-content"}).find_all("div", attrs={"class": "d3-l-col__col-4"})[2].find("a").get("href")

                    url = "https://en.volleyballworld.com"

                    firstUrl = url+firstNews
                    secondUrl = url+secondNews
                    thirdUrl = url+thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Sports"
                            subtopic = "Volleyball"
                            name = "volleyballWorld"
                            iconUrl = "https://images.volleyballworld.com/image/upload/f_png/assets/competition-logos/VBW_Logo"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""

                            try:
                                newsTags = soup.find("main",{"role":"main"})
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
                                for x in newsTags.find_all("div",attrs={"class":"oc-c-body-part oc-c-markdown-stories"}):
                                    newsContent = newsContent + " " + x.find("p").get_text().strip()
                            except:
                                print("Error!")

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")




        def worldOfVolley():
            try:
                url = "https://worldofvolley.com/News/Latest_news.html"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"id": "latestStuff-item1"}).find("div", {"id": "sliderLatestStories"}).find("div", {"class": "scrollerContent"}).find("div", {"class": "scrollerBox storyNav storyFirst"}).find_all("div", attrs={"class": "fica1"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"id": "latestStuff-item1"}).find("div", {"id": "sliderLatestStories"}).find("div", {"class": "scrollerContent"}).find("div", {"class": "scrollerBox storyNav storyFirst"}).find_all("div", attrs={"class": "fica1"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"id": "latestStuff-item1"}).find("div", {"id": "sliderLatestStories"}).find("div", {"class": "scrollerContent"}).find("div", {"class": "scrollerBox storyNav storyFirst"}).find_all("div", attrs={"class": "fica1"})[2].find("a").get("href")

                    url = "https://worldofvolley.com"

                    firstUrl = url+firstNews
                    secondUrl = url+secondNews
                    thirdUrl = url+thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Sports"
                            subtopic = "Volleyball"
                            name = "worldOfVolley"
                            iconUrl = "https://pbs.twimg.com/profile_images/824256905757519872/bLxNPeBZ_400x400.jpg"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""

                            try:
                                newsTags = soup.find("div",{"class":"storyHolder"}).find("div",{"class":"storyvieW-container"}).find("div",{"class":"lead"})
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
                                for i in newsTags.find_all('div'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                            except:
                                print("Error!")

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")




        def usaVolleyball():
            try:
                url = "https://usavolleyball.org/stories/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"class": "shell"}).find("main", {"id": "main"}).find("section", {"id": "story-section"}).find("div", {"class": "filter-results"}).find_all("div", attrs={"class": "foot"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"class": "shell"}).find("main", {"id": "main"}).find("section", {"id": "story-section"}).find("div", {"class": "filter-results"}).find_all("div", attrs={"class": "foot"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"class": "shell"}).find("main", {"id": "main"}).find("section", {"id": "story-section"}).find("div", {"class": "filter-results"}).find_all("div", attrs={"class": "foot"})[2].find("a").get("href")

                    url = "https://usavolleyball.org"

                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Sports"
                            subtopic = "Volleyball"
                            name = "usaVolleyball"
                            iconUrl = "https://usavolleyball.org/wp-content/uploads/2021/05/0515121USAV1200x667.jpg"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""

                            try:
                                newsTags = soup.find("div",{"class":"col-xs-9"})
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
                                for i in newsTags.find_all('div'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                            except:
                                print("Error!")

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")




        def bbcVolleyball():
            try:
                url = "https://www.bbc.com/sport/volleyball"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"id": "root"}).find("main", {"id": "main-content"}).find("ul").find_all("div", attrs={"type": "article"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"id": "root"}).find("main", {"id": "main-content"}).find("ul").find_all("div", attrs={"type": "article"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"id": "root"}).find("main", {"id": "main-content"}).find("ul").find_all("div", attrs={"type": "article"})[2].find("a").get("href")

                    url = "https://www.bbc.com"

                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Sports"
                            subtopic = "Volleyball"
                            name = "bbcVolleyball"
                            iconUrl = "https://img.icons8.com/ios/452/bbc-logo.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""

                            try:
                                newsTags = soup.find("div",{"id":"orb-modules"}).find("div",{"class":"qa-story-body"})
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
                                for i in newsTags.find_all('div'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                            except:
                                try:
                                    newsTags = soup.find("main", {"id": "main-content"})
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
                                    for x in newsTags.find_all("div",attrs={"data-component":"text-block"}):
                                        newsContent = newsContent + " " + x.get_text().strip()
                                except:
                                    print("Error!")

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")




        volleyballWorld()
        worldOfVolley()
        usaVolleyball()
        bbcVolleyball()




    def tennis():
        def tennisCom():
            try:
                url = "https://www.tennis.com/news/all-news/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("main", {"role": "main"}).find_all("div", attrs={"class": "d3-l-col__col-4"})[0].find("a").get("href")
                    secondNews = soup.find("main", {"role": "main"}).find_all("div", attrs={"class": "d3-l-col__col-4"})[1].find("a").get("href")
                    thirdNews = soup.find("main", {"role": "main"}).find_all("div", attrs={"class": "d3-l-col__col-4"})[2].find("a").get("href")

                    url = "https://www.tennis.com"

                    firstUrl = url+firstNews
                    secondUrl = url+secondNews
                    thirdUrl = url+thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Sports"
                            subtopic = "Tennis"
                            name = "tennisCom"
                            iconUrl = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAf0AAABjCAMAAACmCSk9AAAAxlBMVEX///9mzDMHEhhgyidkyy+A1Fdiyyz7/fpXyBHg9Njw+utpzTQAAAB60k5kzCleyiSn35K55qXt+ebY8NCb3ICl4Im05p3J673n99+M2GjT8MSXm534/fWs4Zf2/PLf9NXJ7blwz0CP2HLW8M3C6rEACBAAAAx20UiF1WB701G+6Kyn4I+N2GvCxMWf3oO25aHr7OymqatLxQBjZ2qMj5DLzc8OGR8pLzM8QURRVVfu7+/d3+AcIid5foEABBNpbnElLDC4urtK3eznAAARFElEQVR4nO2daWPithaGYSwLg4coOECAstiYjM3S0Ok6baf33v7/P3VtVi/v0ZI4LUN4v83EyLIe6UhHOpJq9ltrua1hrdrg6faIePqmtxB7a4l74s19gZ5+/Ee//r2r/tayaPrg6Rv9f1Q3+u9ZN/rvWTf671nCsjhjN/rvU35nPY8D7oi0ErxFLbjRv2w1pi1vtljP7SCoc1G1KbjR/0bU8MLH1SSpBY6z7xCqqAY3+t+UGuNpa7aYdId25FqpKbjRf48aD2Yj/37evktMwcuHBTf637jGM3/bm8eRK15gCm70r0JTr/ngrzcRt1Jpjw1v9K9LrZnfudd2E2/0r1B7NzFxEKLAlbqJN/rXrIb38JjWApdwE2/0r1+NxE+c+ZPupuQm3ui/I029WZi4iZE4uomS6I7K6CdOyaqznUz6285q1HpF7pG8kb/aTradxWg2rijJ5mjR6U+2K380qChFpNZgFobNwfQNX0Fq2vS368RNvFvn/99r7jXoWWiUsB00C/IUr1nMXWFlxeP+g0YVGBdftM9W7pnB1maZxEXUm8kKswWTzP1iHD4HmbwKPuxIa0CjVB47Sb+s1Xzs2cEp3zzaTEaKYnwTNRI3sfDaOXf3woNEt6hi7cnJu7ddUZyCYMkodNn1G4q8NUuvSsQ2mSfCeSDywxhm3cUdumZN7kCSIhOq2OjElsUKmQ26EoPXWjKQ5h39g8aoaycFkMk3Y9wSLJp3/oUKUNTcOoTwYfr1YqSfRdJvjGLHItJhlrjrhdKMNDmIK+TD099nG8cCiXPhdKnWOoGhiif640VSVVFenaBD1dVWGwVLkvS9rQtzvatmznIrNxpvrzn4fpko+gl7Lk2KWfXhTGIAmqiQTvSn6zqZuhUscLoT1Jmd6DdtcqKUiQ1RoxL64HmC/vg+ErLpFyaC2P9XxgFHVUS/OUTNqPCxXMzpTlVKP5QWI3O60PxL6U+kldViK5hLE/oLOftdzrmItlWPiw1UCf1xX97uz792SZsqo79SJW+5qFpJ6LfmCjJMdFFO9el7XSX7/YusoPev8a+C/sDW+9D6rlAJP01Cf6FOnkcAP01/vEH+bV7WHORSm763VL/hoKQDmFTlvBqqAvqrO5M0LMSpJqPfdzSS5bzcgEj6LRv9pfRkr5xLXfqhUZkwwRb/Cv9X02/cazf8vXgA8ZP0Vzqk0qZastQU/elcL0nul3KpSX8QGK68M8tOhn8//fz397/8+ccLUb5Ar6Xf6Oq0zJy4+wAyQtFf6KbvlHYoUvRjTaPMrJJLrkd/GhiWalKuqZX79PHjp19/+/L7Tz9//uWHP/5QTZG8Xq+k34BThArxAEx0YPqbmas9pHBnhSQJ+vfaPTIv2RM9+s/abzhlvp7OhnxI9fSUVIJEv35JKsHn7/98JWCpXkl/bdzyU/FluZOG9Jkd6ZtQa1NIEtJnQwOj7PiFJLXo++YtYj/E/JDTrhY8ffj62+9/ff7lzz9/eANTYEw/NxTqv6Dl71KxS58C6aeNQl9OYTYR0jdKkS0L+dSh3zCPuGTuzhp+gNrbgq9ffvrr58/f/1AJ9aNe1fbDF7X8XTKlTpqgbyJe8NEwfbMkC3P+OvQ7xnb/uO6O6ecqwceP//ny3++q6g5eQ7+p3SeX5RTPhaiAfrHnr4L+MJ9LDfotg87qmPFgqqZ/rgYfP35/AfRjWelKVo5ScbswwV0B/broV02/LvIDVA36j7jpM25ZwsLLYOJgCfXof3j6UpX9fwV9GA+y/1JLCDcIgjSghHpGdKqnz9zq6ee7KA36Q/TJXLjDXn+77tqBU14DP7YETfof/wtRdib+oDUdmwwOX06/SbVtzpbPC2+aqDXqxdTaHOP5xl8F/bqT8yWqoF8YS6jpj9FEDx8+TneTeY3xtNkfBvlG4RwHF7r0PyOSrbYQzl007G4Xo6bmzOHmGHOCC59bBTmnMT8xYcaczSj77jB2cNKFGDMFfZbaE+X2FbEwoJ9GWSiTZO2c6VfTH4Habk3yhT54jMW5wFl0/H9d+nA2cCYOH5UG89aD+LkTDryWvBos7id7QTeYzycFrY+jNfSV6S+CRfEVoyX2vKJcuUrpM+Ha3Y7v+/35kkmY5v1RKX0uok1v4fuL9Ua6EstzbqSa/qL8UrQy5q2Xx7ey0xv04D/9BknmOuJdAJGwAnve6/uheg1xaxjVuYH04VLrAC+qiNwSuoy+sFancLxWs0uHEvBNtq5L6DMRj7xDD9kYjJY0f+Fnc6mmD15anjDeJeW3dx+SWUvUbPrfQSDI1WC7sabjOMFm7YczjwwlMYzpfYCuvhXD9Mew9TOWfYamz8Q2P5LxhhTWvD2h6Vt24cNW5My81c0+p6TfKA+kWJsq9DBOap04txfNtg/9PU/qYqWmwHIjG8esGNPvQp4REak4gD5wNsCSps/cUiYa1EQ6y5kekj6PS7aQXJXjcfaxF9GPyCY3fgyc5/M/9eB/gd2+xvQyY4KKyjSj30SFxXhxneUkOCtoPWdTpOgLFA26Ib5VZOMkKfrcBmMhauqKBdmnlPTHoEfEln+vaT9TX7Xof/oJJqS13FbRXh48SpBEez+DzLEg0wQp+uU54VQe0VRz5oSgz2AYWG1F2BMn+5C67QN3P995SKRFH/t7U60ZxorowyFGJBlbQlxOJnlqlae4znIQwSrn8hH0rQ5MsRHjrt+QPppA4SBKCEmPPpzoa2otuVRDfwANOTWk2OkeoMiGzhH0BXFO9NSGz+em5og1vgCnSPmwTrbXVtOHAyKxIfvErHTgE92+3mprNfSx4ZfOLHigwrD2+e+YPltSIyaMNvd5+JHCYsBZDdybONleW+3xoVqe5Is/a+wR1Gr62N/DjUFaPFmZ0IfmLTeGA78BHWJ2UQ7TtyhUtRku5ayNxdEddRIDGpsk9LPPq+lTYYiWs3lUzbro0P/0N/qlZiBhJfRbS/AuS75TCxaL5Z/+TNCnLwh4KX08JZEKr84Z0if6j3o6a95+HknXYHTof4WG/1Ez9LUK+k00gLcVNTtEuTlPgBP06UShrVPTl5gor4q2P5UEPTDLaW8lIwCdpv87/CU2W+WPr4K+D55VujXIJ+GbU1vAcX0unR78YDV9QV1OQsVlGNKvEa7D8Ysst92bEXVagz7292qacTaV0F8jI06X6rFYyjlkwWmkSER10snBUa4GfZ9MEfsRpvSJ6I7zNzFLRBNoAXQsPwzqmmmG2FVCHwUw8G5HrhUq27M7Jd/DC4QMkA59eiSB5unM6RO+aE5pBViUDYCO4cf+nmYoYSX0oYXkQiF5wzKmP6qcPnRljOmTk4Z5MdHeFsefGob/Z5hxGE+EiqcK+tUdG35mYUz/oXL6eOnKmH4t0mPBhNPPe58a9OH6nvbGsSrojyuDn5mZvQD6eJ7OnP6D9i4+K1hn278GfZhx1VDj/L4K6E+ro3+ezbkA+lW1/Zqvvc+BiWwslEa3D/OtuSu1GvqtCulngkTBn79R+rWtfjwpE+eDR9RNH/t7d9q2pgL6nvEOVTo7p7mXC6BfleVPX02EssIyOK1lKOn/+ip/7/La/mmO6Lro13ym30Ss4BCTojb80N+Da274TZc16juHy18Z/VooiRQtfeZhT7PS8P8Fs62/J+PCPL7rpZ+83tXmb8W7OU8lfRzPqX9QyIXRvyjLX92o7/BwL9DlL3bjHyV9+Bo47YVVCX3TU2kk2bnSUd9Bg0n55FosnmZL1e3jeE5tf68i+vJlLBOdl3gvgH7VbT/V2B9qGQAWNZT0CX/PoC1WQh8urnLnBfrxKmd7cmo0O21HfZJpeqCBgv7XX1D6oUFTrIQ+WsfgG+8lkq/wXgP9VNPt8E7IR0vp+FcO/+kLhmGwU7kS+iF4ltzHo6mrpp/epriyXU7slD6Wn8LwY38Pb6jEqoQ+XFOSFauGLoB+9aO+vLzH+zZxYHt9t2dJQR/6ey2T43MqoT9G68naO1aw3gH9WnoXSDcg+IutyvLDiT4Df6+qeH4U2lUXrzpq+gLov6XlP8vr4FmgpOOXN33s78E8U6qGPo6rmeCH9fRu6CcGoIcODWS2gj7cxtFAwfWkDOn7+OEGWlXKbco01gXQr87yDxRHJ41Q+UUKyw/X90LiQiUsM/rkVhocTl08KrWsAbnX75roT+8CxRC4g3ZESOk//Q8mpBdEeCoeI/qc4hnewcR9+TfXBpG4J5rFNdFfC8bXUkPogcDYQEqfOKZNN57zUDxG9OuC2PY0hpO9DJ69ftbC5XVnjjd7XhH93WYuwXxZUZS9dCa3/NjfG5udCkvSx6fLFq/uHPuHsoDR9EnXL7F408nO17GKp3TudUX097MhzIof6O4f0F9K6X+F3b6RvyehjzsQ5mY76lYn/vGwCQUeSpg8f0ee9BMeL0WwbDQreD30J8eMcTGndraCfbBJL2tu+DX3752Kh6KPG3Nag31vOm55zXAbWxZ3jluQwLl0u+fFBnZ4D5vzQgdnYB/T1dAPM4lwYfuwOMDkfOIwy+hDf28KdsfJRNLHR7DtviCwh3bExA7fif4YlkP6hui+1Lb9Ls9+Luogroa+nbPpCf91+cCAGYjCFY9S+jie0zDQgqTfogNDGeOn9akTfbjUs3/ccuxtONgdFzxuDR4WGyEKxcpEyfO7APqVzPZMitlKiiPahtmTc701mOxjblNG/xPMsOlVADR9vdWCM33cUg6fInhkx8PNMF4G+LJbXpxJuBL68OxqJqwgnq9X/igMR/15BE+VSAbDxt2+3nktmeKh6Gt2IWf6ivqSGIxE5CH9TBQWhS6AfgWWnzr463BwruRU6DTnEvrQ34NTrjKR9PWO+8vSr4VGd9wUJea58dB10EdzeHpymhL6T/+rwt+T0ScG8cVMZofrWrdk0knlDne8Cvqe9p6q0pem51TQvf4rzufMiqavtz8rR99sebGYk3lu1uca6DeoA2TVYqf7+KDhh9v2Tf09Gf0a5cLllKf/is/lgcbdHN8Y/YX5bVzHfO8+lKYPDT86PEvxGpo+Md+TV55+Msp5IX5rWZgUuAb6g43hncRHSe/jS7r9rzC/5le/SejjLyuoQL82NthLkM1G6Xy3a6Bfa0xets3pcIgF2fRhPKexvyelr7VWXKRvtln59LXD0krPVdBPhuHam7eyeTrkmqQPz+dsmbtcMvq1pXrgV6Zf8wPD5s+sdXmV90ro18b3psWRwD+sBVL0sb/3aL6jSkof3rmQF6Bf82yj+m65Pnr3ldBPev/YMeHCRPe4EEzAJ85rgaG1cknp1x6U072IfnqtjXZOGO/C8I4LoF9ZVGe4oW+hLH2iez64hzL80N8bm3f7Cvq1kSvPNsf0a16XutEvL2a1idK/APrVRXU2wlizPISduUuGog8NP7wjQSEF/cRs0VacJXklD5luPjOl/eci6JC/vyb6icK1cvN2Up5R7vZCDP/pN7iN4wVXfSvpp6MWTJFZ7tKXXcDQWrelG9WsetwhT0e/OvrphXtxILEA6Q2Tfr48iKaP/T2zeM5D8ajop5tNbCe3ErVbn3KC7Ux1we901HPTS4aLX5wkIJzoXnqA/wxu8Jac0hz+iH6QXTlcwyfoCyYbc/iD7DVfrQBmk0px8Nh1d2WZL5J9eZZPav6IBf09zxXFW3LVciT3ZmU+cvUcR8eDd3mwjLt9JfqDHrbzZZD81Np9c3oVpGCBPe94qt83oF7zA/yAJEmN541zWRv467kdufv13bQ4hBvF3Q7a8PEdFryGyVMcig21VdygcdLYmz2EO80Girt8i2oNZuGi35vH9nDem6zC5uBVO/yuQFOv+RA++ouUwOih6eHy/D8AzrUX6x1Y6wAAAABJRU5ErkJggg=="
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""

                            try:
                                newsTags = soup.find("main",{"role":"main"}).find_all("div",attrs={"class":"oc-c-body-part oc-c-markdown-stories"})
                                for a in newsTags:
                                    for i in a.find_all('img'):
                                        i.replace_with("")
                                    for i in a.find_all('iframe'):
                                        i.replace_with("")
                                    for i in a.find_all('h3'):
                                        i.replace_with("")
                                    for i in a.find_all('figure'):
                                        i.replace_with("")
                                    for i in a.find_all('table'):
                                        i.replace_with("")
                                    for i in a.find_all('blockquote'):
                                        i.replace_with("")
                                    for i in a.find_all('em'):
                                        i.replace_with("")
                                    for i in a.find_all('ul'):
                                        i.replace_with("")
                                    for i in a.find_all('div'):
                                        i.replace_with("")
                                    for i in a.find_all('script'):
                                        i.replace_with("")
                                    for x in a.find_all("p"):
                                        newsContent = newsContent + " " + x.get_text().strip()
                            except:
                                print("Error!")

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")




        def bbcTennis():
            try:
                url = "https://www.bbc.com/sport/tennis"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")

                    firstNews = soup.find("div", {"class": "sp-qa-top-stories"}).find_all("div", attrs={"class": "gel-layout__item"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"class": "sp-qa-top-stories"}).find_all("div", attrs={"class": "gel-layout__item"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"class": "sp-qa-top-stories"}).find_all("div", attrs={"class": "gel-layout__item"})[2].find("a").get("href")

                    url = "https://www.bbc.com"
                    if "www" in firstNews:
                        firstUrl = firstNews
                    else:
                        firstUrl = url+firstNews

                    if "www" in secondNews:
                        secondUrl = secondNews
                    else:
                        secondUrl = url+secondNews

                    if "www" in thirdNews:
                        thirdUrl = thirdNews

                    else:
                        thirdUrl = url+thirdNews



                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Sports"
                            subtopic = "Tennis"
                            name = "bbcTennis"
                            iconUrl = "https://img.icons8.com/ios/452/bbc-logo.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""

                            try:
                                newsTags = soup.find("div", {"id": "orb-modules"}).find("div",{"class": "qa-story-body"})
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
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                            except:
                                try:
                                    newsTags = soup.find("div", {"id": "orb-modules"}).find("div",{"id": "lx-stream"}).find("ol", {"class": "lx-stream__feed"}).find_all("li", {"class": "lx-stream__post-container"})
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
                                        for i in y.find_all('section'):
                                            i.replace_with("")
                                        for i in y.find_all('script'):
                                            i.replace_with("")
                                        for i in y.find_all('ul'):
                                            i.replace_with("")
                                        for i in y:
                                            for z in i.find("div", {"class": "lx-stream-post-body"}).find_all("p"):
                                                newsContent = newsContent + " " + z.get_text().strip()
                                except:
                                    print("Error!")

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                        except:
                            print("Error!")


                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)


            except:
                print("Error!")





        def tennisHead():
            try:
                url = "https://tennishead.net/tennis/news/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"class": "qodef-blog-holder-inner"}).find_all("div", attrs={"class": "qodef-post-image"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"class": "qodef-blog-holder-inner"}).find_all("div", attrs={"class": "qodef-post-image"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"class": "qodef-blog-holder-inner"}).find_all("div", attrs={"class": "qodef-post-image"})[2].find("a").get("href")

                    url = "https://tennishead.net"

                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Sports"
                            subtopic = "Tennis"
                            name = "tennisHead"
                            iconUrl = "https://tennishead.net/wp-content/uploads/2020/06/THLogo2018WHITE-copy-3.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""

                            try:
                                newsTags = soup.find("div",{"class":"qodef-post-text-main"})
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
                                for i in newsTags.find_all('div'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                            except:
                                print("Error!")

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")






        def skySportsTennis():
            try:
                url = "https://www.skysports.com/tennis/news"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find_all("div", attrs={"class": "news-list__item"})[0].find("a").get("href")
                    secondNews = soup.find_all("div", attrs={"class": "news-list__item"})[1].find("a").get("href")
                    thirdNews = soup.find_all("div", attrs={"class": "news-list__item"})[2].find("a").get("href")

                    url = "https://www.skysports.com"

                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Sports"
                            subtopic = "Tennis"
                            name = "skySportsTennis"
                            iconUrl = "https://resources.premierleague.com/photos/2020/09/10/74770e21-77e1-4a33-9206-4236897808de/New-Sky-Sports-logo-2020.png?width=1350"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""

                            try:
                                newsTags = soup.find("div",{"itemprop":"articleBody"}).find("div",{"class":"article__body"})
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
                                for i in newsTags.find_all('div'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                            except:
                                print("Error!")

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")






        def theGuardianTennis():
            try:
                url = "https://www.theguardian.com/sport/tennis"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find_all("h3", attrs={"class": "fc-item__title"})[0].find("a").get("href")
                    secondNews = soup.find_all("h3", attrs={"class": "fc-item__title"})[1].find("a").get("href")
                    thirdNews = soup.find_all("h3", attrs={"class": "fc-item__title"})[2].find("a").get("href")

                    url = "https://www.theguardian.com"

                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Sports"
                            subtopic = "Tennis"
                            name = "theGuardianTennis"
                            iconUrl = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/The_Guardian_2018.svg/1200px-The_Guardian_2018.svg.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""

                            try:
                                newsTags = soup.find("div",{"class":"article-body-commercial-selector"})
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
                                for i in newsTags.find_all('div'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                            except:
                                try:
                                    newsTags = soup.find_all("div", attrs={"itemprop": "liveBlogUpdate"})
                                    for d in newsTags:
                                        for i in d.find_all('img'):
                                            i.replace_with("")
                                        for i in d.find_all('iframe'):
                                            i.replace_with("")
                                        for i in d.find_all('h3'):
                                            i.replace_with("")
                                        for i in d.find_all('figure'):
                                            i.replace_with("")
                                        for i in d.find_all('table'):
                                            i.replace_with("")
                                        for i in d.find_all('blockquote'):
                                            i.replace_with("")
                                        for i in d.find_all('em'):
                                            i.replace_with("")
                                        for i in d.find_all('ul'):
                                            i.replace_with("")
                                        for i in d.find_all('script'):
                                            i.replace_with("")
                                        for x in d.find_all("div",attrs={"itemprop":"articleBody"}):
                                            newsContent = newsContent + " " + x.get_text().strip()
                                except:
                                    try:
                                        d = soup.find("div",{"class": "content__standfirst"})
                                        for i in d.find_all('img'):
                                            i.replace_with("")
                                        for i in d.find_all('iframe'):
                                            i.replace_with("")
                                        for i in d.find_all('h3'):
                                            i.replace_with("")
                                        for i in d.find_all('figure'):
                                            i.replace_with("")
                                        for i in d.find_all('table'):
                                            i.replace_with("")
                                        for i in d.find_all('blockquote'):
                                            i.replace_with("")
                                        for i in d.find_all('em'):
                                            i.replace_with("")
                                        for i in d.find_all('ul'):
                                            i.replace_with("")
                                        for i in d.find_all('script'):
                                            i.replace_with("")
                                        for x in d.find_all("div", attrs={"itemprop": "articleBody"}):
                                             newsContent = newsContent + " " + x.get_text().strip()
                                    except:
                                        print("Error!")

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")








        tennisCom()
        bbcTennis()
        tennisHead()
        skySportsTennis()
        theGuardianTennis()



    def athletics():
        def worldAthletics():
            try:
                url = "https://www.worldathletics.org/news/news"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"class": "NewsGrid_grid__bTt_f"}).find_all("div", attrs={"data-name": "newsItem"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"class": "NewsGrid_grid__bTt_f"}).find_all("div", attrs={"data-name": "newsItem"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"class": "NewsGrid_grid__bTt_f"}).find_all("div", attrs={"data-name": "newsItem"})[2].find("a").get("href")

                    url = "https://www.worldathletics.org"

                    firstUrl = url+firstNews
                    secondUrl = url+secondNews
                    thirdUrl = url+thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Sports"
                            subtopic = "Athletics"
                            name = "worldAthletics"
                            iconUrl = "https://www.worldathletics.org/static/icons/256x256.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"name": "twitter:image"}).get("content")
                            newsTitle = soup.find("meta", {"name": "twitter:title"}).get("content")
                            newsContent = ""

                            try:
                                newsTags = soup.find("div",{"data-name":"article-main-content-container"}).find("div",{"data-name":"article-container"})
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
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                            except:
                                print("Error!")

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")




        def bbcAthletics():
            try:
                url = "https://www.bbc.com/sport/athletics"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"class": "sp-qa-top-stories"}).find_all("div", attrs={"class": "gel-layout__item"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"class": "sp-qa-top-stories"}).find_all("div", attrs={"class": "gel-layout__item"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"class": "sp-qa-top-stories"}).find_all("div", attrs={"class": "gel-layout__item"})[2].find("a").get("href")

                    url = "https://www.bbc.com"
                    if "www" in firstNews:
                        firstUrl = firstNews
                    else:
                        firstUrl = url + firstNews

                    if "www" in secondNews:
                        secondUrl = secondNews
                    else:
                        secondUrl = url + secondNews

                    if "www" in thirdNews:
                        thirdUrl = thirdNews

                    else:
                        thirdUrl = url + thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Sports"
                            subtopic = "Athletics"
                            name = "bbcAthletics"
                            iconUrl = "https://img.icons8.com/ios/452/bbc-logo.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""

                            try:
                                c = soup.find("div", {"id": "orb-modules"}).find("div",{"class": "qa-story-body"})
                                for i in c.find_all('img'):
                                    i.replace_with("")
                                for i in c.find_all('iframe'):
                                    i.replace_with("")
                                for i in c.find_all('h3'):
                                    i.replace_with("")
                                for i in c.find_all('figure'):
                                    i.replace_with("")
                                for i in c.find_all('table'):
                                    i.replace_with("")
                                for i in c.find_all('blockquote'):
                                    i.replace_with("")
                                for i in c.find_all('em'):
                                    i.replace_with("")
                                for i in c.find_all('div'):
                                    i.replace_with("")
                                for i in c.find_all('section'):
                                    i.replace_with("")
                                for i in c.find_all('script'):
                                    i.replace_with("")
                                for i in c.find_all('ul'):
                                    i.replace_with("")

                                for x in c.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                            except:
                                try:
                                    c = soup.find("div", {"id": "orb-modules"}).find("div",{"id": "lx-stream"}).find("ol", {"class": "lx-stream__feed"}).find_all("li", {"class": "lx-stream__post-container"})
                                    for y in c:
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
                                            for z in i.find("div", {"class": "lx-stream-post-body"}).find_all("p"):
                                                newsContent = newsContent + " " + z.get_text().strip()
                                except:
                                    try:
                                        newsTags = soup.find("main", {"id": "main-content"}).find_all("div",{"data-component":"text-block"})
                                        for c in newsTags:
                                            for i in c.find_all('img'):
                                                i.replace_with("")
                                            for i in c.find_all('iframe'):
                                                i.replace_with("")
                                            for i in c.find_all('h3'):
                                                i.replace_with("")
                                            for i in c.find_all('figure'):
                                                i.replace_with("")
                                            for i in c.find_all('table'):
                                                i.replace_with("")
                                            for i in c.find_all('blockquote'):
                                                i.replace_with("")
                                            for i in c.find_all('em'):
                                                i.replace_with("")
                                            for i in c.find_all('section'):
                                                i.replace_with("")
                                            for i in c.find_all('script'):
                                                i.replace_with("")
                                            for i in c.find_all('ul'):
                                                i.replace_with("")

                                            for x in c.find_all("p"):
                                                newsContent = newsContent + " " + x.get_text().strip()
                                    except:
                                        print("Error!")

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")






        def independentAthletics():
            try:
                url = "https://www.independent.co.uk/topic/athletics"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"id": "sectionContent"}).find_all("div", attrs={"class": "content"})[0].find("a",{"class":"title"}).get("href")
                    secondNews = soup.find("div", {"id": "sectionContent"}).find_all("div", attrs={"class": "content"})[1].find("a",{"class":"title"}).get("href")
                    thirdNews = soup.find("div", {"id": "sectionContent"}).find_all("div", attrs={"class": "content"})[2].find("a",{"class":"title"}).get("href")

                    url = "https://www.independent.co.uk"
                    firstUrl = url+firstNews
                    secondUrl = url+secondNews
                    thirdUrl = url+thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Sports"
                            subtopic = "Athletics"
                            name = "independentAthletics"
                            iconUrl = "https://w7.pngwing.com/pngs/226/415/png-transparent-the-independent-united-kingdom-logo-newspaper-news-media-newspaper-bald-eagle-vertebrate-media.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"id": "main"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('aside'):
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
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                            except:
                                print("Error!")

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")





        def eurosportAthletics():
            try:
                url = "https://www.eurosport.co.uk/athletics/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div",{"data-testid":"enriched-hero-card"}).find("div",{"class":"EnrichedHeroCard__mainCard"}).find("a").get("href")
                    secondNews = soup.find("div",{"data-testid":"enriched-hero-card"}).find_all("div",attrs={"class":"EnrichedHeroCard__secondaryCardWrapper"})[0].find("a").get("href")
                    thirdNews = soup.find("div",{"data-testid":"enriched-hero-card"}).find_all("div",attrs={"class":"EnrichedHeroCard__secondaryCardWrapper"})[1].find("a").get("href")

                    url = "https://www.eurosport.co.uk"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Sports"
                            subtopic = "Athletics"
                            name = "eurosportAthletics"
                            iconUrl = "https://cdn.worldvectorlogo.com/logos/eurosport-5.svg"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"id": "col-left"}).find("div", {"class": "article-body"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('aside'):
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
                                for i in newsTags.find_all('div',{"data-testid":"adwrapper"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('section'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for i in newsTags.find_all('ul'):
                                    i.replace_with("")
                                for x in newsTags.find_all("div",{"class":"-md:common-container"}):
                                    newsContent = newsContent + " " + x.get_text().strip()
                            except:
                                print("Error!")

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")




        worldAthletics()
        bbcAthletics()
        independentAthletics()
        eurosportAthletics()





    def fitness():
        def independentFitness():
            try:
                url = "https://www.independent.co.uk/topic/fitness"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"id": "sectionContent"}).find_all("div", attrs={"class": "content"})[0].find("a", {"class": "title"}).get("href")
                    secondNews = soup.find("div", {"id": "sectionContent"}).find_all("div", attrs={"class": "content"})[1].find("a", {"class": "title"}).get("href")
                    thirdNews = soup.find("div", {"id": "sectionContent"}).find_all("div", attrs={"class": "content"})[2].find("a", {"class": "title"}).get("href")

                    url = "https://www.independent.co.uk"
                    firstUrl = url + firstNews
                    secondUrl = url + secondNews
                    thirdUrl = url + thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Sports"
                            subtopic = "Fitness"
                            name = "independentFitness"
                            iconUrl = "https://w7.pngwing.com/pngs/226/415/png-transparent-the-independent-united-kingdom-logo-newspaper-news-media-newspaper-bald-eagle-vertebrate-media.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"id": "main"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('aside'):
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
                                for i in newsTags.find_all('div',{"class":"sc-qOvoE jhYSjM"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',{"class":"sc-pczax hJdRYq"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('section'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                            except:
                                print("Error!")

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")




        def menshealthFitness():
            try:
                url = "https://www.menshealth.com/fitness/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("main", {"class": "site-content"}).find("div", {"class": "feed feed-custom"}).find_all("div", attrs={"class": "custom-item-inner"})[0].find("a").get("href")
                    secondNews = soup.find("main", {"class": "site-content"}).find("div", {"class": "feed feed-custom"}).find_all("div", attrs={"class": "custom-item-inner"})[1].find("a").get("href")
                    thirdNews = soup.find("main", {"class": "site-content"}).find("div", {"class": "feed feed-custom"}).find_all("div", attrs={"class": "custom-item-inner"})[2].find("a").get("href")

                    url = "https://www.menshealth.com"
                    firstUrl = url + firstNews
                    secondUrl = url + secondNews
                    thirdUrl = url + thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Sports"
                            subtopic = "Fitness"
                            name = "menshealthFitness"
                            iconUrl = "https://thumbs.dreamstime.com/b/men-s-health-text-men-s-health-logo-icon-men-s-health-text-men-s-health-logo-icon-white-background-124845443.jpg"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("main", {"class": "site-content"}).find("div", {"class": "standard-body"}).find("div", {"class": "article-body-content standard-body-content"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('aside'):
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
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                            except:
                                try:
                                    newsTags = soup.find("div", {"class": "content-container"}).find("div", {"class": "slideshow-desktop-dek"})
                                    for i in newsTags.find_all('img'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('iframe'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('aside'):
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
                                    for x in newsTags.find_all("p"):
                                        newsContent = newsContent + " " + x.get_text().strip()
                                except:
                                    print("Error!")

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")





        def muscleAndFitness():
            try:
                url = "https://www.muscleandfitness.com/athletes-celebrities/news/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("main", {"class": "page-main"}).find_all("article", attrs={"class": "article"})[0].find("a").get("href")
                    secondNews = soup.find("main", {"class": "page-main"}).find_all("article", attrs={"class": "article"})[1].find("a").get("href")
                    thirdNews = soup.find("main", {"class": "page-main"}).find_all("article", attrs={"class": "article"})[2].find("a").get("href")

                    url = "https://www.muscleandfitness.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Sports"
                            subtopic = "Fitness"
                            name = "muscleAndFitness"
                            iconUrl = "https://iconape.com/wp-content/png_logo_vector/muscle-fitness-logo.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"class": "l-main__content"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('aside'):
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
                                for i in newsTags.find_all('div',attrs={"class":"post-tags"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"class":"link-related article link-related__with-thumb"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"id":"ds_default_anchor"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('section'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                            except:
                                print("Error!")

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")







        def tNation():
            try:
                url = "https://www.t-nation.com"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("main", {"id": "main"}).find_all("h2", attrs={"class": "entry-title"})[0].find("a").get("href")
                    secondNews = soup.find("main", {"id": "main"}).find_all("h2", attrs={"class": "entry-title"})[1].find("a").get("href")
                    thirdNews = soup.find("main", {"id": "main"}).find_all("h2", attrs={"class": "entry-title"})[2].find("a").get("href")

                    url = "https://www.t-nation.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Sports"
                            subtopic = "Fitness"
                            name = "tNation"
                            iconUrl = "https://pbs.twimg.com/profile_images/1337448675845545985/gMcYNcsV.jpg"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("main", {"id": "main"}).find("div", {"class": "entry-content"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('aside'):
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
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                            except:
                                print("Error!")

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")






        def myFitnessPal():
            try:
                url = "https://blog.myfitnesspal.com/category/fitness/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"class": "main-content"}).find("div", {"class": "wide-posts"}).find_all("h3", attrs={"class": "post-title"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"class": "main-content"}).find("div", {"class": "wide-posts"}).find_all("h3", attrs={"class": "post-title"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"class": "main-content"}).find("div", {"class": "wide-posts"}).find_all("h3", attrs={"class": "post-title"})[2].find("a").get("href")

                    url = "https://blog.myfitnesspal.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Sports"
                            subtopic = "Fitness"
                            name = "myFitnessPal"
                            iconUrl = "https://e7.pngegg.com/pngimages/269/147/png-clipart-myfitnesspal-data-breach-computer-security-user-data-security-my-fitness-pal-blue-physical-fitness.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"class": "main"}).find("div", {"class": "main-content"}).find("div", {"class": "post-content links-new-tab"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('aside'):
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
                                for i in newsTags.find_all('span'):
                                    i.replace_with("")
                                for i in newsTags.find_all('section'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                            except:
                                print("Error!")

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")






        independentFitness()
        menshealthFitness()
        muscleAndFitness()
        tNation()
        myFitnessPal()




    def mma():
        def mmaNews():
            try:
                url = "https://www.mmanews.com"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"id": "tdi_63"}).find_all("div", attrs={"class": "td-module-meta-info"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"id": "tdi_63"}).find_all("div", attrs={"class": "td-module-meta-info"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"id": "tdi_63"}).find_all("div", attrs={"class": "td-module-meta-info"})[2].find("a").get("href")

                    url = "https://www.mmanews.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Sports"
                            subtopic = "MMA"
                            name = "mmaNews"
                            iconUrl = "https://cdn.mmanews.com/wp-content/uploads/2017/01/mma-news-icon-e1608824310713.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"data-td-block-uid": "tdi_70"}).find("div", {"class": "tdb-block-inner td-fix-index"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('aside'):
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
                                for i in newsTags.find_all('span'):
                                    i.replace_with("")
                                for i in newsTags.find_all('section'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                            except:
                                print("Error!")

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")







        def mmaFighting():
            try:
                url = "https://www.mmafighting.com/latest-news"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"class": "c-compact-river"}).find_all("div", attrs={"class": "c-compact-river__entry"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"class": "c-compact-river"}).find_all("div", attrs={"class": "c-compact-river__entry"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"class": "c-compact-river"}).find_all("div", attrs={"class": "c-compact-river__entry"})[2].find("a").get("href")

                    url = "https://www.mmafighting.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Sports"
                            subtopic = "MMA"
                            name = "mmaFighting"
                            iconUrl = "https://cdn.vox-cdn.com/uploads/chorus_asset/file/8711975/mma-1000.0.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("main", {"id": "content"}).find("div", {"class": "c-entry-content"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('aside'):
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
                                for i in newsTags.find_all('span'):
                                    i.replace_with("")
                                for i in newsTags.find_all('section'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                            except:
                                print("Error!")

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")







        def mmaMania():
            try:
                url = "https://www.mmamania.com/latest-news"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"class": "c-compact-river"}).find_all("div", attrs={"class": "c-compact-river__entry"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"class": "c-compact-river"}).find_all("div", attrs={"class": "c-compact-river__entry"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"class": "c-compact-river"}).find_all("div", attrs={"class": "c-compact-river__entry"})[2].find("a").get("href")

                    url = "https://www.mmamania.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Sports"
                            subtopic = "MMA"
                            name = "mmaMania"
                            iconUrl = "https://s3.amazonaws.com/media.muckrack.com/groups/icons/mmamania.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("main", {"id": "content"}).find("div", {"class": "c-entry-content"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('aside'):
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
                                for i in newsTags.find_all('span'):
                                    i.replace_with("")
                                for i in newsTags.find_all('section'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                            except:
                                print("Error!")

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")







        def mmaJunkie():
            try:
                url = "https://mmajunkie.usatoday.com/news"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"id": "content"}).find("div", {"class": "column big category-page"}).find_all("article", attrs={"class": "block big"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"id": "content"}).find("div", {"class": "column big category-page"}).find_all("article", attrs={"class": "block big"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"id": "content"}).find("div", {"class": "column big category-page"}).find_all("article", attrs={"class": "block big"})[2].find("a").get("href")

                    url = "https://mmajunkie.usatoday.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Sports"
                            subtopic = "MMA"
                            name = "mmaJunkie"
                            iconUrl = "https://mmajunkie.usatoday.com/wp-content/uploads/sites/91/2013/11/mmajunkie-logo-icon.jpg?w=500"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"itemprop": "articleBody"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('aside'):
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
                                for i in newsTags.find_all('span'):
                                    i.replace_with("")
                                for i in newsTags.find_all('section'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                            except:
                                print("Error!")

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")





        def bjpenn():
            try:
                url = "https://www.bjpenn.com/mma-news/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"class": "td-category-grid td-container-wrap"}).find("div", {"class": "td_block_inner"}).find_all("div", attrs={"class": "td-module-thumb"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"class": "td-category-grid td-container-wrap"}).find("div", {"class": "td_block_inner"}).find_all("div", attrs={"class": "td-module-thumb"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"class": "td-category-grid td-container-wrap"}).find("div", {"class": "td_block_inner"}).find_all("div", attrs={"class": "td-module-thumb"})[2].find("a").get("href")

                    url = "https://www.bjpenn.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Sports"
                            subtopic = "MMA"
                            name = "bjpenn"
                            iconUrl = "https://pbs.twimg.com/profile_images/896937816655089665/XEFbV2l1_400x400.jpg"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"class": "td-post-content tagdiv-type"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('aside'):
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
                                for i in newsTags.find_all('span'):
                                    i.replace_with("")
                                for i in newsTags.find_all('section'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                            except:
                                print("Error!")

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")






        mmaNews()
        mmaFighting()
        mmaMania()
        mmaJunkie()
        bjpenn()









    chess()
    basketball()
    football()
    volleyball()
    tennis()
    athletics()
    fitness()
    mma()








