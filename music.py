from bs4 import BeautifulSoup
import requests
import databaseTransactions



def music():
    def electronicMusic():
        def edmNews():
            try:
                url = "https://edm.com/news"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("phoenix-non-personalized-recommendations-tracking",{"class":"m-card-group--content"}).find_all("div", {"class": "l-grid--item"})[0].find("a").get("href")
                    secondNews = soup.find("phoenix-non-personalized-recommendations-tracking",{"class":"m-card-group--content"}).find_all("div", {"class": "l-grid--item"})[1].find("a").get("href")
                    thirdNews = soup.find("phoenix-non-personalized-recommendations-tracking",{"class":"m-card-group--content"}).find_all("div", {"class": "l-grid--item"})[2].find("a").get("href")

                    url = "https://edm.com"
                    firstUrl = url+firstNews
                    secondUrl = url+secondNews
                    thirdUrl = url+thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Music"
                            subtopic = "Electronic Music"
                            name = "edmNews"
                            iconUrl = "https://edm.com/.image/c_fit%2Ccs_srgb%2Cq_auto:good%2Cw_916/MTgxNDU4NzMxNDkyNDUxNDky/edmcom---moore-kismet---website-header---front-image---916x240.webp"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"class": "l-grid--content-body"}).find("div", {"class": "m-detail--body"})
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












        def pitchforkElectronic():
            try:
                url = "https://pitchfork.com/news/?genre=electronic"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div",{"id":"news-page"}).find_all("div", {"class": "article-details"})[0].find("a").get("href")
                    secondNews = soup.find("div",{"id":"news-page"}).find_all("div", {"class": "article-details"})[1].find("a").get("href")
                    thirdNews = soup.find("div",{"id":"news-page"}).find_all("div", {"class": "article-details"})[2].find("a").get("href")

                    url = "https://pitchfork.com"
                    firstUrl = url+firstNews
                    secondUrl = url+secondNews
                    thirdUrl = url+thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Music"
                            subtopic = "Electronic Music"
                            name = "pitchforkElectronic"
                            iconUrl = "https://cdn.pitchfork.com/assets/misc/hp-og-image.jpg"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"class": "article__chunks"}).find("div", {"class": "grid-layout__content"})
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






        def edmTunesNews():
            try:
                url = "https://www.edmtunes.com/news/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div",{"class":"td-category-grid td-container-wrap"}).find_all("div", {"class": "td-module-thumb"})[0].find("a").get("href")
                    secondNews = soup.find("div",{"class":"td-category-grid td-container-wrap"}).find_all("div", {"class": "td-module-thumb"})[1].find("a").get("href")
                    thirdNews = soup.find("div",{"class":"td-category-grid td-container-wrap"}).find_all("div", {"class": "td-module-thumb"})[2].find("a").get("href")

                    url = "https://www.edmtunes.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Music"
                            subtopic = "Electronic Music"
                            name = "edmTunesNews"
                            iconUrl = "https://www.edmtunes.com/wp-content/uploads/2017/08/edmtunes-red.jpg"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
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







        def theMusicEssentials():
            try:
                url = "https://themusicessentials.com/news/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div",{"class":"td-ss-main-content"}).find_all("div", {"class": "td-module-thumb"})[0].find("a").get("href")
                    secondNews = soup.find("div",{"class":"td-ss-main-content"}).find_all("div", {"class": "td-module-thumb"})[1].find("a").get("href")
                    thirdNews = soup.find("div",{"class":"td-ss-main-content"}).find_all("div", {"class": "td-module-thumb"})[2].find("a").get("href")

                    url = "https://themusicessentials.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Music"
                            subtopic = "Electronic Music"
                            name = "theMusicEssentials"
                            iconUrl = "https://themusicessentials.com/wp-content/uploads/2015/06/T.H.E-Logo2.jpg"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"class": "td-ss-main-content"}).find("div", {"class": "td-post-content"})
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







        def edmSauceNews():
            try:
                url = "https://www.edmsauce.com/news/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div",{"class":"elementor-posts-container"}).find_all("article", {"class": "elementor-post"})[0].find("a").get("href")
                    secondNews = soup.find("div",{"class":"elementor-posts-container"}).find_all("article", {"class": "elementor-post"})[1].find("a").get("href")
                    thirdNews = soup.find("div",{"class":"elementor-posts-container"}).find_all("article", {"class": "elementor-post"})[2].find("a").get("href")

                    url = "https://www.edmsauce.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Music"
                            subtopic = "Electronic Music"
                            name = "edmSauceNews"
                            iconUrl = "https://www.edmsauce.com/wp-content/uploads/2014/12/edmsaucelogo.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"class": "theiaPostSlider_slides"}).find("div", {"class": "theiaPostSlider_preloadedSlide"})
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
                                for i in newsTags.find_all('p'):
                                    newsContent = newsContent + " " + i.get_text().strip()

                            except:
                                try:
                                    newsTags = soup.find("div", {"class": "zox-post-main"}).find("div", {"class": "zox-post-body left zoxrel zox100"})
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

                                    newsContent = newsContent + " " + newsTags.find("p").get_text().strip()
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







        edmNews()
        pitchforkElectronic()
        edmTunesNews()
        theMusicEssentials()
        edmSauceNews()





    def rock():
        def loudWireNews():
            try:
                url = "https://loudwire.com/category/news/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div",{"class":"main-content"}).find("div",{"class":"blogroll-inner"}).find_all("div", {"class": "content"})[0].find("a").get("href")
                    secondNews = soup.find("div",{"class":"main-content"}).find("div",{"class":"blogroll-inner"}).find_all("div", {"class": "content"})[1].find("a").get("href")
                    thirdNews = soup.find("div",{"class":"main-content"}).find("div",{"class":"blogroll-inner"}).find_all("div", {"class": "content"})[2].find("a").get("href")

                    url = "https://loudwire.com"
                    if '//' in firstNews[0:2]:
                        firstUrl = "https:"+firstNews
                    else:
                        firstUrl = firstNews

                    if '//' in secondNews[0:2]:
                        secondUrl = "https:"+secondNews

                    else:
                        secondUrl = secondNews

                    if '//' in thirdNews[0:2]:
                        thirdUrl = "https:"+thirdNews

                    else:
                        thirdUrl = thirdNews


                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Music"
                            subtopic = "Rock"
                            name = "loudWireNews"
                            iconUrl = "https://townsquare.media/site/366/files/2019/03/ldlogo2.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"class": "entry"}).find("div", {"class": "pod-content"})
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









        def blabberMouth():
            try:
                url = "https://www.blabbermouth.net/news"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div",{"role":"main"}).find_all("header", {"class": "article-header"})[0].find("a").get("href")
                    secondNews = soup.find("div",{"role":"main"}).find_all("header", {"class": "article-header"})[1].find("a").get("href")
                    thirdNews = soup.find("div",{"role":"main"}).find_all("header", {"class": "article-header"})[2].find("a").get("href")

                    url = "https://www.blabbermouth.net"
                    firstUrl = url+firstNews
                    secondUrl = url+secondNews
                    thirdUrl = url+thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Music"
                            subtopic = "Rock"
                            name = "blabberMouth"
                            iconUrl = "https://www.blabbermouth.net/assets/main-logo-93709a4802ad4d1f9f32d19edee7e59fa97395795d2711150f4271ba47e07f08.jpg"
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










        def weareThePit():
            try:
                url = "https://www.wearethepit.com/category/news/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div",{"id":"main-content"}).find_all("h3", {"class": "entry-title mh-posts-large-title"})[0].find("a").get("href")
                    secondNews = soup.find("div",{"id":"main-content"}).find_all("h3", {"class": "entry-title mh-posts-large-title"})[1].find("a").get("href")
                    thirdNews = soup.find("div",{"id":"main-content"}).find_all("h3", {"class": "entry-title mh-posts-large-title"})[2].find("a").get("href")

                    url = "https://www.wearethepit.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Music"
                            subtopic = "Rock"
                            name = "weareThePit"
                            iconUrl = "http://www.wearethepit.com/wp-content/uploads/2019/01/heromockup-1.jpg"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"id": "main-content"}).find("div", {"class": "entry-content clearfix"})
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
                                for i in newsTags.find_all('hr'):
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

                                newsContent = newsContent + " " + newsTags.get_text().strip()
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






        loudWireNews()
        blabberMouth()
        weareThePit()







    def blues():
        def bluesMatters():
            try:
                url = "https://bluesmatters.com/news/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div",{"class":"entry-content"}).find("div",{"class":"et_pb_ajax_pagination_container"}).find_all("h2", {"class": "entry-title"})[0].find("a").get("href")
                    secondNews = soup.find("div",{"class":"entry-content"}).find("div",{"class":"et_pb_ajax_pagination_container"}).find_all("h2", {"class": "entry-title"})[1].find("a").get("href")
                    thirdNews = soup.find("div",{"class":"entry-content"}).find("div",{"class":"et_pb_ajax_pagination_container"}).find_all("h2", {"class": "entry-title"})[2].find("a").get("href")

                    url = "https://bluesmatters.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Music"
                            subtopic = "Blues"
                            name = "bluesMatters"
                            iconUrl = "https://bluesmatters.com/wp-content/uploads/2020/05/blues-matters-logo-large.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"class": "et_pb_row et_pb_row_0"}).find_all("div", attrs={"class": "et_pb_text_inner"})
                                for c in newsTags:
                                    for i in c.find_all('img'):
                                        i.replace_with("")
                                    for i in c.find_all('iframe'):
                                        i.replace_with("")
                                    for i in c.find_all('aside'):
                                        i.replace_with("")
                                    for i in c.find_all('h2'):
                                        i.replace_with("")
                                    for i in c.find_all('figure'):
                                        i.replace_with("")
                                    for i in c.find_all('table'):
                                        i.replace_with("")
                                    for i in c.find_all('div'):
                                        i.replace_with("")
                                    for i in c.find_all('blockquote'):
                                        i.replace_with("")
                                    for i in c.find_all('em'):
                                        i.replace_with("")
                                    for i in c.find_all('section'):
                                        i.replace_with("")
                                    for i in c.find_all('script'):
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






        def americanBluesScene():
            try:
                url = "https://www.americanbluesscene.com/category/news/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div",{"class":"uael-post__body"}).find("div",{"class":"uael-post-grid uael-posts"}).find_all("div", {"class": "uael-post-wrapper"})[0].find("a").get("href")
                    secondNews = soup.find("div",{"class":"uael-post__body"}).find("div",{"class":"uael-post-grid uael-posts"}).find_all("div", {"class": "uael-post-wrapper"})[1].find("a").get("href")
                    thirdNews = soup.find("div",{"class":"uael-post__body"}).find("div",{"class":"uael-post-grid uael-posts"}).find_all("div", {"class": "uael-post-wrapper"})[2].find("a").get("href")

                    url = "https://www.americanbluesscene.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Music"
                            subtopic = "Blues"
                            name = "americanBluesScene"
                            iconUrl = "https://www.americanbluesscene.com/wp-content/uploads/2020/04/american-blues-scene-logo.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
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








        def downBeat():
            try:
                url = "https://downbeat.com/news"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("ul",{"class":"category-list"}).find_all("li")[0].find_all("a")[-1].get("href")
                    secondNews = soup.find("ul",{"class":"category-list"}).find_all("li")[1].find_all("a")[-1].get("href")
                    thirdNews = soup.find("ul",{"class":"category-list"}).find_all("li")[2].find_all("a")[-1].get("href")

                    url = "https://downbeat.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Music"
                            subtopic = "Blues"
                            name = "downBeat"
                            iconUrl = "https://downbeat.com/_img/logo_0087DE.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"class": "col-sm-7 col-sm-push-2 pad-col"})
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






        def bluesRockReview():
            try:
                url = "https://bluesrockreview.com/category/news"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div",{"id":"content"}).find("div",{"class":"article-container"}).find_all("h2",{"class":"entry-title"})[0].find("a").get("href")
                    secondNews = soup.find("div",{"id":"content"}).find("div",{"class":"article-container"}).find_all("h2",{"class":"entry-title"})[1].find("a").get("href")
                    thirdNews = soup.find("div",{"id":"content"}).find("div",{"class":"article-container"}).find_all("h2",{"class":"entry-title"})[2].find("a").get("href")

                    url = "https://bluesrockreview.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Music"
                            subtopic = "Blues"
                            name = "bluesRockReview"
                            iconUrl = "https://bluesrockreview.com/wp-content/uploads/2014/03/cropped-brr_logo.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"id": "content"}).find("div", {"class": "entry-content clearfix"})
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




        bluesMatters()
        americanBluesScene()
        downBeat()
        bluesRockReview()






    def hipHop():
        def hipHopDx():
            try:
                url = "https://hiphopdx.com/news#"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div",{"id":"cmn_wrap"}).find("div",{"class":"content with-sidebars"}).find("div",{"class":"secondary-posts"}).find_all("div",{"class":"news-info"})[0].find("a").get("href")
                    secondNews = soup.find("div",{"id":"cmn_wrap"}).find("div",{"class":"content with-sidebars"}).find("div",{"class":"secondary-posts"}).find_all("div",{"class":"news-info"})[1].find("a").get("href")
                    thirdNews = soup.find("div",{"id":"cmn_wrap"}).find("div",{"class":"content with-sidebars"}).find("div",{"class":"secondary-posts"}).find_all("div",{"class":"news-info"})[2].find("a").get("href")

                    url = "https://hiphopdx.com"
                    firstUrl = url+firstNews
                    secondUrl = url+secondNews
                    thirdUrl = url+thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Music"
                            subtopic = "Hip Hop"
                            name = "hipHopDx"
                            iconUrl = "https://static.hiphopdx.com/assets/prod/img/logo-black.svg?v11"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"id": "cmn_wrap"}).find("div", {"itemprop": "articleBody"})
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





        def theSource():
            try:
                url = "https://thesource.com/category/news/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div",{"id":"main"}).find_all("h2",{"class":"cb-post-title"})[0].find("a").get("href")
                    secondNews = soup.find("div",{"id":"main"}).find_all("h2",{"class":"cb-post-title"})[1].find("a").get("href")
                    thirdNews = soup.find("div",{"id":"main"}).find_all("h2",{"class":"cb-post-title"})[2].find("a").get("href")

                    url = "https://thesource.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Music"
                            subtopic = "Hip Hop"
                            name = "theSourceHipHop"
                            iconUrl = "https://thesource.com/source_logo_.svg"
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
                                for i in newsTags.find_all('blockquote'):
                                    i.replace_with("")
                                for i in newsTags.find_all('em'):
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

        def pitchforkHipHop():
            try:
                url = "https://pitchfork.com/news/?genre=rap"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"id": "news-page"}).find_all("div", {"class": "article-details"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"id": "news-page"}).find_all("div", {"class": "article-details"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"id": "news-page"}).find_all("div", {"class": "article-details"})[2].find("a").get("href")

                    url = "https://pitchfork.com"
                    firstUrl = url + firstNews
                    secondUrl = url + secondNews
                    thirdUrl = url + thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Music"
                            subtopic = "Hip Hop"
                            name = "pitchforkHipHop"
                            iconUrl = "https://cdn.pitchfork.com/assets/misc/hp-og-image.jpg"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"class": "article__chunks"}).find("div", {"class": "grid-layout__content"})
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







        def xxlmagHipHop():
            try:
                url = "https://www.xxlmag.com/category/news/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("section", {"id": "carbonwidget-taxonomy-1"}).find("div", {"class": "blogroll-inner clearfix"}).find_all("div", {"class": "content"})[0].find("a").get("href")
                    secondNews = soup.find("section", {"id": "carbonwidget-taxonomy-1"}).find("div", {"class": "blogroll-inner clearfix"}).find_all("div", {"class": "content"})[1].find("a").get("href")
                    thirdNews = soup.find("section", {"id": "carbonwidget-taxonomy-1"}).find("div", {"class": "blogroll-inner clearfix"}).find_all("div", {"class": "content"})[2].find("a").get("href")

                    url = "https://www.xxlmag.com"
                    if "//" in firstNews[0:2]:
                        firstUrl = "https:"+firstNews
                    else:
                        firstUrl=firstNews
                    if "//" in secondNews[0:2]:
                        secondUrl = "https:"+secondNews
                    else:
                        secondUrl=secondNews
                    if "//" in thirdNews[0:2]:
                        thirdUrl = "https:"+thirdNews
                    else:
                        thirdUrl=thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Music"
                            subtopic = "Hip Hop"
                            name = "xxlmagHipHop"
                            iconUrl = "https://townsquare.media/site/812/files/2017/10/xxl-trimmed-spacing.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"class": "entry"}).find("div", {"class": "pod-content"})
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








        def rapupHipHop():
            try:
                url = "https://www.rap-up.com/category/news/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("main", {"id": "music-hub"}).find("section", {"id": "stories"}).find_all("div", {"class": "inner"})[0].find("a").get("href")
                    secondNews = soup.find("main", {"id": "music-hub"}).find("section", {"id": "stories"}).find_all("div", {"class": "inner"})[1].find("a").get("href")
                    thirdNews = soup.find("main", {"id": "music-hub"}).find("section", {"id": "stories"}).find_all("div", {"class": "inner"})[2].find("a").get("href")

                    url = "https://www.rap-up.com"
                    firstUrl=firstNews
                    secondUrl=secondNews
                    thirdUrl=thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Music"
                            subtopic = "Hip Hop"
                            name = "rapupHipHop"
                            iconUrl = "https://pbs.twimg.com/profile_images/1270742698278785029/CxbBCQ-7_400x400.jpg"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("main", {"id": "post-single"}).find("section", {"id": "story"}).find("div",{"class":"content stickem-container"})
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




        hipHopDx()
        theSource()
        pitchforkHipHop()
        xxlmagHipHop()
        rapupHipHop()






    def country():
        def cmtCountry():
            try:
                url = "http://www.cmt.com/news/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"id": "content"}).find("div", {"id": "main"}).find_all("div", {"class": "content"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"id": "content"}).find("div", {"id": "main"}).find_all("div", {"class": "content"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"id": "content"}).find("div", {"id": "main"}).find_all("div", {"class": "content"})[2].find("a").get("href")

                    url = "http://www.cmt.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Music"
                            subtopic = "Country"
                            name = "cmtCountry"
                            iconUrl = "https://seeklogo.com/images/C/cmt-country-music-television-logo-A17712C67C-seeklogo.com.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"id": "main"}).find("section", {"class": "entry-content"})
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







        def tasteOfCountry():
            try:
                url = "https://tasteofcountry.com/category/country-music-news/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"class": "main-content"}).find("div", {"class": "blogroll-inner clearfix"}).find_all("article")[0].find("a").get("href")
                    secondNews = soup.find("div", {"class": "main-content"}).find("div", {"class": "blogroll-inner clearfix"}).find_all("article")[1].find("a").get("href")
                    thirdNews = soup.find("div", {"class": "main-content"}).find("div", {"class": "blogroll-inner clearfix"}).find_all("article")[2].find("a").get("href")

                    url = "https://tasteofcountry.com"
                    if "//" in firstNews[0:2]:
                        firstUrl = "https:" + firstNews
                    else:
                        firstUrl = firstNews
                    if "//" in secondNews[0:2]:
                        secondUrl = "https:" + secondNews
                    else:
                        secondUrl = secondNews
                    if "//" in thirdNews[0:2]:
                        thirdUrl = "https:" + thirdNews
                    else:
                        thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Music"
                            subtopic = "Country"
                            name = "tasteOfCountry"
                            iconUrl = "https://pbs.twimg.com/profile_images/656499940806385664/yHeprouf.jpg"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"class": "main-content"}).find("div", {"class": "entry"}).find("div", {"class": "pod-content"})
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





        def peopleCountry():
            try:
                url = "https://people.com/country/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("main", {"class": "container-full-width"}).find("div", {"class": "category-page-list-content"}).find_all("div", {"class": "category-page-item"})[0].find("a").get("href")
                    secondNews = soup.find("main", {"class": "container-full-width"}).find("div", {"class": "category-page-list-content"}).find_all("div", {"class": "category-page-item"})[1].find("a").get("href")
                    thirdNews = soup.find("main", {"class": "container-full-width"}).find("div", {"class": "category-page-list-content"}).find_all("div", {"class": "category-page-item"})[2].find("a").get("href")

                    url = "https://people.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Music"
                            subtopic = "Country"
                            name = "peopleCountry"
                            iconUrl = "https://people.com/img/misc/og-default.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"class": "container-full-width"}).find("div", {"class": "articleContainer"}).find_all("div",{"class":"articleContainer__content"})
                                for c in newsTags:
                                    for i in c.find_all('img'):
                                        i.replace_with("")
                                    for i in c.find_all('iframe'):
                                        i.replace_with("")
                                    for i in c.find_all('aside'):
                                        i.replace_with("")
                                    for i in c.find_all('h2'):
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
                                    for x in c.find_all("div",{"class":"paragraph"}):
                                        for e in x.find_all("p"):
                                            newsContent = newsContent + " " + e.get_text().strip()
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





        def countryNow():
            try:
                url = "https://www.countrynow.com/news/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("section", {"id": "content"}).find("div", {"class": "grids"}).find("div", {"class": "grids entries list-layout"}).find_all("div", {"class": "post-item-inner"})[0].find("a").get("href")
                    secondNews = soup.find("section", {"id": "content"}).find("div", {"class": "grids"}).find("div", {"class": "grids entries list-layout"}).find_all("div", {"class": "post-item-inner"})[1].find("a").get("href")
                    thirdNews = soup.find("section", {"id": "content"}).find("div", {"class": "grids"}).find("div", {"class": "grids entries list-layout"}).find_all("div", {"class": "post-item-inner"})[2].find("a").get("href")

                    url = "https://www.countrynow.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Music"
                            subtopic = "Country"
                            name = "countryNow"
                            iconUrl = "https://countrynow.com/wp-content/uploads/2019/04/logo.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("main", {"id": "content"}).find("div", {"class": "grids"}).find("article", {"class": "clearfix single-box entry-content"})
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







        def theBoot():
            try:
                url = "https://theboot.com/category/country-news/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"class": "main-content"}).find("section", {"id": "carbonwidget-taxonomy-1"}).find("div", {"class": "blogroll-inner clearfix"}).find_all("article")[0].find("a").get("href")
                    secondNews = soup.find("div", {"class": "main-content"}).find("section", {"id": "carbonwidget-taxonomy-1"}).find("div", {"class": "blogroll-inner clearfix"}).find_all("article")[1].find("a").get("href")
                    thirdNews = soup.find("div", {"class": "main-content"}).find("section", {"id": "carbonwidget-taxonomy-1"}).find("div", {"class": "blogroll-inner clearfix"}).find_all("article")[2].find("a").get("href")

                    url = "https://theboot.com"
                    if "//" in firstNews[0:2]:
                        firstUrl = "https:" + firstNews
                    else:
                        firstUrl = firstNews
                    if "//" in secondNews[0:2]:
                        secondUrl = "https:" + secondNews
                    else:
                        secondUrl = secondNews
                    if "//" in thirdNews[0:2]:
                        thirdUrl = "https:" + thirdNews
                    else:
                        thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Music"
                            subtopic = "Country"
                            name = "theBootCountry"
                            iconUrl = "https://townsquare.media/site/623/files/2017/10/theboot-logo.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"class": "main-content"}).find("div", {"class": "entry"}).find("div", {"class": "content-wrap"}).find("div", {"class": "pod-content"})
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




        cmtCountry()
        tasteOfCountry()
        peopleCountry()
        countryNow()
        theBoot()





    def jazz():
        def jazzTimes():
            try:
                url = "https://jazztimes.com/news/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"id": "content"}).find("main", {"id": "main"}).find("div", {"class": "o-layout o-layout--equal-height"}).find_all("div", {"class": "o-layout__item"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"id": "content"}).find("main", {"id": "main"}).find("div", {"class": "o-layout o-layout--equal-height"}).find_all("div", {"class": "o-layout__item"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"id": "content"}).find("main", {"id": "main"}).find("div", {"class": "o-layout o-layout--equal-height"}).find_all("div", {"class": "o-layout__item"})[2].find("a").get("href")

                    url = "https://jazztimes.com"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Music"
                            subtopic = "Jazz"
                            name = "jazzTimes"
                            iconUrl = "https://pbs.twimg.com/profile_images/1009167791377641474/Y6Lk_s2i_400x400.jpg"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("main", {"id": "main"}).find("div", {"class": "entry-content-wrapper"}).find("div", {"class": "entry-content"})
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






        def allAboutJazz():
            try:
                url = "https://news.allaboutjazz.com"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("section", {"id": "content"}).find_all("div", {"itemprop": "itemListElement"})[0].find("div",{"class":"panel-body"}).find("a").get("href")
                    secondNews = soup.find("section", {"id": "content"}).find_all("div", {"itemprop": "itemListElement"})[1].find("div",{"class":"panel-body"}).find("a").get("href")
                    thirdNews = soup.find("section", {"id": "content"}).find_all("div", {"itemprop": "itemListElement"})[2].find("div",{"class":"panel-body"}).find("a").get("href")

                    url = "https://news.allaboutjazz.com"
                    firstUrl = url+firstNews
                    secondUrl = url+secondNews
                    thirdUrl = url+thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Music"
                            subtopic = "Jazz"
                            name = "allAboutJazz"
                            iconUrl = "https://upload.wikimedia.org/wikipedia/en/3/3f/All-about-jazz-logo.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"itemprop": "articleBody"}).find("div", {"itemprop": "text"})
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
                                newsContent = newsContent + " " + newsTags.get_text().strip()
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




        def pitchforkJazz():
            try:
                url = "https://pitchfork.com/news/?genre=jazz"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"id": "news-page"}).find_all("div", {"class": "article-details"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"id": "news-page"}).find_all("div", {"class": "article-details"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"id": "news-page"}).find_all("div", {"class": "article-details"})[2].find("a").get("href")

                    url = "https://pitchfork.com"
                    firstUrl = url + firstNews
                    secondUrl = url + secondNews
                    thirdUrl = url + thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Music"
                            subtopic = "Jazz"
                            name = "pitchforkJazz"
                            iconUrl = "https://cdn.pitchfork.com/assets/misc/hp-og-image.jpg"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"class": "article__chunks"}).find("div", {"class": "grid-layout__content"})
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






        def nprJazz():
            try:
                url = "https://www.npr.org/music/genres/jazz/"
                websiteRequest = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("section", {"id": "main-section"}).find("div", {"id": "overflow"}).find_all("div", {"class": "item-info"})[0].find("h2",{"class":"title"}).find("a").get("href")
                    secondNews = soup.find("section", {"id": "main-section"}).find("div", {"id": "overflow"}).find_all("div", {"class": "item-info"})[1].find("h2",{"class":"title"}).find("a").get("href")
                    thirdNews =soup.find("section", {"id": "main-section"}).find("div", {"id": "overflow"}).find_all("div", {"class": "item-info"})[2].find("h2",{"class":"title"}).find("a").get("href")

                    url = "https://www.npr.org"
                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Music"
                            subtopic = "Jazz"
                            name = "nprJazz"
                            iconUrl = "https://media.npr.org/chrome_svg/npr-logo.svg"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("article", {"class": "story"}).find("div", {"id": "storytext"})
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




        jazzTimes()
        allAboutJazz()
        pitchforkJazz()
        nprJazz()







    electronicMusic()
    rock()
    blues()
    hipHop()
    country()
    jazz()





