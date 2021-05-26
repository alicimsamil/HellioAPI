
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

                            for new in newsTags.find_all('div',{'class':'row'}):
                                if a==3:
                                    for i in new.find("div",{"class":"col-12"}).find("article",{"id":"article-body"}).find("div",{"class":"col-7 article-main-body row"}).find_all('p'):
                                        newsContent = newsContent + " " + i.text
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
                                    newsContent=newsContent+" "+new.get_text()

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
                                        newsContent = newsContent + " " + new.get_text()

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
                                newsContent=newsContent+" "+new.get_text()

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
                                newsContent=newsContent+" "+new.get_text()

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
                                newsContent=newsContent+" "+new.get_text()

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






    mobileDevices()



technology()
