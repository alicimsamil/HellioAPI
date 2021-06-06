
import requests
from bs4 import BeautifulSoup



def science():
    def mathematics():
        def physMathematics():
            try:
                url = "https://phys.org/science-news/mathematics/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"class": "sorted-news-list"}).find_all("article", attrs={"class": "sorted-article"})[0].find("h3").find("a").get("href")
                    secondNews = soup.find("div", {"class": "sorted-news-list"}).find_all("article", attrs={"class": "sorted-article"})[1].find("h3").find("a").get("href")
                    thirdNews = soup.find("div", {"class": "sorted-news-list"}).find_all("article", attrs={"class": "sorted-article"})[2].find("h3").find("a").get("href")

                    url = "https://phys.org"
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
                                newsTags = soup.find("article", {"class": "news-article"}).find("div", {"class": "mt-4 article-main"})
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
                                for i in newsTags.find_all('p',attrs={"class":"article-main__note mt-4"}):
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
                                newsContent = newsContent + " " + newsTags.find("p").get_text().strip()
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




        def scienceDailyMathematics():
            try:
                url = "https://www.sciencedaily.com/news/computers_math/mathematics/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"id": "heroes"}).find_all("h3", attrs={"class": "latest-head"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"id": "heroes"}).find_all("h3", attrs={"class": "latest-head"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"id": "heroes"}).find_all("h3", attrs={"class": "latest-head"})[2].find("a").get("href")

                    url = "https://www.sciencedaily.com"
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
                                newsTags = soup.find("div", {"id": "story_text"})
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
                                for i in newsTags.find_all('div',attrs={"class":"mobile-top-rectangle hidden-md hidden-lg"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"class":"impact-unit-wrapper"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"id":"story_source"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"id":"citations"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"id":"story_source"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"id":"journal_references"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"class":"clearfix"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('span'):
                                    i.replace_with("")
                                for i in newsTags.find_all('section'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for i in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + i.get_text().strip()
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








        def plusMagazineMathematics():
            try:
                url = "https://plus.maths.org/content/News"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"class": "region region-content"}).find("div", {"class": "view-content"}).find_all("div", attrs={"class": "views-field-view-node"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"class": "region region-content"}).find("div", {"class": "view-content"}).find_all("div", attrs={"class": "views-field-view-node"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"class": "region region-content"}).find("div", {"class": "view-content"}).find_all("div", attrs={"class": "views-field-view-node"})[2].find("a").get("href")

                    url = "https://plus.maths.org"
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
                                newsTags = soup.find("div", {"class": "field field-name-body field-type-text-with-summary field-label-hidden"}).find("div", {"class": "field-item even"})
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
                                for i in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + i.get_text().strip()
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






        def firstPostMathematics():
            try:
                url = "https://www.firstpost.com/tag/mathematics"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"class": "main-content"}).find_all("div", attrs={"class": "big-thumb"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"class": "main-content"}).find_all("div", attrs={"class": "big-thumb"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"class": "main-content"}).find_all("div", attrs={"class": "big-thumb"})[2].find("a").get("href")

                    url = "https://www.firstpost.com"
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
                                newsTags = soup.find("div", {"class": "inner-copy article-full-content"})
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
                                for i in newsTags.find_all('div'):
                                    i.replace_with("")
                                for i in newsTags.find_all('span'):
                                    i.replace_with("")
                                for i in newsTags.find_all('section'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for i in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + i.get_text().strip()
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





        physMathematics()
        scienceDailyMathematics()
        plusMagazineMathematics()
        firstPostMathematics()





    def biology():
        def sciencedailybiology():
            try:
                url = "https://www.sciencedaily.com/news/plants_animals/biology/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"id": "heroes"}).find_all("h3", attrs={"class": "latest-head"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"id": "heroes"}).find_all("h3", attrs={"class": "latest-head"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"id": "heroes"}).find_all("h3", attrs={"class": "latest-head"})[2].find("a").get("href")

                    url = "https://www.sciencedaily.com"
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
                                newsTags = soup.find("div", {"id": "story_text"})
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
                                for i in newsTags.find_all('div',attrs={"class": "mobile-top-rectangle hidden-md hidden-lg"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div', attrs={"class": "impact-unit-wrapper"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div', attrs={"id": "story_source"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div', attrs={"id": "citations"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div', attrs={"id": "story_source"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div', attrs={"id": "journal_references"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div', attrs={"class": "clearfix"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('span'):
                                    i.replace_with("")
                                for i in newsTags.find_all('section'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")
                                for i in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + i.get_text().strip()
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



        def physBiology():
            try:
                url = "https://phys.org/biology-news/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"class": "sorted-news-list"}).find_all("article", attrs={"class": "sorted-article"})[0].find("h3").find("a").get("href")
                    secondNews = soup.find("div", {"class": "sorted-news-list"}).find_all("article", attrs={"class": "sorted-article"})[1].find("h3").find("a").get("href")
                    thirdNews = soup.find("div", {"class": "sorted-news-list"}).find_all("article", attrs={"class": "sorted-article"})[2].find("h3").find("a").get("href")

                    url = "https://phys.org"
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
                                newsTags = soup.find("article", {"class": "news-article"}).find("div", {"class": "mt-4 article-main"})
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
                                for i in newsTags.find_all('p',attrs={"class":"article-main__note mt-4"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('blockquote'):
                                    i.replace_with("")
                                for i in newsTags.find_all('em'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div'):
                                    i.replace_with("")
                                for i in newsTags.find_all('span'):
                                    i.replace_with("")
                                for i in newsTags.find_all('hr'):
                                    i.replace_with("")
                                for i in newsTags.find_all('section'):
                                    i.replace_with("")
                                for i in newsTags.find_all('script'):
                                    i.replace_with("")


                                newsContent = newsContent + " " + newsTags.find("p").get_text().strip()
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






        def scitechDailybiology():
            try:
                url = "https://scitechdaily.com/news/biology/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"class": "mh-section mh-group"}).find_all("h3", attrs={"class": "entry-title"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"class": "mh-section mh-group"}).find_all("h3", attrs={"class": "entry-title"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"class": "mh-section mh-group"}).find_all("h3", attrs={"class": "entry-title"})[2].find("a").get("href")

                    url = "https://scitechdaily.com"
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
                                newsTags = soup.find("div", {"class": "entry-content clearfix"})
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
                                for i in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + i.get_text().strip()
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







        def sciNewsbiology():
            try:
                url = "http://www.sci-news.com/news/biology"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"class": "post-wrapper-archive"}).find_all("h2")[0].find("a").get("href")
                    secondNews = soup.find("div", {"class": "post-wrapper-archive"}).find_all("h2")[1].find("a").get("href")
                    thirdNews = soup.find("div", {"class": "post-wrapper-archive"}).find_all("h2")[2].find("a").get("href")

                    url = "http://www.sci-news.com"
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
                                newsTags = soup.find("div", {"class": "entry-content"})
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
                                for i in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + i.get_text().strip()
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











        sciencedailybiology()
        physBiology()
        scitechDailybiology()
        sciNewsbiology()





















    mathematics()
    biology()




science()
