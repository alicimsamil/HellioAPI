
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
                            for i in newsTags.find_all('div', attrs={'class': 'c-listiclePrecap ampHide shortcode'}):
                                i.replace_with("")

                            for new in newsTags.find_all('div',{'class':'row'}):
                                if a==3:
                                    for i in new.find("div",{"class":"col-12"}).find("article",{"id":"article-body"}).find("div",{"class":"col-7 article-main-body row"}).find_all('p'):
                                        newsContent = newsContent + " " + i.text.strip()
                                a=a+1
                            print(newsContent.strip())

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
                            try:
                                newsContent = ""
                                newsTags = soup.find("section", {"class": "content-wrapper"}).find("div",{"id": "article-body"})

                                for i in newsTags.find_all('div', attrs={'class': 'see-more'}):
                                    i.replace_with("")

                                for i in newsTags.find_all('a', attrs={'class': 'view-deal button'}):
                                    i.replace_with("")

                                for new in newsTags.find_all('p'):
                                    newsContent=newsContent+" "+new.get_text().strip()

                                print(newsContent.strip())
                            except:
                                try:
                                    newsContent = ""
                                    newsTags = soup.find("div", {"id": "main"}).find("article", {
                                        "class": "page-content-onecol flex-1 live-article"}).find("div", {
                                        "id": "live-feed-multipage"}).find("div", {"id": "article-body"})

                                    for i in newsTags.find_all('figure'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('time'):
                                        i.replace_with("")
                                    for i in newsTags.find_all('div', attrs={'class': 'ad-unit'}):
                                        i.replace_with("")

                                    for new in newsTags.find_all('div', attrs={'class': 'wcp-item-content'}):
                                        newsContent = newsContent + " " + new.get_text().strip()

                                    print(newsContent.strip())

                                except:
                                    print("Error!" + Exception)

                        except:
                            print("Error!")
                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!"+Exception)


        def pocketLint():
            try:
                url = "https://www.pocket-lint.com/phones/news"
                websiteRequest = requests.get(url, timeout=30 , headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    a=0
                    for i in soup.find("div",{"id":"container"}).find("div",{"id":"hub"}).find("div",{"class":"content"}).find("div",{"class":"articles"}).find_all('div',{'class':'article'}):
                        if a==0:
                            firstNews = i.find("a").get("href")
                        elif a==1:
                            secondNews = i.find("a").get("href")
                        elif a==2:
                            thirdNews = i.find("a").get("href")

                        a=a+1

                    url = "https://www.pocket-lint.com"
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
                            newsTags = soup.find("div", {"id": "container"}).find("div",{"class": "text-content"})
                            a = 0
                            for i in newsTags.find_all('div', attrs={'class': 'has-attribution'}):
                                i.replace_with("")

                            for i in newsTags.find_all('div', attrs={'class': 'squirrel_intelligent_widget'}):
                                i.replace_with("")

                            for i in newsTags.find_all('div', attrs={'id': 'hub'}):
                                i.replace_with("")

                            for i in newsTags.find_all('div', attrs={'class': 'ttp_byline'}):
                                i.replace_with("")

                            for i in newsTags.find_all('picture'):
                                i.replace_with("")

                            for new in newsTags.find_all('p'):
                                newsContent=newsContent+" "+new.get_text().strip()

                            print(newsContent.strip())

                        except:
                            print("Error!"+Exception)

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!"+Exception)





        def gadgets360():
            try:
                url = "https://gadgets.ndtv.com/mobiles/news"
                websiteRequest = requests.get(url, timeout=30 , headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    a=0
                    for i in soup.find("div",{"class":"row white_bg"}).find("div",{"class":"content_section"}).find("div",{"class":"content_block row margin_b30 ncgv"}).find("div",{"class":"story_list row margin_b20"}).find("ul").find_all('li'):
                        if a==0:
                            firstNews = i.find("div",{"class":"caption_box"}).find("a").get("href")
                        elif a==1:
                            secondNews = i.find("div",{"class":"caption_box"}).find("a").get("href")
                        elif a==2:
                            thirdNews = i.find("div",{"class":"caption_box"}).find("a").get("href")

                        a=a+1

                    url = "https://gadgets.ndtv.com/mobiles/news"
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
                            newsTags = soup.find("div", {"class": "rhs clearfix"}).find("div",{"class": "content_section"}).find("div",{"class": "content_block white_bg row margin_b30"}).find("div",{"class": "story_detail row margin_b20"}).find("div",{"id": "center_content_div"}).find("div",{"class": "content_text row description"})

                            for i in newsTags.find_all('div', attrs={'class': 'embed-container'}):
                                i.replace_with("")

                            for i in newsTags.find_all('iframe', attrs={'allow': 'encrypted-media'}):
                                i.replace_with("")

                            for i in newsTags.find_all('div', attrs={'id': 'adslotNativeVideo'}):
                                i.replace_with("")
                            for i in newsTags.find_all('div', attrs={'class': 'alsoseewgt oneline clearfix'}):
                                i.replace_with("")


                            for new in newsTags.find_all('p'):
                                newsContent=newsContent+" "+new.get_text().strip()

                            print(newsContent.strip())

                        except:
                            print("Error!"+Exception)

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!"+Exception)


        def techTimes():
            try:
                url = "https://www.techtimes.com/smartphone"
                websiteRequest = requests.get(url, timeout=30 , headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")

                    firstNews = soup.find("div", {"class": "archive"}).find("article", {"class": "lg"}).find("div", {"class": "row"}).find("div", {"class": "col-sm-6"}).find("h2").find("a").get("href")


                    a=0
                    for i in soup.find("div", {"class": "archive"}).find_all('div', attrs={'class': 'row'}):

                        if a==1:
                            b=0
                            for c in i.find("div", {"class": "col-md-8"}).find("ul",{"class":"list"}).find_all('li'):
                                if b==0:
                                    secondNews = c.find("article",{"class":"clearfix"}).find("h4").find("a").get("href")
                                elif b==1:
                                    thirdNews = c.find("article",{"class":"clearfix"}).find("h4").find("a").get("href")
                                b=b+1

                        a=a+1

                    url = "https://www.techtimes.com"
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
                            newsTags = soup.find("div", {"class": "archive"}).find("div",{"class": "row"}).find("div",{"class": "article-body"})

                            for i in newsTags.find_all('div'):
                                i.replace_with("")
                            for i in newsTags.find_all('script',{'type':'text/javascript'}):
                                i.replace_with("")
                            for i in newsTags.find_all('script'):
                                i.replace_with("")
                            for i in newsTags.find_all('strong'):
                                i.replace_with("")
                            for i in newsTags.find_all('center'):
                                i.replace_with("")
                            for new in newsTags.find_all('p'):
                                newsContent=newsContent+" "+new.get_text().strip()

                            print(newsContent.strip())

                        except:
                            print("Error!"+Exception)

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!"+Exception)


        cNET()
        techRadar()
        pocketLint()
        gadgets360()
        techTimes()


    def iot():
        def iotNow():
            try:
                url = "https://www.iot-now.com/news/"
                websiteRequest = requests.get(url, timeout=30 , headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")

                    a=0
                    for i in soup.find("main", {"id": "main"}).find("div",{"class": "row"}).find("div",{"class": "col-md-12 col-lg-8"}).find("div",{"class": "row categories__wrapper"}).find_all('div', attrs={'class': 'col-md-6 mb-4'}):

                        if a==0:
                            firstNews = i.find("div", {"class": "category__post"}).find("h2", {"class": "category__title"}).find("a").get("href")
                        elif a==1:
                            secondNews = i.find("div", {"class": "category__post"}).find("h2", {"class": "category__title"}).find("a").get("href")
                        elif a==2:
                            thirdNews = i.find("div", {"class": "category__post"}).find("h2", {"class": "category__title"}).find("a").get("href")
                        a=a+1

                    url = "https://www.iot-now.com"

                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=30,headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            print(newsImage)
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            print(newsTitle)
                            newsContent = ""
                            newsTags = soup.find("div", {"class": "builder-html"}).find("main", {"class": "container"}).find("div",{"class": "col-md-12 col-lg-8"}).find("div",{"class": "article__content"})


                            for new in newsTags.find_all():
                                newsContent=newsContent+" "+new.get_text().strip()

                            print(newsContent.strip())

                        except:
                            print("Error!"+Exception)

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!"+Exception)



        def iotBusinessNews():
            try:
                url = "https://iotbusinessnews.com"
                websiteRequest = requests.get(url, timeout=30 , headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")

                    a=0
                    for i in soup.find("div", {"class": "main-content"}).find("section",{"class": "section news-box nb1 cat_4,5,6,7,8,9,10,11,16,564,1465,2192,2519,2600"}).find("ul").find_all('li'):

                        if a==0:
                            firstNews = i.find("figure", {"class": "post-thumbnail"}).find("a").get("href")
                        elif a==1:
                            secondNews = i.find("figure", {"class": "post-thumbnail"}).find("a").get("href")
                        elif a==2:
                            thirdNews = i.find("figure", {"class": "post-thumbnail"}).find("a").get("href")
                        a=a+1

                    url = "https://iotbusinessnews.com"

                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=30,headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            print(newsImage)
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            print(newsTitle)
                            newsContent = ""
                            newsTags = soup.find("div", {"class": "main-content"}).find("div", {"class": "site-content page-wrap"}).find("div",{"class": "entry-content clearfix"})

                            for i in newsTags.find_all('img'):
                                i.replace_with("")
                            for i in newsTags.find_all('noscript'):
                                i.replace_with("")
                            for i in newsTags.find_all('div'):
                                i.replace_with("")
                            for new in newsTags.find_all("p"):
                                newsContent=newsContent+" "+new.get_text().strip()

                            print(newsContent.strip())

                        except:
                            print("Error!"+Exception)

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!"+Exception)





        def futureIot():
            try:
                url = "https://futureiot.tech/?s="
                websiteRequest = requests.get(url, timeout=30 , headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")

                    a=0
                    for i in soup.find("div", {"class": "jeg_viewport"}).find("div", {"class": "jeg_main"}).find("div",{"class": "container"}).find("div",{"class": "jeg_cat_content row"}).find("div",{"class": "jeg_sidebar left jeg_sticky_sidebar col-sm-4"}).find("div",{"class": "widget widget_recent_entries"}).find("ul").find_all('li'):

                        if a==0:
                            firstNews = i.find("a").get("href")
                        elif a==1:
                            secondNews = i.find("a").get("href")
                        elif a==2:
                            thirdNews = i.find("a").get("href")
                        a=a+1

                    url = "https://futureiot.tech"

                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=30,headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            print(newsImage)
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            print(newsTitle)
                            newsContent = ""
                            newsTags = soup.find("div", {"class": "jeg_viewport"}).find("div", {"class": "post-wrapper"}).find("div",{"class": "row"}).find("div",{"class": "entry-content with-share"}).find("div",{"class": "content-inner"})

                            for i in newsTags.find_all('img'):
                                i.replace_with("")
                            for i in newsTags.find_all('div'):
                                i.replace_with("")
                            for new in newsTags.find_all("p"):
                                newsContent=newsContent+" "+new.get_text().strip()

                            print(newsContent.strip())

                        except:
                            print("Error!"+Exception)

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!"+Exception)



        iotNow()
        iotBusinessNews()
        futureIot()



    def AI():
        def mit():
            try:
                url = "https://news.mit.edu/topic/artificial-intelligence2"
                websiteRequest = requests.get(url, timeout=30 , headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")

                    a=0
                    for i in soup.find("main", {"class": "site-main"}).find("div",{"class": "page--section"}).find("div",{"class": "page--section--inner"}).find("div",{"id": "block-mit-content"}).find("div",{"class": "page-term--views--list"}).find_all('div', attrs={'class': 'page-term--views--list-item'}):

                        if a==0:
                            firstNews = i.find("article", {"class": "term-page--news-article--item"}).find("div", {"class": "term-page--news-article--item--cover-image"}).find("a").get("href")
                        elif a==1:
                            secondNews = i.find("article", {"class": "term-page--news-article--item"}).find("div", {"class": "term-page--news-article--item--cover-image"}).find("a").get("href")
                        elif a==2:
                            thirdNews = i.find("article", {"class": "term-page--news-article--item"}).find("div", {"class": "term-page--news-article--item--cover-image"}).find("a").get("href")
                        a=a+1

                    url = "https://news.mit.edu"

                    firstUrl = url + firstNews
                    secondUrl = url + secondNews
                    thirdUrl = url + thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=30,headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            print(newsImage)
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            print(newsTitle)
                            newsContent = ""
                            newsTags = soup.find("main", {"class": "site-main"}).find("div", {"class": "page--section"}).find("div",{"id": "block-mit-content"}).find("div",{"class": "news-article--content"}).find("div",{"class": "news-article--content--body"}).find("div",{"class": "news-article--content--body--inner"})

                            for i in newsTags.find_all('iframe'):
                                i.replace_with("")
                            for i in newsTags.find_all('div',attrs={'class':'news-article--inline-video'}):
                                i.replace_with("")
                            for new in newsTags.find_all('div',attrs={'class':'paragraph paragraph--type--content-block-text paragraph--view-mode--default'}):
                                for x in new.find_all('p'):
                                    newsContent=newsContent+" "+x.get_text().strip()

                            print(newsContent.strip())

                        except:
                            print("Error!"+Exception)

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!"+Exception)


        def wiredAI():
            try:
                url = "https://www.wired.com/tag/artificial-intelligence/"
                websiteRequest = requests.get(url, timeout=30 , headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")

                    a=0
                    for i in soup.find("div", {"class": "page-loader-component"}).find("div",{"class": "tag-main"}).find("div",{"class": "primary-grid-component"}).find("div",{"class": "cards-component"}).find_all('div', attrs={'class': 'cards-component__row'}):

                        try:
                            if a==0:
                                c=0
                                for x in i.find_all('ul'):
                                    if c==0:
                                        firstNews = x.find("li").find("a").get("href")
                                    elif c == 1:
                                        secondNews = x.find("li").find("a").get("href")
                                    c=c+1
                            elif a==1:
                                c = 0
                                for x in i.find_all('ul'):
                                    if c == 0:
                                        thirdNews = x.find("li").find("a").get("href")
                                    c = c+1

                            a=a+1
                        except:
                            try:
                                if a == 0:
                                    c = 0
                                    for x in i.find_all('ul'):
                                        if c == 0:
                                            firstNews = x.find("li").find("a").get("href")

                                        c = c + 1
                                elif a == 1:
                                    c = 0
                                    for x in i.find_all('ul'):
                                        if c == 0:
                                            secondNews = x.find("li").find("a").get("href")
                                        elif c == 1:
                                            thirdNews = x.find("li").find("a").get("href")
                                        c = c + 1

                                a = a + 1
                            except:
                                print("Error!")


                    url = "https://www.wired.com"

                    firstUrl = url + firstNews
                    secondUrl = url + secondNews
                    thirdUrl = url + thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=30,headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            print(newsImage)
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            print(newsTitle)
                            newsContent = ""
                            newsTags = soup.find("main", {"id": "main-content"}).find("div", {"class": "content-background"})


                            for i in newsTags.find_all('div',attrs={'class':'sc-hRUHzT dOqdZq callout--has-top-border'}):
                                i.replace_with("")
                            for x in newsTags.find_all('p'):
                                    newsContent=newsContent+" "+x.get_text().strip()

                            print(newsContent.strip())

                        except:
                            print("Error!"+Exception)

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!"+Exception)








        mit()
        wiredAI()





    mobileDevices()
    iot()
    AI()



technology()
