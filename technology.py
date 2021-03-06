import databaseTransactions
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
                            topic = "Technology"
                            subtopic = "Mobile Devices"
                            name = "cNETMobile"
                            iconUrl = "https://cdn.iconscout.com/icon/free/png-512/cnet-283245.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
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
                            topic = "Technology"
                            subtopic = "Mobile Devices"
                            name = "techRadarMobile"
                            iconUrl = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/TechRadar_logo.svg/1200px-TechRadar_logo.svg.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            try:
                                newsContent = ""
                                newsTags = soup.find("section", {"class": "content-wrapper"}).find("div",{"id": "article-body"})

                                for i in newsTags.find_all('div', attrs={'class': 'see-more'}):
                                    i.replace_with("")

                                for i in newsTags.find_all('a', attrs={'class': 'view-deal button'}):
                                    i.replace_with("")

                                for new in newsTags.find_all('p'):
                                    newsContent=newsContent+" "+new.get_text().strip()

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
                            topic = "Technology"
                            subtopic = "Mobile Devices"
                            name = "pocketLintMobile"
                            iconUrl = "https://assets-global.website-files.com/5ca6f1703977261264f0212e/5dc976f041ec9e06774029ed_pocketlint.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
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

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")





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
                            topic = "Technology"
                            subtopic = "Mobile Devices"
                            name = "gadgets360Mobile"
                            iconUrl = "https://images.metadata.sky.com/pd-image/91746c63-9c7d-4f64-b7b4-bf7148eef072/16-9"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
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

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")


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
                            topic = "Technology"
                            subtopic = "Mobile Devices"
                            name = "techTimesMobile"
                            iconUrl = "https://owlcam.com/wp-content/uploads/2019/09/tech-times.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
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

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")


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
                            topic = "Technology"
                            subtopic = "Iot"
                            name = "iotNow"
                            iconUrl = "https://cdn.asp.events/CLIENT_CL_EE_E92EC48A_9F42_8E1E_7106D5CAFEEF513B/sites/Project-Alex/media/libraries/media/Iotnow_500x200.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            newsTags = soup.find("div", {"class": "builder-html"}).find("main", {"class": "container"}).find("div",{"class": "col-md-12 col-lg-8"}).find("div",{"class": "article__content"})
                            for new in newsTags.find_all("p"):
                                newsContent=newsContent+" "+new.get_text().strip()

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")



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
                            topic = "Technology"
                            subtopic = "Iot"
                            name = "iotBusinessNews"
                            iconUrl = "https://pbs.twimg.com/profile_images/1248601787147280384/viJxcTHE.jpg"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
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

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")





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
                            topic = "Technology"
                            subtopic = "Iot"
                            name = "futureIot"
                            iconUrl = "https://pbs.twimg.com/profile_images/1141217277959761922/-_W98lS9.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            newsTags = soup.find("div", {"class": "jeg_viewport"}).find("div", {"class": "post-wrapper"}).find("div",{"class": "row"}).find("div",{"class": "entry-content with-share"}).find("div",{"class": "content-inner"})

                            for i in newsTags.find_all('img'):
                                i.replace_with("")
                            for i in newsTags.find_all('div'):
                                i.replace_with("")
                            for new in newsTags.find_all("p"):
                                newsContent=newsContent+" "+new.get_text().strip()

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")



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
                            topic = "Technology"
                            subtopic = "AI"
                            name = "mitAI"
                            iconUrl = "https://yt3.ggpht.com/ytc/AAUvwnjQD4IfLhQni2KsfwvW8MbpZSxeKUgfOadv0EWVoA=s900-c-k-c0x00ffffff-no-rj"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            newsTags = soup.find("main", {"class": "site-main"}).find("div", {"class": "page--section"}).find("div",{"id": "block-mit-content"}).find("div",{"class": "news-article--content"}).find("div",{"class": "news-article--content--body"}).find("div",{"class": "news-article--content--body--inner"})

                            for i in newsTags.find_all('iframe'):
                                i.replace_with("")
                            for i in newsTags.find_all('div',attrs={'class':'news-article--inline-video'}):
                                i.replace_with("")
                            for new in newsTags.find_all('div',attrs={'class':'paragraph paragraph--type--content-block-text paragraph--view-mode--default'}):
                                for x in new.find_all('p'):
                                    newsContent=newsContent+" "+x.get_text().strip()

                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                        except:
                            print("Error!")

                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)

            except:
                print("Error!")


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
                            topic = "Technology"
                            subtopic = "AI"
                            name = "wiredAI"
                            iconUrl = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Wired_logo.svg/1200px-Wired_logo.svg.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("main", {"id": "main-content"}).find("div", {"class": "content-background"})
                                for i in newsTags.find_all('div',attrs={'class':'sc-hRUHzT dOqdZq callout--has-top-border'}):
                                    i.replace_with("")
                                for x in newsTags.find_all('p'):
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




        def theNextWeb():
            try:
                url = "https://thenextweb.com/neural"
                websiteRequest = requests.get(url, timeout=30 , headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")

                    firstNews=soup.find("main",{"class":"c-split__main"}).find("article",{"class":"c-topArticles__article o-grid__col"}).find("a").get("href")
                    a=0
                    for i in soup.find("main",{"class":"c-split__main"}).find_all('div',{'class':'c-card t-white w-full'}):
                        if a==0:
                            secondNews=i.find("a").get("href")
                        elif a==1:
                            thirdNews=i.find("a").get("href")
                        a=a+1


                    url = "https://thenextweb.com"

                    firstUrl = url + firstNews
                    secondUrl = url + secondNews
                    thirdUrl = url + thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=30,headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Technology"
                            subtopic = "AI"
                            name = "theNextWebAI"
                            iconUrl = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1eJ3yboAArCUm-JjezpoKu8XDISu5r-_UcpOiFJGxe3mdw3Iqlvjfl4v7Z11Ow6w9jy0&usqp=CAU"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""

                            try:
                                newsTags = soup.find("main", {"class": "c-split__main"}).find("div", {"class": "c-article__main"}).find("div", {"class": "c-richText c-richText--large"})
                                for i in newsTags.find_all('div',attrs={'class':'corona-wrapper'}):
                                    i.replace_with("")
                                for i in newsTags.find_all('p',attrs={'class':'yt-responsive-wrapper'}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={'class':'wp-block-image'}):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('h3',attrs={'class':'alsoTaggedIn'}):
                                    i.replace_with("")

                                for x in newsTags.find_all('p'):
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






        def theVergeAI():
            try:
                url = "https://www.theverge.com/ai-artificial-intelligence"
                websiteRequest = requests.get(url, timeout=60, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")

                    a=0
                    for i in soup.find("main",{"id":"content"}).find("div",{"class":"c-compact-river"}).find_all('div',{'class':'c-compact-river__entry'}):
                        if a==0:
                            firstNews=i.find("a").get("href")
                        elif a==1:
                            secondNews=i.find("a").get("href")
                        elif a==2:
                            thirdNews=i.find("a").get("href")
                        a=a+1


                    url = "https://www.theverge.com"

                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60,headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Technology"
                            subtopic = "AI"
                            name = "theVergeAI"
                            iconUrl = "https://cdn.vox-cdn.com/uploads/chorus_asset/file/9672633/VergeOG.0_1200x627.0.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""

                            try:
                                newsTags = soup.find("main", {"id": "content"}).find("div", {"class": "c-entry-content"})
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={'class':'article-body-banner banner'}):
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



        mit()
        wiredAI()
        theNextWeb()
        theVergeAI()


    def computing():
        def digitalTrends():
            try:
                url = "https://www.digitaltrends.com/computing/"
                websiteRequest = requests.get(url, timeout=60, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")

                    a=0
                    for i in soup.find("div",{"class":"b-page__wrapper"}).find_all('a',{'class':'b-synopsis-stack__hot'}):
                        if a==0:
                            firstNews=i.get("href")
                        elif a==1:
                            secondNews=i.get("href")
                        elif a==2:
                            thirdNews=i.get("href")
                        a=a+1


                    url = "https://www.digitaltrends.com"

                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60,headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Technology"
                            subtopic = "Computing"
                            name = "digitalTrends"
                            iconUrl = "https://cdn.dtcn.com/dtdesign/2019/iphone-11-amp-review/assets/DT-logo-RGB-horizontal_4x.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""

                            try:
                                newsTags = soup.find("div", {"class": "b-page__inner"}).find("article", {"itemprop": "articleBody"})
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div'):
                                    i.replace_with("")
                                for i in newsTags.find_all('ul'):
                                    i.replace_with("")
                                for i in newsTags.find_all('h4'):
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



        def techRadarComputing():
            try:
                url = "https://www.techradar.com/news/computing"
                websiteRequest = requests.get(url, timeout=60, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")

                    firstNews= soup.find("div",{"id":"main"}).find("div",{"class":"listingResults"}).find("div",{"class":"listingResult small result1"}).find("a").get("href")
                    secondNews = soup.find("div",{"id":"main"}).find("div",{"class":"listingResults"}).find("div",{"class":"listingResult small result2"}).find("a").get("href")
                    thirdNews = soup.find("div",{"id":"main"}).find("div",{"class":"listingResults"}).find("div",{"class":"listingResult small result3"}).find("a").get("href")

                    url = "https://www.techradar.com"

                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60,headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Technology"
                            subtopic = "Computing"
                            name = "techRadarComputing"
                            iconUrl = "https://assets-jpcust.jwpsrv.com/watermarks/0AT1nZQJ.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""

                            try:
                                newsTags = soup.find("div", {"id": "article-body"})
                                for i in newsTags.find_all('aside'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
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



        def cnetComputing():
            try:
                url = "https://www.cnet.com/topics/computers/"
                websiteRequest = requests.get(url, timeout=60, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")

                    a = 0
                    for i in soup.find("div", {"class": "container"}).find("div", {"class": "row"}).find("div", {
                        "class": "col-8"}).find("section", {"class": "listing"}).find_all('div',attrs={'class': 'row asset'}):
                        if a == 0:
                            firstNews = i.find("div", {"class": "col-6 assetBody"}).find("a").get("href")
                        elif a == 1:
                            secondNews = i.find("div", {"class": "col-6 assetBody"}).find("a").get("href")
                        elif a == 2:
                            thirdNews = i.find("div", {"class": "col-6 assetBody"}).find("a").get("href")
                        a = a + 1
                    url = "https://www.cnet.com"
                    firstUrl = url + firstNews
                    secondUrl = url + secondNews
                    thirdUrl = url + thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=30)
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Technology"
                            subtopic = "Computing"
                            name = "cnetComputing"
                            iconUrl = "https://cdn.iconscout.com/icon/free/png-512/cnet-283245.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"class": "contentWrap"}).find("div",{"class": "container"})
                                a = 0

                                for i in newsTags.find_all('figure', attrs={'section': 'shortcodeImage'}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div', attrs={'class': 'newsletter-subscribe-form desktop -inline'}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={'class': 'c-listiclePrecap ampHide shortcode'}):
                                    i.replace_with("")

                                for new in newsTags.find_all('div', {'class': 'row'}):
                                    if a == 3:
                                        for i in new.find("div", {"class": "col-12"}).find("article",{"id": "article-body"}).find("div", {"class": "col-7 article-main-body row"}).find_all('p'):
                                            newsContent = newsContent + " " + i.text.strip()
                                    a = a + 1
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





        def tomsHardware():
            try:
                url = "https://www.tomshardware.com"
                websiteRequest = requests.get(url, timeout=60, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")

                    firstNews = soup.find("div", {"id": "content"}).find_all("div", attrs={"class": "mainCarousel curatedCarousel"})[1].find("div", {"id": "Item1"}).find("a").get("href")
                    secondNews = soup.find("div", {"id": "content"}).find_all("div", attrs={"class": "mainCarousel curatedCarousel"})[1].find("div", {"id": "Item2"}).find("a").get("href")
                    thirdNews = soup.find("div", {"id": "content"}).find_all("div", attrs={"class": "mainCarousel curatedCarousel"})[1].find("div", {"id": "Item3"}).find("a").get("href")

                    url = "https://www.tomshardware.com"

                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=30)
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Technology"
                            subtopic = "Computing"
                            name = "tomsHardware"
                            iconUrl = "https://cdn.knoji.com/images/logo/tomshardwarecom.jpg"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("article", {"class": "news-article"}).find("section", {"class": "content-wrapper"}).find("div", {"id": "article-body"})


                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div'):
                                    i.replace_with("")
                                for i in newsTags.find_all('br'):
                                    i.replace_with("")

                                for new in newsTags.find_all('p'):
                                    newsContent = newsContent + " " + new.text.strip()

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


        def computerworld():
            try:
                url = "https://www.computerworld.com"
                websiteRequest = requests.get(url, timeout=60, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"class": "page-wrapper"}).find("section", {"role": "main"}).find("div", {"class": "homepage-top-stories"}).find("div", {"class": "item item-1 three"}).find("a").get("href")
                    secondNews = soup.find("div", {"class": "page-wrapper"}).find("section", {"role": "main"}).find("div", {"class": "homepage-top-stories"}).find("div", {"class": "item item-2 three"}).find("a").get("href")
                    thirdNews = soup.find("div", {"class": "page-wrapper"}).find("section", {"role": "main"}).find("div", {"class": "homepage-top-stories"}).find("div", {"class": "item item-3 three"}).find("a").get("href")

                    url = "https://www.computerworld.com"

                    firstUrl = url+firstNews
                    secondUrl = url+secondNews
                    thirdUrl = url+thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=30)
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Technology"
                            subtopic = "Computing"
                            name = "computerworld"
                            iconUrl = "https://mobysign.com/mobysign/wp-content/uploads/2016/07/computerworld.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"class": "page-wrapper"}).find("section", {"role": "main"}).find("section", {"class": "bodee"}).find("div", {"itemprop": "articleBody"})

                                for i in newsTags.find_all('aside'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"id":"sponsoredfakesidebardiv"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"id":"editorialfakesidebardiv"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"class":"end-note"}):
                                    i.replace_with("")

                                for new in newsTags.find_all('p'):
                                    newsContent = newsContent + " " + new.text.strip()

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




        digitalTrends()
        techRadarComputing()
        cnetComputing()
        tomsHardware()
        computerworld()



    def robotics():
        def robohub():
            try:
                url = "https://robohub.org"
                websiteRequest = requests.get(url, timeout=60, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")

                    firstNews = soup.find("div",{"id":"main"}).find("div",{"class":"inner clearfix"}).find("div",{"class":"columnv mainw"}).find_all("div",attrs={"class":"roundedge cpxframex"})[0].find("a").get("href")
                    secondNews = soup.find("div",{"id":"main"}).find("div",{"class":"inner clearfix"}).find("div",{"class":"columnv mainw"}).find_all("div",attrs={"class":"roundedge cpxframex"})[1].find("a").get("href")
                    thirdNews = soup.find("div",{"id":"main"}).find("div",{"class":"inner clearfix"}).find("div",{"class":"columnv mainw"}).find_all("div",attrs={"class":"roundedge cpxframex"})[2].find("a").get("href")

                    url = "https://robohub.org"

                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60)
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Technology"
                            subtopic = "Robotics"
                            name = "robohub"
                            iconUrl = "https://robohub.org/wp-content/themes/rbh_vf/images/printlogo.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("head").find("title").get_text().strip()
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"class": "page-wrap"}).find("div", {"id": "main"}).find("div", {"class": "inner clearfix"}).find("div", {"class": "columnv mainw"}).find("div", {"class": "intcontent"})


                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('strong'):
                                    i.replace_with("")
                                for i in newsTags.find_all('style'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"class":"maintext ftauthdiv desaturate_bak"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")

                                for new in newsTags.find_all('p'):
                                    newsContent = newsContent + " " + new.text.strip()

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


        def automate():
            try:
                url = "https://www.automate.org/news"
                websiteRequest = requests.get(url, timeout=60, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("main", {"role": "main"}).find("div", {"class": "inner"}).find("div", {"class": "gridcol nine"}).find_all("div", attrs={"class": "item informational tc-robotics"})[0].find("a").get("href")
                    secondNews = soup.find("main", {"role": "main"}).find("div", {"class": "inner"}).find("div", {"class": "gridcol nine"}).find_all("div", attrs={"class": "item informational tc-robotics"})[1].find("a").get("href")
                    thirdNews = soup.find("main", {"role": "main"}).find("div", {"class": "inner"}).find("div", {"class": "gridcol nine"}).find_all("div", attrs={"class": "item informational tc-robotics"})[2].find("a").get("href")

                    url = "https://www.automate.org"

                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=30)
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Technology"
                            subtopic = "Robotics"
                            name = "automate"
                            iconUrl = "https://www.wileyindustrynews.com/sites/default/files/styles/gallery/public/2021-03/a3_logo.jpg?h=bdcf3624&itok=vuMwHO7o"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            if newsImage=="":
                                newsImage="https://www.automate.org/favicon.ico"
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:
                                newsTags = soup.find("div", {"id": "wrapper"}).find("main", {"role": "main"}).find("div", {"class": "gridcol nine"}).find("div", {"class": "articleContent"})

                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('a'):
                                    i.replace_with("")
                                for new in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + new.text.strip()

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





        def theRobotReport():
            try:
                url = "https://www.therobotreport.com"
                websiteRequest = requests.get(url, timeout=60, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"class": "site-inner"}).find("div", {"class": "row"}).find_all("div", attrs={"class": "header-slide"})[0].find("a").get("href")
                    secondNews = soup.find("div", {"class": "site-inner"}).find("div", {"class": "row"}).find_all("div", attrs={"class": "header-slide"})[1].find("a").get("href")
                    thirdNews = soup.find("div", {"class": "site-inner"}).find("div", {"class": "row"}).find_all("div", attrs={"class": "header-slide"})[2].find("a").get("href")
                    url = "https://www.therobotreport.com"

                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=30, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Technology"
                            subtopic = "Robotics"
                            name = "theRobotReport"
                            iconUrl = "https://sponsorlogo.informamarkets.com/sites/default/files/The-Robot-Report-422x292.jpg"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:

                                newsTags = soup.find("div", {"class": "site-inner"}).find("main", {"class": "content"}).find("div", {"class": "entry-content"})
                                for i in newsTags.find_all('table'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div'):
                                    i.replace_with("")
                                for new in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + new.text.strip()
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



        def techxplore():
            try:
                url = "https://phys.org/technology-news/robotics/"
                websiteRequest = requests.get(url, timeout=60, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("main", {"class": "pt-2"}).find("div", {"class": "col-12"}).find_all("article", attrs={"class": "sorted-article"})[0].find("a").get("href")
                    secondNews = soup.find("main", {"class": "pt-2"}).find("div", {"class": "col-12"}).find_all("article", attrs={"class": "sorted-article"})[1].find("a").get("href")
                    thirdNews = soup.find("main", {"class": "pt-2"}).find("div", {"class": "col-12"}).find_all("article", attrs={"class": "sorted-article"})[2].find("a").get("href")
                    url = "https://phys.org"

                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=30, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Technology"
                            subtopic = "Robotics"
                            name = "physRobotics"
                            iconUrl = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRoUiTEXIJ78QFU6YRh1CF8x0gNrX5rlin4BAulPXPs30M09gtABAc169NMazKMqC4LXPc&usqp=CAU"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""
                            try:

                                newsTags = soup.find("section", {"class": "article"}).find("article", {"class": "news-article"}).find("div", {"class": "mt-4 text-low-up text-regular article-main"})
                                for i in newsTags.find_all('table'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div'):
                                    i.replace_with("")
                                for i in newsTags.find_all('p',attrs={"class":"article-byline text-low"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('p',attrs={"class":"article-main__note mt-4"}):
                                    i.replace_with("")
                                for new in newsTags.find_all("p"):
                                    newsContent = newsContent + " " + new.text.strip()

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


        robohub()
        automate()
        theRobotReport()
        techxplore()






    def cyberSecurity():
        def theHackerNews():
            try:
                url = "https://thehackernews.com"
                websiteRequest = requests.get(url, timeout=60, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")

                    firstNews= soup.find("main",{"class":"main clear"}).find("div",{"class":"main-left-right clear"}).find("div",{"class":"blog-posts clear"}).find_all("div",attrs={"class":"body-post clear"})[0].find("a").get("href")
                    secondNews = soup.find("main",{"class":"main clear"}).find("div",{"class":"main-left-right clear"}).find("div",{"class":"blog-posts clear"}).find_all("div",attrs={"class":"body-post clear"})[1].find("a").get("href")
                    thirdNews = soup.find("main",{"class":"main clear"}).find("div",{"class":"main-left-right clear"}).find("div",{"class":"blog-posts clear"}).find_all("div",attrs={"class":"body-post clear"})[2].find("a").get("href")

                    url = "https://thehackernews.com"

                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60,headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Technology"
                            subtopic = "Cyber Security"
                            name = "theHackerNews"
                            iconUrl = "https://thehackernews.com/images/-AaptImXE5Y4/WzjvqBS8HtI/AAAAAAAAxSs/BcCIwpWJszILkuEbDfKZhxQJwOAD7qV6ACLcBGAs/s728-e100/the-hacker-news.jpg"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""

                            try:
                                newsTags = soup.find("div", {"class": "widget Blog"}).find("div", {"class": "post"}).find("div", {"id": "articlebody"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div'):
                                    i.replace_with("")
                                for i in newsTags.find_all('br'):
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


        def tripWire():
            try:
                url = "https://www.tripwire.com/state-of-security/"
                websiteRequest = requests.get(url, timeout=60, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")

                    firstNews= soup.find("section",{"id":"content"}).find("section",{"class":"col-left body-content list-posts"}).find_all("div",attrs={"class":"post-image"})[0].find("a").get("href")
                    secondNews = soup.find("section",{"id":"content"}).find("section",{"class":"col-left body-content list-posts"}).find_all("div",attrs={"class":"post-image"})[1].find("a").get("href")
                    thirdNews = soup.find("section",{"id":"content"}).find("section",{"class":"col-left body-content list-posts"}).find_all("div",attrs={"class":"post-image"})[2].find("a").get("href")

                    url = "https://www.tripwire.com"

                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60,headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Technology"
                            subtopic = "Cyber Security"
                            name = "tripWire"
                            iconUrl = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRANxSlbPj3u8uc1KPELXrmIZScs4nLzfiwrresiALgAcATaVLZpuQBXsdP-drHHUUc8CM&usqp=CAU"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""

                            try:
                                newsTags = soup.find("section", {"id": "page"}).find("section", {"class": "col-main col-main"}).find("section", {"class": "body-content"}).find("span", {"class": "entry-content post-content"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div'):
                                    i.replace_with("")
                                for i in newsTags.find_all('br'):
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





        def darkReading():
            try:
                url = "https://www.darkreading.com"
                websiteRequest = requests.get(url, timeout=60, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")

                    firstNews= soup.find("div",{"class":"column-full"}).find("section",{"class":"column left-main"}).find("section",{"id":"left-column"}).find("div",{"id":"left-column-inner"}).find_all("header",attrs={"class":"strong medium"})[0].find("a").get("href")
                    secondNews = soup.find("div",{"class":"column-full"}).find("section",{"class":"column left-main"}).find("section",{"id":"left-column"}).find("div",{"id":"left-column-inner"}).find_all("header",attrs={"class":"strong medium"})[1].find("a").get("href")
                    thirdNews = soup.find("div",{"class":"column-full"}).find("section",{"class":"column left-main"}).find("section",{"id":"left-column"}).find("div",{"id":"left-column-inner"}).find_all("header",attrs={"class":"strong medium"})[2].find("a").get("href")

                    url = "https://www.darkreading.com"

                    firstUrl = url+firstNews
                    secondUrl = url+secondNews
                    thirdUrl = url+thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60,headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Technology"
                            subtopic = "Cyber Security"
                            name = "darkReading"
                            iconUrl = "https://twimgs.com/nojitter/darkreading/dr-logo.jpg"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""

                            try:
                                newsTags = soup.find("div", {"id": "thedoctop"}).find("div", {"id": "article-main"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('table'):
                                    i.replace_with("")
                                for i in newsTags.find_all('header'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div'):
                                    i.replace_with("")
                                for i in newsTags.find_all('br'):
                                    i.replace_with("")
                                for i in newsTags.find_all('strong'):
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



        def threatPost():
            try:
                url = "https://threatpost.com"
                websiteRequest = requests.get(url, timeout=60, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews= soup.find("div",{"class":"c-main"}).find("div",{"id":"latest_news_container"}).find_all("div",attrs={"class":"o-row"})[0].find("a").get("href")
                    secondNews = soup.find("div",{"class":"c-main"}).find("div",{"id":"latest_news_container"}).find_all("div",attrs={"class":"o-row"})[1].find("a").get("href")
                    thirdNews = soup.find("div",{"class":"c-main"}).find("div",{"id":"latest_news_container"}).find_all("div",attrs={"class":"o-row"})[2].find("a").get("href")

                    url = "https://threatpost.com"

                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60,headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Technology"
                            subtopic = "Cyber Security"
                            name = "threatPost"
                            iconUrl = "https://media.threatpost.com/wp-content/uploads/sites/103/2018/07/02133237/THREAT-e1530305072468.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""

                            try:
                                newsTags = soup.find("div", {"class": "c-main"}).find("div", {"class": "c-article__main"}).find("div", {"class": "c-article__content js-reading-content"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('table'):
                                    i.replace_with("")
                                for i in newsTags.find_all('header'):
                                    i.replace_with("")
                                for i in newsTags.find_all('footer'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div'):
                                    i.replace_with("")
                                for i in newsTags.find_all('br'):
                                    i.replace_with("")
                                for i in newsTags.find_all('strong'):
                                    i.replace_with("")
                                for i in newsTags.find_all('a'):
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





        def hackRead():
            try:
                url = "https://www.hackread.com"
                websiteRequest = requests.get(url, timeout=60, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews= soup.find("div",{"id":"main"}).find("div",{"class":"articles relative clearfix"}).find_all("div",attrs={"class":"col-sm-4"})[0].find("a").get("href")
                    secondNews = soup.find("div",{"id":"main"}).find("div",{"class":"articles relative clearfix"}).find_all("div",attrs={"class":"col-sm-4"})[1].find("a").get("href")
                    thirdNews = soup.find("div",{"id":"main"}).find("div",{"class":"articles relative clearfix"}).find_all("div",attrs={"class":"col-sm-4"})[2].find("a").get("href")

                    url = "https://www.hackread.com"

                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60,headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Technology"
                            subtopic = "Cyber Security"
                            name = "hackRead"
                            iconUrl = "https://pbs.twimg.com/profile_images/1076928978794016769/paG0wbRw_400x400.jpg"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""

                            try:
                                newsTags = soup.find("div", {"id": "page-outer-wrap"}).find("div", {"id": "content-container"}).find("div", {"class": "main article"}).find("div", {"class": "col col-sm-8"}).find("div", {"class": "article-post-content clearfix"})
                                for i in newsTags.find_all('img'):
                                    i.replace_with("")
                                for i in newsTags.find_all('figure'):
                                    i.replace_with("")
                                for i in newsTags.find_all('header'):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div'):
                                    i.replace_with("")
                                for i in newsTags.find_all('aside'):
                                    i.replace_with("")
                                for i in newsTags.find_all('em'):
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







        theHackerNews()
        tripWire()
        darkReading()
        threatPost()
        hackRead()



    def blockChain():
        def wiredBlockChain():
            try:
                url = "https://www.wired.com/tag/blockchain/"
                websiteRequest = requests.get(url, timeout=60, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews= soup.find("div",{"class":"tag-main"}).find("div",{"class":"cards-component"}).find_all("ul")[0].find("a").get("href")
                    secondNews = soup.find("div",{"class":"tag-main"}).find("div",{"class":"cards-component"}).find_all("ul")[1].find("a").get("href")
                    thirdNews = soup.find("div",{"class":"tag-main"}).find("div",{"class":"cards-component"}).find_all("ul")[2].find("a").get("href")

                    url = "https://www.wired.com"

                    firstUrl = url+firstNews
                    secondUrl = url+secondNews
                    thirdUrl = url+thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60,headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Technology"
                            subtopic = "Block Chain"
                            name = "wiredBlockChain"
                            iconUrl = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Wired_logo.svg/1200px-Wired_logo.svg.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""

                            try:
                                newsTags = soup.find("main", {"id": "main-content"}).find("div", {"class": "content-background"}).find("div", {"class": "article__chunks"})
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
                                for i in newsTags.find_all('aside'):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"data-testid":"GenericCallout"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"role":"heading"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"class":"newsletter-subscribe-form newsletter-subscribe-form--slim"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('ul',attrs={"class":"paywall"}):
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


        def cnbcBlockChain():
            try:
                url = "https://www.cnbc.com/blockchain/"
                websiteRequest = requests.get(url, timeout=60, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews= soup.find("div",{"id":"MainContentContainer"}).find("div",{"class":"PageBuilder-pageWrapper"}).find("div",{"class":"SectionWrapper-content"}).find_all("div",attrs={"data-test":"Column"})[0].find("a").get("href")
                    secondNews = soup.find("div",{"id":"MainContentContainer"}).find("div",{"class":"PageBuilder-pageWrapper"}).find("div",{"class":"SectionWrapper-content"}).find_all("div",attrs={"data-test":"Column"})[1].find("a").get("href")
                    thirdNews = soup.find("div",{"id":"MainContentContainer"}).find("div",{"class":"PageBuilder-pageWrapper"}).find("div",{"class":"SectionWrapper-content"}).find_all("div",attrs={"data-test":"Column"})[2].find("a").get("href")

                    url = "https://www.cnbc.com"

                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60,headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Technology"
                            subtopic = "Block Chain"
                            name = "cnbcBlockChain"
                            iconUrl = "https://upload.wikimedia.org/wikipedia/en/thumb/d/d7/CNBC-e.svg/1200px-CNBC-e.svg.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""

                            try:
                                newsTags = soup.find("div", {"role": "main"}).find("div", {"data-module": "ArticleBody"}).find_all("div", attrs={"class": "group"})
                                for x in newsTags:
                                    for i in x.find_all('img'):
                                        i.replace_with("")
                                    for i in x.find_all('figure'):
                                        i.replace_with("")
                                    for i in x.find_all('header'):
                                        i.replace_with("")
                                    for i in x.find_all('iframe'):
                                        i.replace_with("")
                                    for i in x.find_all('hr'):
                                        i.replace_with("")
                                    for i in x.find_all('aside'):
                                        i.replace_with("")
                                    for i in x.find_all('div',attrs={"id":"MakeItRegularArticle-RelatedContent-1"}):
                                        i.replace_with("")
                                    for i in x.find_all('div',attrs={"class":"newsletter-subscribe-form newsletter-subscribe-form--slim"}):
                                        i.replace_with("")
                                    for i in x.find_all('em'):
                                        i.replace_with("")
                                    for c in x.find_all("p"):
                                        newsContent=newsContent+" "+c.get_text().strip()
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




        def forbesBlockChain():
            try:
                url = "https://www.forbes.com/crypto-blockchain/"
                websiteRequest = requests.get(url, timeout=60, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews= soup.find("section",{"id":"row-2"}).find("div",{"class":"chansec-stream__content"}).find("div",{"class":"chansec-stream__items"}).find_all("div",attrs={"class":"stream-item__text"})[0].find("a").get("href")
                    secondNews = soup.find("section",{"id":"row-2"}).find("div",{"class":"chansec-stream__content"}).find("div",{"class":"chansec-stream__items"}).find_all("div",attrs={"class":"stream-item__text"})[1].find("a").get("href")
                    thirdNews = soup.find("section",{"id":"row-2"}).find("div",{"class":"chansec-stream__content"}).find("div",{"class":"chansec-stream__items"}).find_all("div",attrs={"class":"stream-item__text"})[2].find("a").get("href")

                    url = "https://www.forbes.com"

                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60,headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Technology"
                            subtopic = "Block Chain"
                            name = "forbesBlockChain"
                            iconUrl = "https://1000logos.net/wp-content/uploads/2021/05/Forbes-logo.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""

                            try:
                                newsTags = soup.find("main", {"class": "main-content--body"}).find("div", {"class": "body-container"}).find("div", {"class": "article-body"})
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
                                for i in newsTags.find_all('a',attrs={"rel":"noopener noreferrer"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"class":"embed-base embedly-align"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"class":"recirc-module seo"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"class":"vestpocket"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"class":"article-sharing"}):
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



        def coindeskBlockChain():
            try:
                url = "https://www.coindesk.com/category/tech"
                websiteRequest = requests.get(url, timeout=60, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews= soup.find("main").find("div",{"class":"container"}).find("section",{"class":"featured-hub-content v3up"}).find_all("div",attrs={"class":"text-group"})[0].find("a").get("href")
                    secondNews = soup.find("main").find("div",{"class":"container"}).find("section",{"class":"featured-hub-content v3up"}).find_all("div",attrs={"class":"text-group"})[1].find("a").get("href")
                    thirdNews = soup.find("main").find("div",{"class":"container"}).find("section",{"class":"featured-hub-content v3up"}).find_all("div",attrs={"class":"text-group"})[2].find("a").get("href")

                    url = "https://www.coindesk.com"

                    firstUrl = url+firstNews
                    secondUrl = url+secondNews
                    thirdUrl = url+thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60,headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Technology"
                            subtopic = "Block Chain"
                            name = "coindeskBlockChain"
                            iconUrl = "https://s2-recruiting.cdn.greenhouse.io/external_greenhouse_job_boards/logos/400/839/300/original/coindesk-4C_2x.png?1570032520"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""

                            try:
                                newsTags = soup.find("main").find("section", {"class": "article news global-content"}).find("div", {"class": "article-module article"}).find("div", {"class": "article-body-wrapper"})
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
                                for i in newsTags.find_all('div',attrs={"class":"read-more-widget"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"class":"article-disclosure"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"class":"tags"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"class":"end"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"class":"read-more-widget"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"class":"newsletter-module-wrapper"}):
                                    i.replace_with("")
                                for x in newsTags.find_all("p",{"class":"text"}):
                                    newsContent=newsContent+" "+x.get_text().strip()
                            except:
                                try:
                                    newsTags = soup.find("div",{"class": "article-body-wrapper"}).find("section",{"class": "article-body"})
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
                                    for i in newsTags.find_all('div', attrs={"class": "read-more-widget"}):
                                        i.replace_with("")
                                    for i in newsTags.find_all('div', attrs={"class": "article-disclosure"}):
                                        i.replace_with("")
                                    for i in newsTags.find_all('div', attrs={"class": "tags"}):
                                        i.replace_with("")
                                    for i in newsTags.find_all('div', attrs={"class": "end"}):
                                        i.replace_with("")
                                    for i in newsTags.find_all('div', attrs={"class": "read-more-widget"}):
                                        i.replace_with("")
                                    for i in newsTags.find_all('div', attrs={"class": "newsletter-module-wrapper"}):
                                        i.replace_with("")
                                    for x in newsTags.find_all("p",{"class":"text"}):
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



        def bitcoinBlockChain():
            try:
                url = "https://news.bitcoin.com"
                websiteRequest = requests.get(url, timeout=60, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")

                    firstNews= soup.find("div", {"id": "td-outer-wrap"}).find("div", {"class": "vc_row wpb_row td-pb-row"}).find("div", {"class": "story story--huge"}).find("a").get("href")
                    secondNews = soup.find("div",{"id":"td-outer-wrap"}).find("div",{"class":"vc_row wpb_row td-pb-row"}).find_all("div",attrs={"class":"story story--medium"})[0].find("a").get("href")
                    thirdNews = soup.find("div",{"id":"td-outer-wrap"}).find("div",{"class":"vc_row wpb_row td-pb-row"}).find_all("div",attrs={"class":"story story--medium"})[1].find("a").get("href")

                    url = "https://news.bitcoin.com"

                    firstUrl = firstNews
                    secondUrl = secondNews
                    thirdUrl = thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=60,headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "Technology"
                            subtopic = "Block Chain"
                            name = "bitcoinBlockChain"
                            iconUrl = "https://blokzin.github.io/assets/img/resources/bitcoin-com.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            newsContent = ""

                            try:
                                newsTags = soup.find("div", {"id": "td-outer-wrap"}).find("main", {"class": "article full-grid"}).find("article", {"class": "article__body"})
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
                                for i in newsTags.find_all('div',attrs={"class":"read-more-widget"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"class":"article__body__tags-related"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('p',attrs={"class":"images_credits"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"class":"disclaimer"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"class":"switch_container"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"class":"snippet_container"}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={"class":"alm-disqus"}):
                                    i.replace_with("")
                                for x in newsTags.find_all():
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





        wiredBlockChain()
        cnbcBlockChain()
        forbesBlockChain()
        coindeskBlockChain()
        bitcoinBlockChain()







    mobileDevices()
    iot()
    AI()
    computing()
    robotics()
    cyberSecurity()
    blockChain()



