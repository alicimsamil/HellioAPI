from bs4 import BeautifulSoup
import requests
import databaseTransactions

def showsMovies():
    def tvShows():
        def screenRantTv():
            try:
                url = "https://screenrant.com/tv-news/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"class": "w-content"}).find("section", {"class": "listing-content"}).find_all("article",{"class": "browse-clip"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"class": "w-content"}).find("section", {"class": "listing-content"}).find_all("article",{"class": "browse-clip"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"class": "w-content"}).find("section", {"class": "listing-content"}).find_all("article",{"class": "browse-clip"})[2].find("a").get("href")

                    url = "https://screenrant.com"
                    firstUrl = url+firstNews
                    secondUrl = url+secondNews
                    thirdUrl = url+thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Shows Movies"
                            subtopic = "Tv Shows"
                            name = "screenRantTv"
                            iconUrl = "https://findlogovector.com/wp-content/uploads/2020/06/screen-rant-logo-vector.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("section", {"id": "article-body"})
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





        def varietyTvShows():
            try:
                url = "https://variety.com/v/tv/news/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("ul", {"class": "o-tease-news-list"}).find_all("li",{"class": "o-tease-list__item"})[0].find("h3",{"id":"title-of-a-story"}).find("a").get("href")
                    secondNews = soup.find("ul", {"class": "o-tease-news-list"}).find_all("li",{"class": "o-tease-list__item"})[1].find("h3",{"id":"title-of-a-story"}).find("a").get("href")
                    thirdNews = soup.find("ul", {"class": "o-tease-news-list"}).find_all("li",{"class": "o-tease-list__item"})[2].find("h3",{"id":"title-of-a-story"}).find("a").get("href")

                    url = "https://variety.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Shows Movies"
                            subtopic = "Tv Shows"
                            name = "varietyTvShows"
                            iconUrl = "https://miro.medium.com/max/3520/1*VNe0Lf6ur02sK5f31dHbYA.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"class": "vy-cx-page-content"})
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






        def tvSeriesFinale():
            try:
                url = "https://tvseriesfinale.com/news/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("aside", {"class": "sidebar sidebar-secondary widget-area"}).find("div", {"class": "textwidget"}).find("ul").find_all("li")[0].find("a").get("href")
                    secondNews = soup.find("aside", {"class": "sidebar sidebar-secondary widget-area"}).find("div", {"class": "textwidget"}).find("ul").find_all("li")[1].find("a").get("href")
                    thirdNews = soup.find("aside", {"class": "sidebar sidebar-secondary widget-area"}).find("div", {"class": "textwidget"}).find("ul").find_all("li")[2].find("a").get("href")

                    url = "https://tvseriesfinale.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            name = "tvSeriesFinale"
                            topic = "Shows Movies"
                            subtopic = "Tv Shows"
                            iconUrl = "https://tvseriesfinale.com/wp-content/themes/tvseriesfinale/images/logo.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("main", {"class": "content"}).find("div", {"class": "entry-content"})
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





        def hollywoodReporterTv():
            try:
                url = "https://www.hollywoodreporter.com/c/tv/tv-news/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("section", {"class": "latest-stories-news-river"}).find_all("div",{"class":"story"})[0].find("a").get("href")
                    secondNews = soup.find("section", {"class": "latest-stories-news-river"}).find_all("div",{"class":"story"})[1].find("a").get("href")
                    thirdNews = soup.find("section", {"class": "latest-stories-news-river"}).find_all("div",{"class":"story"})[2].find("a").get("href")

                    url = "https://www.hollywoodreporter.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Shows Movies"
                            subtopic = "Tv Shows"
                            name = "hollywoodReporterTv"
                            iconUrl = "https://www.hollywoodreporter.com/wp-content/uploads/2014/07/thr_logo.jpg"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"class": "a-content"})
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






        def colliderTv():
            try:
                url = "https://collider.com/tv/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("section", {"class": "listing-content"}).find("div", {"class": "sentinel-category-list"}).find_all("article",{"class":"browse-clip"})[0].find("a").get("href")
                    secondNews = soup.find("section", {"class": "listing-content"}).find("div", {"class": "sentinel-category-list"}).find_all("article",{"class":"browse-clip"})[1].find("a").get("href")
                    thirdNews = soup.find("section", {"class": "listing-content"}).find("div", {"class": "sentinel-category-list"}).find_all("article",{"class":"browse-clip"})[2].find("a").get("href")

                    url = "https://collider.com"
                    firstUrl = url+firstNews
                    secondUrl = url+secondNews
                    thirdUrl = url+thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Shows Movies"
                            subtopic = "Tv Shows"
                            name = "colliderTv"
                            iconUrl = "https://collider.com/public/build/images/cl-amp-logo.93e10fe7.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("section", {"itemprop": "articleBody"})
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





        def theWrap():
            try:
                url = "https://www.thewrap.com/category/tv/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    topic = "Shows Movies"
                    subtopic = "Tv Shows"
                    firstNews = soup.find("div", {"id": "featured-main"}).find_all("div",{"class":"subtext"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"id": "featured-main"}).find_all("div",{"class":"subtext"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"id": "featured-main"}).find_all("div",{"class":"subtext"})[2].find("a").get("href")

                    url = "https://www.thewrap.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            name = "theWrap"
                            iconUrl = "https://www.thewrap.com/wp-content/themes/thewrap-canvas/imgs/thewrap-logo.svg"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"class": "article-content"}).find("div", {"class": "entry-content"})
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
                                for i in newsTags.find_all('section'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for x in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + x.get_text().strip()
                            except:
                                try:
                                    newsTags = soup.find("section", {"class": "aesop-content"})
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





        def mtvTvShows():
            try:
                url = "http://www.mtv.com/news/tv/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("main", {"class": "hub"}).find_all("div", {"class": "card post"})[0].find("a").get("href")
                    secondNews = soup.find("main", {"class": "hub"}).find_all("div", {"class": "card post"})[1].find("a").get("href")
                    thirdNews = soup.find("main", {"class": "hub"}).find_all("div", {"class": "card post"})[2].find("a").get("href")

                    url = "https://www.mtv.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Shows Movies"
                            subtopic = "Tv Shows"
                            name = "mtvTvShows"
                            iconUrl = "https://www.mtv.com.lb/Content/images/push-icon.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("article", {"class": "post"}).find("section", {"class": "entry-content"})
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
                                for i in newsTags.find_all('header'):
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










        screenRantTv()
        varietyTvShows()
        tvSeriesFinale()
        hollywoodReporterTv()
        colliderTv()
        theWrap()
        mtvTvShows()








    def movies():
        def cinemaBlend():
            try:
                url = "https://www.cinemablend.com/news.php"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("section", {"id": "body"}).find("div", {"id": "slot_body"}).find_all("a",{"class":"story-related-story"})[0].get("href")
                    secondNews = soup.find("section", {"id": "body"}).find("div", {"id": "slot_body"}).find_all("a",{"class":"story-related-story"})[1].get("href")
                    thirdNews = soup.find("section", {"id": "body"}).find("div", {"id": "slot_body"}).find_all("a",{"class":"story-related-story"})[2].get("href")

                    url = "https://www.cinemablend.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Shows Movies"
                            subtopic = "Movies"
                            name = "cinemaBlend"
                            iconUrl = "https://logovectorseek.com/wp-content/uploads/2020/11/cinemablend-logo-vector.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"id": "slot_main"}).find_all("div", attrs={"class": "text-body"})
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
                                    for i in x.find_all('div'):
                                        i.replace_with("")
                                    for i in x.find_all('section'):
                                        i.replace_with("")
                                    for i in x.find_all('script'):
                                        i.replace_with("")
                                    for i in x.find_all("p"):
                                        newsContent = newsContent + " " + i.get_text().strip()
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





        def screenRantMovies():
            try:
                url = "https://screenrant.com/movie-news/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"class": "w-content"}).find("section", {"class": "listing-content"}).find_all("article",{"class": "browse-clip"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"class": "w-content"}).find("section", {"class": "listing-content"}).find_all("article",{"class": "browse-clip"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"class": "w-content"}).find("section", {"class": "listing-content"}).find_all("article",{"class": "browse-clip"})[2].find("a").get("href")

                    url = "https://screenrant.com"
                    firstUrl = url+firstNews
                    secondUrl = url+secondNews
                    thirdUrl = url+thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Shows Movies"
                            subtopic = "Movies"
                            name = "screenRantMovies"
                            iconUrl = "https://findlogovector.com/wp-content/uploads/2020/06/screen-rant-logo-vector.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("section", {"id": "article-body"})
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

        def colliderMovies():
            try:
                url = "https://collider.com/all-news/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("section", {"class": "listing-content"}).find("div", {"class": "sentinel-category-list"}).find_all("article", {"class": "browse-clip"})[0].find("a").get("href")
                    secondNews = soup.find("section", {"class": "listing-content"}).find("div", {"class": "sentinel-category-list"}).find_all("article", {"class": "browse-clip"})[1].find("a").get("href")
                    thirdNews = soup.find("section", {"class": "listing-content"}).find("div", {"class": "sentinel-category-list"}).find_all("article", {"class": "browse-clip"})[2].find("a").get("href")

                    url = "https://collider.com"
                    firstUrl = url + firstNews
                    secondUrl = url + secondNews
                    thirdUrl = url + thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Shows Movies"
                            subtopic = "Movies"
                            name = "colliderMovies"
                            iconUrl = "https://upload.wikimedia.org/wikipedia/en/6/64/Collider-logo.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("section", {"itemprop": "articleBody"})
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







        def cbrMovies():
            try:
                url = "https://www.cbr.com/category/movies/news-movies/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("section", {"class": "listing-content"}).find("div", {"class": "sentinel-category-list"}).find_all("article", {"class": "browse-clip"})[0].find("a").get("href")
                    secondNews = soup.find("section", {"class": "listing-content"}).find("div", {"class": "sentinel-category-list"}).find_all("article", {"class": "browse-clip"})[1].find("a").get("href")
                    thirdNews = soup.find("section", {"class": "listing-content"}).find("div", {"class": "sentinel-category-list"}).find_all("article", {"class": "browse-clip"})[2].find("a").get("href")

                    url = "https://www.cbr.com"
                    firstUrl = url + firstNews
                    secondUrl = url + secondNews
                    thirdUrl = url + thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Shows Movies"
                            subtopic = "Movies"
                            name = "cbrMovies"
                            iconUrl = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTFB3kB1GM13rBThEfypxDAB6adFzNR7qT8R4Y4AsDN2sbe_QzB5stiH9ezjqEWFlI8Vg&usqp=CAU"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("section", {"itemprop": "articleBody"})
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








        def comingSoonMovies():
            try:
                url = "https://www.comingsoon.net/hub/movie-news"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"class": "featured-posts"}).find("ul", {"class": "listed-post"}).find_all("li", {"class": "listed-post-featured"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"class": "featured-posts"}).find("ul", {"class": "listed-post"}).find_all("li", {"class": "listed-post-featured"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"class": "featured-posts"}).find("ul", {"class": "listed-post"}).find_all("li", {"class": "listed-post-featured"})[2].find("a").get("href")

                    url = "https://www.comingsoon.net"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Shows Movies"
                            subtopic = "Movies"
                            name = "comingSoonMovies"
                            iconUrl = "https://www.comingsoon.net/assets/uploads/2021/05/evolve_media_llc_summer_season_pass_sales_2021_comingsoon_logo_r04b.svg"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("article", {"class": "js-article"}).find("div", {"class": "article-content"})
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








        def mtvMovies():
            try:
                url = "https://www.mtv.com/news/movies/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("main", {"class": "hub"}).find_all("div", {"class": "card post"})[0].find("a").get("href")
                    secondNews = soup.find("main", {"class": "hub"}).find_all("div", {"class": "card post"})[1].find("a").get("href")
                    thirdNews = soup.find("main", {"class": "hub"}).find_all("div", {"class": "card post"})[2].find("a").get("href")

                    url = "https://www.mtv.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Shows Movies"
                            subtopic = "Movies"
                            name = "mtvMovies"
                            iconUrl = "https://www.mtv.com.lb/Content/images/push-icon.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("article", {"class": "post"}).find("section", {"class": "entry-content"})
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
                                for i in newsTags.find_all('header'):
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








        cinemaBlend()
        screenRantMovies()
        colliderMovies()
        cbrMovies()
        comingSoonMovies()
        mtvMovies()










    tvShows()
    movies()




