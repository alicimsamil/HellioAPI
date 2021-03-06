import databaseTransactions
import requests
from bs4 import BeautifulSoup

def news():
    def bbc():
        try:
            try:
                url="https://www.bbc.com/news"
                websiteRequest=requests.get(url,timeout=30)

                if websiteRequest.status_code!=200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent=websiteRequest.content
                    soup=BeautifulSoup(websiteContent,"html.parser")
                    firstNews=soup.find("div",{"data-entityid":"container-top-stories#1"}).find("a",{"class":"gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold nw-o-link-split__anchor"}).get("href")
                    secondNews=soup.find("div",{"data-entityid":"container-top-stories#2"}).find("a",{"class":"gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor"}).get("href")
                    thirdNews=soup.find("div",{"data-entityid":"container-top-stories#3"}).find("a",{"class":"gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor"}).get("href")
                    url = "https://www.bbc.com"
                    firstUrl=url+firstNews
                    secondUrl = url + secondNews
                    thirdUrl = url + thirdNews


                    def getContent(url):
                        try:
                            request=requests.get(url,timeout=30)
                            content=request.content
                            soup=BeautifulSoup(content,"html.parser")
                            topic = "News"
                            subtopic = "News"
                            name="bbcNews"
                            iconUrl="https://cdn.iconscout.com/icon/free/png-256/bbc-3-555283.png"
                            pageurl=url
                            newsImage = soup.find("meta",{"property":"og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")

                            try:
                                newsTags= soup.find("article",{"class":"ssrcss-5h7eao-ArticleWrapper e1nh2i2l6"})
                                newsContent=""
                                for i in newsTags.find_all('div', attrs={'class': 'ssrcss-18mjolk-ComponentWrapper e1xue1i87'}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div', attrs={'class': 'ssrcss-1lp2cw-ComponentWrapper-SocialEmbedComponentWrapper e1xue1i86'}):
                                    i.replace_with("")
                                for new in newsTags.find_all('div', attrs={'data-component': 'text-block'}):
                                    newsContent = newsContent+ " " + new.get_text().strip()

                            except:
                                try:
                                    newsTags = soup.find("article", {"class": "ssrcss-1qrrcog-StyledMediaItem elwf6ac4"}).find("div", {"class": "ssrcss-1p48mn5-StyledSummary elwf6ac2"}).find("div", {"class": "ssrcss-18snukc-RichTextContainer e5tfeyi1"})
                                    newsContent = ""
                                    for i in newsTags.find_all('div', attrs={'class': 'ssrcss-18mjolk-ComponentWrapper e1xue1i87'}):
                                        i.replace_with("")
                                    for i in newsTags.find_all('div', attrs={'class': 'ssrcss-1lp2cw-ComponentWrapper-SocialEmbedComponentWrapper e1xue1i86'}):
                                        i.replace_with("")
                                    for new in newsTags.find_all('p'):
                                        newsContent = newsContent+ " " + new.get_text()

                                except:
                                    try:
                                        newsTags = soup.find("div", {"class": "gel-layout__item gel-2/3@l gel-2/4@xxl"}).find("div", {"class": "lx-o-panel__item"}).find("section",{"class":"lx-commentary lx-commentary--robo-text gs-t-news"}).find("div",{"class":"lx-commentary__stream"}).find("article",{"class":"qa-post gs-u-pb-alt+ lx-stream-post gs-u-pt-alt+ gs-u-align-left"}).find("div",{"class":"gs-u-mb+ gel-body-copy qa-post-body"}).find("div",{"class":"lx-stream-post-body"})
                                        newsContent = ""
                                        for i in newsTags.find_all('div', attrs={'class': 'ssrcss-18mjolk-ComponentWrapper e1xue1i87'}):
                                            i.replace_with("")
                                        for i in newsTags.find_all('div', attrs={'class': 'ssrcss-1lp2cw-ComponentWrapper-SocialEmbedComponentWrapper e1xue1i86'}):
                                            i.replace_with("")
                                        for new in newsTags.find_all('p'):
                                            newsContent = newsContent+ " " + new.get_text()


                                    except:
                                        try:
                                            newsTags = soup.find("div",{"class":"gel-layout__item gel-2/3@l gel-3/4@xxl"}).find("div",{"class":"lx-commentary__stream"}).find("ol",{"class":"gs-u-m0 gs-u-p0 lx-stream__feed qa-stream"}).find("li",{"class":"lx-stream__post-container placeholder-animation-finished"}).find("div",{"class":"gs-u-mb+ gel-body-copy qa-post-body"}).find("div",{"class":"lx-stream-post-body"})
                                            newsContent = ""


                                            for i in newsTags.find_all('figure', attrs={'class':'lx-stream-post-body__media-asset lx-media-asset lx-media-asset--image lx-media-asset--landscape gs-u-mb+'}):
                                                i.replace_with("")

                                            for new in newsTags.find_all('p'):
                                                newsContent = newsContent + " " + new.text


                                        except:
                                            try:
                                                newsTags = soup.find("div",{"id": "orb-modules"}).find("div",{"class": "qa-story-body story-body gel-pica gel-10/12@m gel-7/8@l gs-u-ml0@l gs-u-pb++"})

                                                newsContent = ""


                                                for i in newsTags.find_all('ul'):
                                                    i.replace_with("")

                                                for i in newsTags.find_all('span',attrs={'class':'gs-u-display-block story-body__media gs-u-mb-alt+ qa-story-body-media'}):
                                                    i.replace_with("")

                                                for new in newsTags.find_all('p'):
                                                    newsContent = newsContent + " " + new.text


                                            except:
                                                try:
                                                    newsTags = soup.find("div", {"class": "article__container"}).find("article", {"class": "article__body"}).find("div", {"class": "article__body-content"})
                                                    newsContent = ""
                                                    for i in newsTags.find_all('div', attrs={'class': 'article-body-native-ad article-body__body-text'}):
                                                        i.replace_with("")
                                                    for i in newsTags.find_all('div', attrs={'class': 'article-body__image-text article-body__image-text--portrait'}):
                                                        i.replace_with("")
                                                    for i in newsTags.find_all('div', attrs={'class': 'article__end'}):
                                                        i.replace_with("")
                                                    for new in newsTags.find_all('p'):
                                                        newsContent = newsContent + " " + new.get_text()

                                                except:
                                                    try:
                                                        newsTags = soup.find("main", {"id": "main-content"}).find("article", {"class": "ssrcss-1072xwf-ArticleWrapper"})
                                                        newsContent = ""
                                                        for i in newsTags.find_all('div', attrs={'class': 'article-body-native-ad article-body__body-text'}):
                                                            i.replace_with("")
                                                        for i in newsTags.find_all('div', attrs={'class': 'article-body__image-text article-body__image-text--portrait'}):
                                                            i.replace_with("")
                                                        for i in newsTags.find_all('div', attrs={'class': 'article__end'}):
                                                            i.replace_with("")
                                                        for new in newsTags.find_all('div',{"data-component":"text-block"}):
                                                            for a in new.find_all("p"):
                                                                newsContent = newsContent + " " + a.get_text()

                                                    except:
                                                        print("Error!")
                            databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                        except:
                            print("Error!")
                    getContent(firstUrl)
                    getContent(secondUrl)
                    getContent(thirdUrl)


            except:

                url = "https://www.bbc.com/news"
                websiteRequest = requests.get(url, timeout=30)

                if websiteRequest.status_code != 200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent = websiteRequest.content
                    soup = BeautifulSoup(websiteContent, "html.parser")
                    firstNews = soup.find("div", {"data-entityid": "container-top-stories#1"}).find("a", {
                        "class": "gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold nw-o-link-split__anchor"}).get(
                        "href")
                    secondNews = soup.find("div", {"data-entityid": "container-top-stories#2"}).find("a", {
                        "class": "gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor"}).get(
                        "href")
                    thirdNews = soup.find("div", {"data-entityid": "container-top-stories#4"}).find("a", {
                        "class": "gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor"}).get(
                        "href")
                    url = "https://www.bbc.com"
                    firstUrl = url + firstNews
                    secondUrl = url + secondNews
                    thirdUrl = url + thirdNews

                    def getContent(url):
                        try:
                            request = requests.get(url, timeout=30)
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "News"
                            subtopic = "News"
                            name = "bbcNews"
                            iconUrl = "https://cdn.iconscout.com/icon/free/png-256/bbc-3-555283.png"
                            pageurl = url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            try:
                                newsTags = soup.find("article", {"class": "ssrcss-5h7eao-ArticleWrapper e1nh2i2l6"})
                                newsContent = ""
                                for i in newsTags.find_all('div',
                                                           attrs={'class': 'ssrcss-18mjolk-ComponentWrapper e1xue1i87'}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div', attrs={
                                    'class': 'ssrcss-1lp2cw-ComponentWrapper-SocialEmbedComponentWrapper e1xue1i86'}):
                                    i.replace_with("")
                                for new in newsTags.find_all('div', attrs={'data-component': 'text-block'}):
                                    newsContent = newsContent + " " + new.get_text()

                            except:
                                try:
                                    newsTags = soup.find("article",
                                                         {"class": "ssrcss-1qrrcog-StyledMediaItem elwf6ac4"}).find("div", {
                                        "class": "ssrcss-1p48mn5-StyledSummary elwf6ac2"}).find("div", {
                                        "class": "ssrcss-18snukc-RichTextContainer e5tfeyi1"})
                                    newsContent = ""
                                    for i in newsTags.find_all('div', attrs={
                                        'class': 'ssrcss-18mjolk-ComponentWrapper e1xue1i87'}):
                                        i.replace_with("")
                                    for i in newsTags.find_all('div', attrs={
                                        'class': 'ssrcss-1lp2cw-ComponentWrapper-SocialEmbedComponentWrapper e1xue1i86'}):
                                        i.replace_with("")
                                    for new in newsTags.find_all('p'):
                                        newsContent = newsContent + " " + new.get_text()

                                except:
                                    try:
                                        newsTags = soup.find("div",
                                                             {"class": "gel-layout__item gel-2/3@l gel-2/4@xxl"}).find(
                                            "div", {"class": "lx-o-panel__item"}).find("section", {
                                            "class": "lx-commentary lx-commentary--robo-text gs-t-news"}).find("div", {
                                            "class": "lx-commentary__stream"}).find("article", {
                                            "class": "qa-post gs-u-pb-alt+ lx-stream-post gs-u-pt-alt+ gs-u-align-left"}).find(
                                            "div", {"class": "gs-u-mb+ gel-body-copy qa-post-body"}).find("div", {
                                            "class": "lx-stream-post-body"})
                                        newsContent = ""
                                        for i in newsTags.find_all('div', attrs={
                                            'class': 'ssrcss-18mjolk-ComponentWrapper e1xue1i87'}):
                                            i.replace_with("")
                                        for i in newsTags.find_all('div', attrs={
                                            'class': 'ssrcss-1lp2cw-ComponentWrapper-SocialEmbedComponentWrapper e1xue1i86'}):
                                            i.replace_with("")
                                        for new in newsTags.find_all('p'):
                                            newsContent = newsContent + " " + new.get_text()


                                    except:
                                        try:
                                            newsTags = soup.find("div",
                                                                 {"class": "gel-layout__item gel-2/3@l gel-3/4@xxl"}).find(
                                                "div", {"class": "lx-commentary__stream"}).find("ol", {
                                                "class": "gs-u-m0 gs-u-p0 lx-stream__feed qa-stream"}).find("li", {
                                                "class": "lx-stream__post-container placeholder-animation-finished"}).find(
                                                "div", {"class": "gs-u-mb+ gel-body-copy qa-post-body"}).find("div", {
                                                "class": "lx-stream-post-body"})
                                            newsContent = ""

                                            for i in newsTags.find_all('figure', attrs={
                                                'class': 'lx-stream-post-body__media-asset lx-media-asset lx-media-asset--image lx-media-asset--landscape gs-u-mb+'}):
                                                i.replace_with("")

                                            for new in newsTags.find_all('p'):
                                                newsContent = newsContent + " " + new.text


                                        except:
                                            try:
                                                newsTags = soup.find("div", {"id": "orb-modules"}).find("div", {
                                                    "class": "qa-story-body story-body gel-pica gel-10/12@m gel-7/8@l gs-u-ml0@l gs-u-pb++"})

                                                newsContent = ""

                                                for i in newsTags.find_all('ul'):
                                                    i.replace_with("")

                                                for i in newsTags.find_all('span', attrs={
                                                    'class': 'gs-u-display-block story-body__media gs-u-mb-alt+ qa-story-body-media'}):
                                                    i.replace_with("")

                                                for new in newsTags.find_all('p'):
                                                    newsContent = newsContent + " " + new.text


                                            except:
                                                try:
                                                    newsTags = soup.find("div", {"class": "article__container"}).find(
                                                        "article", {"class": "article__body"}).find("div", {
                                                        "class": "article__body-content"})
                                                    newsContent = ""
                                                    for i in newsTags.find_all('div', attrs={
                                                        'class': 'article-body-native-ad article-body__body-text'}):
                                                        i.replace_with("")
                                                    for i in newsTags.find_all('div', attrs={
                                                        'class': 'article-body__image-text article-body__image-text--portrait'}):
                                                        i.replace_with("")
                                                    for i in newsTags.find_all('div', attrs={'class': 'article__end'}):
                                                        i.replace_with("")
                                                    for new in newsTags.find_all('p'):
                                                        newsContent = newsContent + " " + new.get_text()

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



    def aljazeera():
        try:
            url="https://www.aljazeera.com/news/"
            websiteRequest=requests.get(url,timeout=30)

            if websiteRequest.status_code!=200:
                newsImage = "Error"
                newsTitle = "Error"
                newsContent = "Error"
            else:
                websiteContent=websiteRequest.content
                soup=BeautifulSoup(websiteContent,"html.parser")
                firstNews=soup.find("div",{"class":"section-top-grid__col-1"}).find("div",{"class":"gc__content"}).find("div",{"class":"gc__header-wrap"}).find("h3",{"class":"gc__title"}).find("a").get("href")
                secondNews=soup.find("div",{"class":"section-top-grid__col-2"}).find("div",{"class":"gc__content"}).find("div",{"class":"gc__header-wrap"}).find("h3",{"class":"gc__title"}).find("a").get("href")
                a=0
                for i in soup.find("div",{"class":"section-top-grid__col-2"}).find_all('h3',attrs={'class':'gc__title'}):
                    if a==1:
                        thirdNews=i.find("a").get("href")
                    a=a+1

                url = "https://www.aljazeera.com"
                firstUrl=url+firstNews
                secondUrl = url + secondNews
                thirdUrl = url + thirdNews
                def getContent(url):
                    try:
                        request=requests.get(url,timeout=30)
                        content=request.content
                        topic = "News"
                        subtopic = "News"
                        name = "aljazeeraNews"
                        iconUrl = "https://iconape.com/wp-content/png_logo_vector/aljazeera-logo.png"
                        pageurl = url
                        soup=BeautifulSoup(content,"html.parser")
                        newsImage = soup.find("meta",{"property":"og:image"}).get("content")
                        newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                        try:
                            newsTags= soup.find("div",{"class":"wysiwyg wysiwyg--all-content css-az20b6"})
                            newsContent=""
                            for i in newsTags.find_all('div', attrs={'class': 'twitter-tweet twitter-tweet-rendered'}):
                                i.replace_with("")
                            for i in newsTags.find_all('div', attrs={'class': 'article-source'}):
                                i.replace_with("")
                            for i in newsTags.find_all('div', attrs={'class': 'wp-caption aligncenter'}):
                                i.replace_with("")
                            for i in newsTags.find_all('div', attrs={'class': 'more-on'}):
                                i.replace_with("")
                            for i in newsTags.find_all('iframe'):
                                i.replace_with("")
                            for new in newsTags.find_all('p'):
                                newsContent = newsContent+ " " + new.get_text()
                        except:
                            try:

                                newsTags = soup.find("div", {"class": "container__inner css-eaqrp2-Gallery"}).find("div", {"class": "l-col l-col--8--centered"}).find("div", {"class": "gallery-content wysiwyg wysiwyg--all-content css-az20b6"})
                                newsContent = ""
                                for i in newsTags.find_all('div', attrs={'class': 'twitter-tweet twitter-tweet-rendered'}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div', attrs={'class': 'article-source'}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div', attrs={'class': 'wp-caption aligncenter'}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div', attrs={'class': 'more-on'}):
                                    i.replace_with("")
                                for i in newsTags.find_all('iframe'):
                                    i.replace_with("")
                                for new in newsTags.find_all('p'):
                                    newsContent = newsContent+ " " + new.get_text()
                            except:
                                try:
                                    newsTags = soup.find("div",{"id":"root"}).find("div", {"class": "container container--grid container--gallery container--white"}).find("div", {"class": "container__inner css-eaqrp2-Gallery"}).find("div",{"class":"gallery-content wysiwyg wysiwyg--all-content css-az20b6"})
                                    newsContent = ""
                                    for i in newsTags.find_all('div',attrs={'class': 'twitter-tweet twitter-tweet-rendered'}):
                                        i.replace_with("")
                                    for i in newsTags.find_all('div', attrs={'class': 'article-source'}):
                                        i.replace_with("")
                                    for i in newsTags.find_all('div', attrs={'class': 'wp-caption aligncenter'}):
                                        i.replace_with("")
                                    for i in newsTags.find_all('div', attrs={'class': 'more-on'}):
                                        i.replace_with("")
                                    for i in newsTags.find_all('iframe'):
                                        i.replace_with("")
                                    for new in newsTags.find_all('p'):
                                        newsContent = newsContent+ " " + new.get_text()

                                except:
                                    try:
                                        newsTags = soup.find("div", {"id": "root"}).find("header", {"class": "article-header"})
                                        newsContent = ""
                                        for i in newsTags.find_all('div',attrs={'class': 'twitter-tweet twitter-tweet-rendered'}):
                                            i.replace_with("")
                                        for i in newsTags.find_all('div', attrs={'class': 'article-source'}):
                                            i.replace_with("")
                                        for i in newsTags.find_all('div', attrs={'class': 'wp-caption aligncenter'}):
                                            i.replace_with("")
                                        for i in newsTags.find_all('div', attrs={'class': 'more-on'}):
                                            i.replace_with("")
                                        for i in newsTags.find_all('iframe'):
                                            i.replace_with("")
                                        for new in newsTags.find_all('p'):
                                            newsContent = newsContent + " " + new.get_text()
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


    def dwNews():
        try:
            url="https://www.dw.com/en/top-stories/news/s-30701"
            websiteRequest=requests.get(url,timeout=30)

            if websiteRequest.status_code!=200:
                newsImage = "Error"
                newsTitle = "Error"
                newsContent = "Error"
            else:
                websiteContent=websiteRequest.content
                soup=BeautifulSoup(websiteContent,"html.parser")
                b=0
                for i in soup.find("div",{"id":"bodyContent"}).find("div",{"class":"col2 left"}).find_all('div', attrs={'class':'col2 basicTeaser'}):
                    if b==0:
                        firstNews=i.find("div",{"class":"group"}).find("div",{"class":"news"}).find("a").get("href")
                    if b == 1:
                        secondNews = i.find("div",{"class":"group"}).find("div",{"class":"news"}).find("a").get("href")
                    if b == 2:
                        thirdNews = i.find("div",{"class":"group"}).find("div",{"class":"news"}).find("a").get("href")


                    b=b+1

                url = "https://www.dw.com"
                firstUrl=url+firstNews
                secondUrl = url + secondNews
                thirdUrl = url + thirdNews


                def getContent(url):
                    try:
                        request=requests.get(url,timeout=30)
                        content=request.content
                        soup=BeautifulSoup(content,"html.parser")
                        topic = "News"
                        subtopic = "News"
                        newsImage = soup.find("meta",{"property":"og:image"}).get("content")
                        name = "dwNews"
                        iconUrl = "https://upload.wikimedia.org/wikipedia/commons/8/8e/DW_%28TV%29_Logo_2012.png"
                        pageurl = url
                        newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                        newsTags= soup.find("div",{"id":"innerFrame"}).find("div",{"id":"bodyContent"}).find("div",{"class":"col3"}).find("div",{"class":"group"})
                        newsContent=""

                        for i in newsTags.find_all('div',attrs={'class':'col3 right'}):
                            i.replace_with("")

                        for i in newsTags.find_all('div',attrs={'class':'articleWidget'}):
                            i.replace_with("")

                        for i in newsTags.find_all('div',attrs={'class':'picBox fullrechts'}):
                            i.replace_with("")

                        for new in newsTags.find_all('p'):
                            newsContent = newsContent+ " " + new.get_text().strip()

                        databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                    except:
                        print("Error!")
                getContent(firstUrl)
                getContent(secondUrl)
                getContent(thirdUrl)
        except:
            print("Error!")


    def foxNews():
        try:
            url="https://www.foxnews.com"
            websiteRequest=requests.get(url,timeout=30)

            if websiteRequest.status_code!=200:
                newsImage = "Error"
                newsTitle = "Error"
                newsContent = "Error"
            else:
                websiteContent=websiteRequest.content
                soup=BeautifulSoup(websiteContent,"html.parser")
                firstNews=soup.find("div",{"class":"page-content"}).find("main",{"class":"main-content"}).find("article",{"class":"article story-1"}).find("a").get("href")
                secondNews=soup.find("div",{"class":"page-content"}).find("main",{"class":"main-content"}).find("article",{"class":"article story-2"}).find("a").get("href")
                thirdNews=soup.find("div",{"class":"page-content"}).find("main",{"class":"main-content"}).find("article",{"class":"article story-3"}).find("a").get("href")

                firstUrl=firstNews
                secondUrl =secondNews
                thirdUrl =thirdNews

                def getContent(url):
                    try:
                        request=requests.get(url,timeout=30)
                        content=request.content
                        soup=BeautifulSoup(content,"html.parser")
                        topic = "News"
                        subtopic = "News"
                        name = "foxNews"
                        iconUrl = "https://www.logo.wine/a/logo/Fox_News/Fox_News-Logo.wine.svg"
                        pageurl = url
                        newsImage = soup.find("meta",{"property":"og:image"}).get("content")
                        newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                        newsTags= soup.find("div",{"class":"article-body"})
                        newsContent=""

                        for i in newsTags.find_all('div', attrs={'class': 'featured featured-video video-ct'}):
                            i.replace_with("")
                        for i in newsTags.find_all('div', attrs={'class': 'image-ct inline'}):
                            i.replace_with("")
                        for i in newsTags.find_all('div', attrs={'type': 'video'}):
                            i.replace_with("")
                        for new in newsTags.find_all("p"):
                            newsContent = newsContent+ " " + new.get_text()

                        databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                    except:
                        print("Error!")
                getContent(firstUrl)
                getContent(secondUrl)
                getContent(thirdUrl)

        except:
            print("Error!")

    def rtNews():
        try:
            url="https://www.rt.com/news/"
            websiteRequest=requests.get(url,timeout=30)

            if websiteRequest.status_code!=200:
                newsImage = "Error"
                newsTitle = "Error"
                newsContent = "Error"
            else:
                websiteContent=websiteRequest.content
                soup=BeautifulSoup(websiteContent,"html.parser")
                a=0
                o=0


                for i in soup.find("div",{"class":"layout__wrapper"}).find("div",{"class":"columns__column static-66_high-100"}).find_all("div",{"class":"columns__content"}):
                    if a==1:
                        firstNews=i.find("strong",{"class":"card__header card__header_top-news"}).find("a").get("href")
                    elif a==2:

                            for x in i.find_all('li',attrs={'class':'card-rows__item static-two_low-one'}):
                                if o == 0:
                                    secondNews=x.find("strong", {"class": "card__header card__header_vertical_padding-to-low"}).find("a").get("href")
                                elif o==1:
                                    thirdNews=x.find("strong", {"class":"card__header card__header_vertical_padding-to-low"}).find("a").get("href")

                                o=o+1

                    a=a+1

                url="https://www.rt.com"
                firstUrl=url+firstNews
                secondUrl =url+secondNews
                thirdUrl =url+thirdNews


                def getContent(url):
                    try:
                        request=requests.get(url,timeout=30)
                        content=request.content
                        soup=BeautifulSoup(content,"html.parser")
                        topic = "News"
                        subtopic = "News"
                        name = "rtNews"
                        iconUrl = "https://seeklogo.com/images/R/russia-today-logo-3E92F51CD6-seeklogo.com.png"
                        pageurl = url
                        newsImage = soup.find("meta",{"property":"og:image"}).get("content")
                        newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                        newsTags= soup.find("div",{"class":"columns__content"}).find("div",{"class":"article__text text"}).find_all('p')
                        newsContent=""
                        for new in newsTags:
                            newsContent = newsContent+ " " + new.get_text()

                        databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                    except:
                        print("Error!")
                getContent(firstUrl)
                getContent(secondUrl)
                getContent(thirdUrl)

        except:
            print("Error!")



    def independent():
        try:
            try:
                url="https://www.independent.co.uk/news/world"
                websiteRequest=requests.get(url,timeout=30)

                if websiteRequest.status_code!=200:
                    newsImage = "Error"
                    newsTitle = "Error"
                    newsContent = "Error"
                else:
                    websiteContent=websiteRequest.content
                    soup=BeautifulSoup(websiteContent,"html.parser")

                    firstNews=soup.find("div",{"id":"sectionContent"}).find("div",{"class":"sc-oVpqz sc-pQrUA bTgZlJ"}).find("div",{"class":"sc-pbvYO kyuTJY sc-prrfo bqrhRh hero-article article-default"}).find("div",{"class":"sc-pIJmg fgdQdf image-wrap"}).find("a").get("href")
                    a=0
                    for i in soup.find("div",{"id":"sectionContent"}).find("div",{"class":"sc-oVpqz sc-pQrUA bTgZlJ"}).find("div",{"class":"articles"}).find_all('div',attrs={'class':'sc-pRgDJ dibVwu article article-default'}):
                        if a==0:
                            secondNews = i.find("a",{"class":"sc-pRFHb kfZOQo"}).get("href")
                        elif a==1:
                            thirdNews = i.find("a",{"class":"sc-pRFHb kfZOQo"}).get("href")

                        a=a+1

                    url="https://www.independent.co.uk"
                    firstUrl=url+firstNews
                    secondUrl =url+secondNews
                    thirdUrl =url+thirdNews


                def getContent(url):
                    try:
                        request=requests.get(url,timeout=30)
                        content=request.content
                        soup=BeautifulSoup(content,"html.parser")
                        topic = "News"
                        subtopic = "News"
                        name = "independentNews"
                        iconUrl = "https://img1.pnghut.com/0/18/25/C0STPpgPST/united-kingdom-media-daily-telegraph-irish-independent-symbol.jpg"
                        pageurl = url
                        newsImage = soup.find("meta",{"property":"og:image"}).get("content")
                        newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                        try:
                            newsTags= soup.find("div",{"class":"sc-psEMT gwrImx main-wrapper"}).find("div",{"class":"sc-pJgJK daSdlt sc-pZbQk kzfPTw"}).find_all('p')
                            newsContent=""
                            for new in newsTags:
                                newsContent = newsContent+ " " + new.get_text().strip()

                        except:
                            try:
                                newsTags = soup.find("div", {"class": "sc-psEMT sc-pbxEC dKclYu main-wrapper"}).find("div", {"class": "sc-pJgJK daSdlt sc-pZbQk sc-oTAMn kWoGPI"}).find_all('p')
                                newsContent = ""
                                for new in newsTags:
                                    newsContent = newsContent + " " + new.get_text().strip()

                            except:
                                try:
                                    newsTags = soup.find("body", {"id": "body"}).find("div", {"class": "sc-pBjRv sc-qQIyP khJPob main-wrapper "}).find("div",{"id": "frameInner"}).find("div", {"id": "main"}).find_all('p')
                                    newsContent = ""
                                    for new in newsTags:
                                        newsContent = newsContent + " " + new.get_text().strip()

                                except:
                                    try:

                                        newsTags = soup.find("body", {"id": "body"}).find("div", {"class": "sc-pBjRv sc-qQIyP khJPob main-wrapper "}).find("div", {"id": "frameInner"}).find( "div", {"class": "sc-oTAMn ldIexo sc-pjvSN sc-prsLc eLjvEP"}).find_all( 'p')
                                        newsContent = ""
                                        for new in newsTags:
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
                try:
                    url = "https://www.independent.co.uk/news/world"
                    websiteRequest = requests.get(url, timeout=30)

                    if websiteRequest.status_code != 200:
                        newsImage = "Error"
                        newsTitle = "Error"
                        newsContent = "Error"
                    else:
                        websiteContent = websiteRequest.content
                        soup = BeautifulSoup(websiteContent, "html.parser")

                        firstNews = soup.find("div", {"id": "sectionContent"}).find("div", {"class": "sc-pbvYO kyuTJY sc-prrfo bqrhRh hero-article article-default"}).find("div", {"class": "sc-pIJmg fgdQdf image-wrap"}).find("a").get("href")
                        secondNews= soup.find("div", {"id": "sectionContent"}).find("div", {"class": "articles"}).find('div', attrs={'class': 'sc-pRgDJ dibVwu article article-default'}).find("a", {"class": "sc-pRFHb kfZOQo"}).get("href")
                        thirdNews = soup.find("div", {"id": "sectionContent"}).find("div", {"class": "articles"}).find('div', attrs={'class': 'sc-pRgDJ dibVwu article article-default article-premium'}).find("a", {"class": "sc-pRFHb kfZOQo"}).get("href")


                    url = "https://www.independent.co.uk"
                    firstUrl = url + firstNews
                    secondUrl = url + secondNews
                    thirdUrl = url + thirdNews

                    def getContent(url):
                        try:
                            request=requests.get(url,timeout=30)
                            content=request.content
                            soup=BeautifulSoup(content,"html.parser")
                            topic = "News"
                            subtopic = "News"
                            name = "independentNews"
                            iconUrl = "https://img1.pnghut.com/0/18/25/C0STPpgPST/united-kingdom-media-daily-telegraph-irish-independent-symbol.jpg"
                            pageurl = url
                            newsImage = soup.find("meta",{"property":"og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            try:
                                newsTags= soup.find("div",{"class":"sc-psEMT gwrImx main-wrapper"}).find("div",{"class":"sc-pJgJK daSdlt sc-pZbQk kzfPTw"}).find_all('p')
                                newsContent=""
                                for new in newsTags:
                                    newsContent = newsContent+ " " + new.get_text().strip()


                            except:
                                try:
                                    newsTags = soup.find("div", {"class": "sc-psEMT sc-pbxEC dKclYu main-wrapper"}).find("div", {"class": "sc-pJgJK daSdlt sc-pZbQk sc-oTAMn kWoGPI"}).find_all('p')
                                    newsContent = ""
                                    for new in newsTags:
                                        newsContent = newsContent + " " + new.get_text().strip()

                                except:

                                    try:

                                        newsTags = soup.find("body", {"id": "body"}).find("div", {
                                            "class": "sc-pBjRv sc-qQIyP khJPob main-wrapper "}).find("div", {
                                            "id": "frameInner"}).find("div", {"id": "main"}).find_all(
                                            'p')

                                        newsContent = ""

                                        for new in newsTags:
                                            newsContent = newsContent + " " + new.get_text().strip()


                                    except:

                                        try:

                                            newsTags = soup.find("body", {"id": "body"}).find("div", { "class": "sc-pBjRv sc-qQIyP khJPob main-wrapper "}).find("div",{"id": "frameInner"}).find("div", {"class": "sc-oTAMn ldIexo sc-pjvSN sc-prsLc eLjvEP"}).find_all('p')
                                            newsContent = ""
                                            for new in newsTags:
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
                    try:
                        url = "https://www.independent.co.uk/news/world"
                        websiteRequest = requests.get(url, timeout=30)

                        if websiteRequest.status_code != 200:
                            newsImage = "Error"
                            newsTitle = "Error"
                            newsContent = "Error"
                        else:
                            websiteContent = websiteRequest.content
                            soup = BeautifulSoup(websiteContent, "html.parser")


                            firstNews = soup.find("div", {"id": "sectionContent"}).find("div", {"class": "sc-pmjZF sc-oUMOe iQMxTb"}).find("div", {"class": "sc-prrfo ioTEQn sc-qYGWS iaowKX hero-article article-default"}).find("div", {"class": "sc-pZCuu FQldL image-wrap"}).find("a").get("href")
                            a=0
                            for i in soup.find("div", {"id": "sectionContent"}).find("div", {"class": "sc-pmjZF sc-oUMOe iQMxTb"}).find("div", {"class": "articles"}).find_all('div',attrs={'class':'sc-oTzgz byxrrN article article-default'}):
                                if a==0:
                                    secondNews = i.find("div",{"class":"content"}).find("h2").find("a").get("href")
                                elif a==1:
                                    thirdNews = i.find("div",{"class":"content"}).find("h2").find("a").get("href")
                                a=a+1
                        url = "https://www.independent.co.uk"
                        firstUrl = url + firstNews
                        secondUrl = url + secondNews
                        thirdUrl = url + thirdNews

                        def getContent(url):
                            try:
                                request = requests.get(url, timeout=30)
                                content = request.content
                                soup = BeautifulSoup(content, "html.parser")
                                topic = "News"
                                subtopic = "News"
                                name = "independentNews"
                                iconUrl = "https://img1.pnghut.com/0/18/25/C0STPpgPST/united-kingdom-media-daily-telegraph-irish-independent-symbol.jpg"
                                pageurl = url
                                newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                                newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                                try:
                                    newsTags = soup.find("div", {"class": "sc-psEMT gwrImx main-wrapper"}).find("div", {"class": "sc-pJgJK daSdlt sc-pZbQk kzfPTw"}).find_all('p')
                                    newsContent = ""
                                    for new in newsTags:
                                        newsContent = newsContent + " " + new.get_text().strip()


                                except:
                                    try:
                                        newsTags = soup.find("div", {"id": "main"}).find_all('p')
                                        newsContent = ""
                                        for new in newsTags:
                                            newsContent = newsContent + " " + new.get_text().strip()



                                    except:

                                        try:

                                            newsTags = soup.find("body", {"id": "body"}).find("div", {"class": "sc-pBjRv sc-qQIyP khJPob main-wrapper "}).find("div", {"id": "frameInner"}).find("div", {"id": "main"}).find_all('p')
                                            newsContent = ""

                                            for new in newsTags:
                                                newsContent = newsContent + " " + new.get_text().strip()



                                        except:

                                            try:

                                                newsTags = soup.find("body", {"id": "body"}).find("div", {"class": "sc-pBjRv sc-qQIyP khJPob main-wrapper "}).find("div",{"id": "frameInner"}).find("div", {"class": "sc-oTAMn ldIexo sc-pjvSN sc-prsLc eLjvEP"}).find_all('p')
                                                newsContent = ""
                                                for new in newsTags:
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
                        try:
                            url = "https://www.independent.co.uk/news/world"
                            websiteRequest = requests.get(url, timeout=30)

                            if websiteRequest.status_code != 200:
                                newsImage = "Error"
                                newsTitle = "Error"
                                newsContent = "Error"
                            else:
                                websiteContent = websiteRequest.content
                                soup = BeautifulSoup(websiteContent, "html.parser")


                                firstNews = soup.find("div", {"id": "sectionContent"}).find("div", {
                                    "class": "sc-pbvYO kyuTJY sc-prrfo bqrhRh hero-article article-default"}).find("div", {
                                    "class": "sc-pIJmg fgdQdf image-wrap"}).find("a").get("href")
                                secondNews = soup.find("div", {"id": "sectionContent"}).find("div",
                                                                                             {"class": "articles"}).find(
                                    'div', attrs={'class': 'sc-pRgDJ dibVwu article article-default'}).find("a", {
                                    "class": "sc-pRFHb kfZOQo"}).get("href")
                                thirdNews = soup.find("div", {"id": "sectionContent"}).find("div",
                                                                                            {"class": "articles"}).find(
                                    'div', attrs={'class': 'sc-pRgDJ dibVwu article article-default article-premium'}).find(
                                    "a", {"class": "sc-pRFHb kfZOQo"}).get("href")

                            url = "https://www.independent.co.uk"
                            firstUrl = url + firstNews
                            secondUrl = url + secondNews
                            thirdUrl = url + thirdNews

                            def getContent(url):
                                try:
                                    request = requests.get(url, timeout=30)
                                    content = request.content
                                    soup = BeautifulSoup(content, "html.parser")
                                    topic = "News"
                                    subtopic = "News"
                                    name = "independentNews"
                                    iconUrl = "https://img1.pnghut.com/0/18/25/C0STPpgPST/united-kingdom-media-daily-telegraph-irish-independent-symbol.jpg"
                                    pageurl = url
                                    newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                                    newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                                    try:
                                        newsTags = soup.find("div", {"class": "sc-psEMT gwrImx main-wrapper"}).find("div", {
                                            "class": "sc-pJgJK daSdlt sc-pZbQk kzfPTw"}).find_all('p')
                                        newsContent = ""
                                        for new in newsTags:
                                            newsContent = newsContent + " " + new.get_text().strip()


                                    except:
                                        try:
                                            newsTags = soup.find("div",
                                                                 {"class": "sc-psEMT sc-pbxEC dKclYu main-wrapper"}).find(
                                                "div", {"class": "sc-pJgJK daSdlt sc-pZbQk sc-oTAMn kWoGPI"}).find_all('p')
                                            newsContent = ""
                                            for new in newsTags:
                                                newsContent = newsContent + " " + new.get_text().strip()


                                        except:
                                            try:

                                                newsTags = soup.find("body", {"id": "body"}).find("div", {
                                                    "class": "sc-pBjRv sc-qQIyP khJPob main-wrapper "}).find("div", {
                                                    "id": "frameInner"}).find("div", {"id": "main"}).find_all(
                                                    'p')
                                                newsContent = ""
                                                for new in newsTags:
                                                    newsContent = newsContent + " " + new.get_text().strip()


                                            except:
                                                try:

                                                    newsTags = soup.find("body", {"id": "body"}).find("div", {
                                                        "class": "sc-pBjRv sc-qQIyP khJPob main-wrapper "}).find("div",{"id": "frameInner"}).find(
                                                        "div",
                                                        {"class": "sc-oTAMn ldIexo sc-pjvSN sc-prsLc eLjvEP"}).find_all(
                                                        'p')
                                                    newsContent = ""
                                                    for new in newsTags:
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
                            try:
                                url = "https://www.independent.co.uk/news/world"
                                websiteRequest = requests.get(url, timeout=30)

                                if websiteRequest.status_code != 200:
                                    newsImage = "Error"
                                    newsTitle = "Error"
                                    newsContent = "Error"
                                else:
                                    websiteContent = websiteRequest.content
                                    soup = BeautifulSoup(websiteContent, "html.parser")



                                    a = 0
                                    for i in soup.find("div", {"id": "sectionContent"}).find("div", {
                                        "class": "section-body"}).find_all("div", {"class": "content"}):
                                        if a == 0:
                                            firstNews = i.find("h2").find("a").get("href")
                                        elif a == 1:
                                            secondNews = i.find("h2").find("a").get("href")
                                        elif a == 2:
                                            thirdNews = i.find("h2").find("a").get("href")
                                        a = a + 1
                                url = "https://www.independent.co.uk"
                                firstUrl = url + firstNews
                                secondUrl = url + secondNews
                                thirdUrl = url + thirdNews

                                def getContent(url):
                                    try:
                                        request = requests.get(url, timeout=30, headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 OPR/76.0.4017.154'})
                                        content = request.content
                                        soup = BeautifulSoup(content, "html.parser")
                                        topic = "News"
                                        subtopic = "News"
                                        name = "independentNews"
                                        iconUrl = "https://img1.pnghut.com/0/18/25/C0STPpgPST/united-kingdom-media-daily-telegraph-irish-independent-symbol.jpg"
                                        pageurl = url
                                        newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                                        newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                                        try:
                                            newsTags = soup.find("div", {"class": "sc-psEMT gwrImx main-wrapper"}).find(
                                                "div", {"class": "sc-pJgJK daSdlt sc-pZbQk kzfPTw"}).find_all('p')
                                            newsContent = ""
                                            for new in newsTags:
                                                newsContent = newsContent + " " + new.get_text().strip()


                                        except:
                                            try:

                                                newsTags = soup.find("div", {"id": "main"}).find_all('p')
                                                newsContent = ""
                                                for new in newsTags:
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




        except:
            print("Error!")

    def time():
        try:
            url="https://time.com"
            websiteRequest=requests.get(url,timeout=30)

            if websiteRequest.status_code!=200:
                newsImage = "Error"
                newsTitle = "Error"
                newsContent = "Error"
            else:
                websiteContent=websiteRequest.content
                soup=BeautifulSoup(websiteContent,"html.parser")
                firstNews=soup.find("section",{"class":"homepage-module lead"}).find("div",{"class":"primary"}).find("article",{"class":"slide"}).find("div",{"class":"content"}).find("h2").find("a").get("href")
                a=0

                for i in soup.find("section",{"class":"homepage-module lead"}).find("div",{"class":"secondary"}).find_all('article',attrs={'class':'slide'}):
                    if a==0:
                        secondNews = i.find("div",{"class":"content"}).find("h2",{"class":"title"}).find("a").get("href")
                    elif a==1:
                        thirdNews = i.find("div",{"class":"content"}).find("h2",{"class":"title"}).find("a").get("href")
                    a=a+1

                url="https://time.com"
                firstUrl=url+firstNews
                secondUrl =url+secondNews
                thirdUrl =url+thirdNews


                def getContent(url):
                    try:
                        request=requests.get(url,timeout=30)
                        content=request.content
                        soup=BeautifulSoup(content,"html.parser")
                        topic = "News"
                        subtopic = "News"
                        name = "timeNews"
                        iconUrl = "https://banner2.cleanpng.com/20180602/hxf/kisspng-shelter-magazine-time-news-magazine-house-garden-no-time-5b127d0800e9a0.1898284415279383120038.jpg"
                        pageurl = url
                        newsImage = soup.find("meta",{"property":"og:image"}).get("content")
                        newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                        newsContent=""
                        try:
                            newsTags = soup.find("div", {"class": "article content body clearfix"}).find("div", {"class": "padded"})
                            for i in newsTags.find_all('div', attrs={'class': 'component inline image margin-32-tb'}):
                                i.replace_with("")
                            for i in newsTags.find_all('div', attrs={'class': 'component subscription-cta'}):
                                i.replace_with("")
                            for i in newsTags.find_all('div', attrs={'class': 'component newsletter-callout newsletter-inline-signup with-known-country'}):
                                 i.replace_with("")
                            for i in newsTags.find_all('div', attrs={'class': 'article-bottom'}):
                                i.replace_with("")
                            for i in newsTags.find_all('p', attrs={'class': 'author-feedback-text'}):
                                i.replace_with("")
                            for new in newsTags.find_all("p"):
                                newsContent = newsContent + " " + new.get_text()

                        except:
                            try:
                                request = requests.get(url, timeout=30)
                                content = request.content
                                soup = BeautifulSoup(content, "html.parser")
                                newsImage = soup.find("meta", {"property": "og:image"}).get("content")

                                newsTitle = soup.find("meta", {"property": "og:title"}).get("content")

                                newsTags = soup.find("div", {"class": "player"}).find("div", {"class": "video-info"}).find("div", {"class": "description"}).get_text()
                                newsContent = ""

                                newsContent = newsContent + " " + newsTags

                            except:
                                try:
                                    request = requests.get(url, timeout=30)
                                    content = request.content
                                    soup = BeautifulSoup(content, "html.parser")
                                    newsImage = soup.find("meta", {"property": "og:image"}).get("content")

                                    newsTitle = soup.find("meta", {"property": "og:title"}).get("content")

                                    newsTags = soup.find("main", {"class": "collection-sections"}).find_all("section",{"class": "collection-section"})
                                    newsContent = ""


                                    for i in newsTags:
                                        for c in i.find_all('ul'):
                                                newsContent = newsContent + " " + c.find("h3").text.strip()+ " " + c.find("h4").text

                                except:
                                    print("Error!")

                        databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                    except:
                        print("Error!")



                try:
                    getContent(firstUrl)
                except:
                    getContent(url+firstUrl)
                try:
                    getContent(secondUrl)
                except:
                    getContent(url+secondUrl)
                try:
                    getContent(thirdUrl)
                except:
                    getContent(url+thirdUrl)



        except:
            print("Error!")





    def chinaPost():
        try:
            url="https://chinapost.nownews.com"
            websiteRequest=requests.get(url,timeout=30)

            if websiteRequest.status_code!=200:
                newsImage = "Error"
                newsTitle = "Error"
                newsContent = "Error"
            else:
                websiteContent=websiteRequest.content
                soup=BeautifulSoup(websiteContent,"html.parser")

                firstNews=soup.find("div",{"class":"td_module_mx5 td-animation-stack td-big-grid-post-0 td-big-grid-post td-big-thumb"}).find("div",{"class":"td-module-thumb"}).find("a",{"class":"td-image-wrap"}).get("href")
                secondNews = soup.find("div",{"class":"td-big-grid-wrapper"}).find("div",{"class":"td-big-grid-scroll"}).find("div",{"class":"td_module_mx6 td-animation-stack td-big-grid-post-1 td-big-grid-post td-small-thumb"}).find("div",{"class":"td-module-thumb"}).find("a",{"class":"td-image-wrap"}).get("href")
                thirdNews = soup.find("div",{"class":"td-big-grid-wrapper"}).find("div",{"class":"td-big-grid-scroll"}).find("div",{"class":"td_module_mx6 td-animation-stack td-big-grid-post-2 td-big-grid-post td-small-thumb"}).find("div",{"class":"td-module-thumb"}).find("a",{"class":"td-image-wrap"}).get("href")


                url="https://chinapost.nownews.com"
                firstUrl=firstNews
                secondUrl =secondNews
                thirdUrl =thirdNews


                def getContent(url):
                    try:
                        request=requests.get(url,timeout=30)
                        content=request.content
                        soup=BeautifulSoup(content,"html.parser")
                        topic = "News"
                        subtopic = "News"
                        name = "chinaPostNews"
                        iconUrl = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQVBpkJTy2YBXCIifpJhXl1fDIgTBuSPWm-dS6fX3uNdxEHL9Bht7UjL_7124h7f_Zfo8c&usqp=CAU"
                        pageurl = url
                        newsImage = soup.find("meta",{"property":"og:image"}).get("content")
                        newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                        newsTags= soup.find("div",{"class":"td-post-content"}).find_all('p')
                        newsContent=""
                        for new in newsTags:
                            newsContent = newsContent+ " " + new.get_text().strip()

                        databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                    except:
                        print("Error!")
                getContent(firstUrl)
                getContent(secondUrl)
                getContent(thirdUrl)

        except:
            print("Error!")





    def france24():
        try:
            url="https://www.france24.com/en/"
            hdr = {'User-Agent': 'Mozilla/5.0'}
            websiteRequest=requests.get(url,headers=hdr,timeout=30)
            if websiteRequest.status_code!=200:
                newsImage = "Error"
                newsTitle = "Error"
                newsContent = "Error"
            else:
                websiteContent=websiteRequest.content
                soup=BeautifulSoup(websiteContent,"html.parser")
                firstNews=soup.find("div",{"class":"t-content t-content--page-builder"}).find("section",{"class":"t-content__section-pb"}).find("div",{"class":"o-banana-split"}).find("div",{"class":"o-layout-list o-banana-split__main-articles"}).find("div",{"class":"o-layout-list__item o-layout-list__item--main-item"}).find("div",{"class":"m-item-list-article m-item-list-article--main-article"}).find("a").get("href")
                a=0

                for i in soup.find("div",{"class":"t-content t-content--page-builder"}).find("section",{"class":"t-content__section-pb"}).find("div",{"class":"o-banana-split"}).find("div",{"class":"o-layout-list o-banana-split__main-articles"}).find_all('div',attrs={'class':'o-layout-list__item l-m-100 l-t-50 l-d-50'}):
                    if a==0:
                        secondNews = i.find("div",{"class":"m-item-list-article"}).find("a").get("href")
                    elif a==1:
                        thirdNews = i.find("div",{"class":"m-item-list-article"}).find("a").get("href")
                    a=a+1

                url="https://www.france24.com"
                firstUrl=url+firstNews
                secondUrl =url+secondNews
                thirdUrl =url+thirdNews



                def getContent(url):
                    try:
                        request=requests.get(url,headers=hdr,timeout=30)
                        content=request.content
                        soup=BeautifulSoup(content,"html.parser")
                        topic = "News"
                        subtopic = "News"
                        name = "france24News"
                        iconUrl = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/France24.png/635px-France24.png"
                        pageurl = url
                        newsImage = soup.find("meta",{"property":"og:image"}).get("content")
                        newsTitle = soup.find("meta", {"property": "og:title"}).get("content")

                        try:
                            newsContent = soup.find("p", {"class": "t-content__chapo"}).get_text().strip()
                            newsTags = soup.find("div", {"class": "t-content t-content--article"}).find("div", {
                                "class": "t-content__body u-clearfix"})
                            for i in newsTags.find_all('div', attrs={'class': 'o-self-promo o-self-promo--app o-self-promo--hidden'}):
                                i.replace_with("")
                            for i in newsTags.find_all('div', attrs={'class': 'o-self-promo o-self-promo--nl'}):
                                i.replace_with("")
                            for i in newsTags.find_all('div', attrs={'class': 'm-em-flash'}):
                                i.replace_with("")
                            for new in newsTags.find_all("p"):
                                newsContent = newsContent+ " " + new.get_text().strip()


                        except:
                            try:
                                newsContent = ""
                                newsTags = soup.find("div", {"class": "t-content t-content--article"}).find("p", {"class": "t-content__chapo"})
                                newsContent = newsContent + " " + newsTags.get_text().strip()


                            except:
                                try:
                                    newsContent = ""
                                    newsTags = soup.find("div", {"class": "t-content__body u-clearfix"})
                                    for i in newsTags.find_all('div', attrs={'class': 'm-em-diaporama'}):
                                        i.replace_with("")
                                    for i in newsTags.find_all("p"):
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

    def insider():
        try:
            url="https://www.insider.com"

            websiteRequest=requests.get(url,timeout=30)
            if websiteRequest.status_code!=200:
                newsImage = "Error"
                newsTitle = "Error"
                newsContent = "Error"
            else:

                websiteContent=websiteRequest.content
                soup=BeautifulSoup(websiteContent,"html.parser")
                firstNews=soup.find("div",{"class":"col-12"}).find("section",{"class":"river-item featured-tout homepage"}).find("div",{"class":"tout-text-wrapper featured-tout"}).find("h1",{"class":"tout-title featured-tout"}).find("a",{"class":"tout-title-link"}).get("href")
                a=0

                for i in soup.find("div",{"class":"col-12"}).find("section",{"class":"river-item featured-tout homepage"}).find("div",{"class":"tout-text-wrapper featured-tout"}).find("div",{"class":"tout-copy featured-tout typography"}).find("ol").find_all('li'):
                    if a==0:
                        secondNews = i.find("a").get("href")
                    elif a==1:
                        thirdNews = i.find("a").get("href")
                    a=a+1

                url="https://www.insider.com"
                firstUrl=firstNews
                secondUrl =secondNews
                thirdUrl =thirdNews


                def getContent(url):
                    try:
                        request=requests.get(url,timeout=30)
                        content=request.content
                        soup=BeautifulSoup(content,"html.parser")
                        topic = "News"
                        subtopic = "News"
                        name = "insiderNews"
                        iconUrl = "https://iconape.com/wp-content/files/cc/348265/png/348265.png"
                        pageurl = url
                        newsImage = soup.find("meta",{"property":"og:image"}).get("content")
                        newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                        try:
                            newsContent = ""
                            newsTags= soup.find("div",{"id":"piano-inline-content-wrapper"}).find("div",{"class":"content-lock-content"})
                            for i in newsTags.find_all('figure', attrs={'data-type': 'img'}):
                                i.replace_with("")
                            for new in newsTags.find_all('p'):
                                newsContent = newsContent+ " " + new.get_text().strip()


                        except:
                            try:
                                newsContent = ""
                                newsTags = soup.find("div", {"class": "col-12"}).find("article").find("section",{"class":"slideshow-container typography"}).find("div",{"class":"content-lock-content"}).find("ul",{"class":"summary-list"})
                                for i in newsTags.find_all('figure', attrs={'data-type': 'img'}):
                                    i.replace_with("")
                                for new in newsTags.find_all('li'):
                                    newsContent = newsContent+ " " + new.get_text().strip()


                            except:
                                print("Error!")
                        databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                    except:
                        try:
                            baseUrl = "https://www.insider.com"
                            request = requests.get(baseUrl+url, timeout=30)
                            content = request.content
                            soup = BeautifulSoup(content, "html.parser")
                            topic = "News"
                            subtopic = "News"
                            name = "insiderNews"
                            iconUrl = "https://iconape.com/wp-content/files/cc/348265/png/348265.png"
                            pageurl = baseUrl+url
                            newsImage = soup.find("meta", {"property": "og:image"}).get("content")
                            newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                            try:
                                newsContent = ""
                                newsTags = soup.find("div", {"id": "piano-inline-content-wrapper"}).find("div", {
                                    "class": "content-lock-content"})
                                for i in newsTags.find_all('figure', attrs={'data-type': 'img'}):
                                    i.replace_with("")
                                for new in newsTags.find_all('p'):
                                    newsContent = newsContent+ " " + new.get_text().strip()


                            except:
                                try:
                                    newsContent = ""
                                    newsTags = soup.find("div", {"class": "col-12"}).find("article").find("section", {"class": "slideshow-container typography"}).find("div", {"class": "content-lock-content"}).find("ul", {"class": "summary-list"})

                                    for i in newsTags.find_all('figure', attrs={'data-type': 'img'}):
                                        i.replace_with("")
                                    for new in newsTags.find_all('p'.find_all('li',id=False)):
                                        newsContent = newsContent+ " " + new.get_text().strip()


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




    def reuters():
        try:
            url="https://www.reuters.com"
            websiteRequest = requests.get(url,timeout=30)
            if websiteRequest.status_code!=200:
                newsImage = "Error"
                newsTitle = "Error"
                newsContent = "Error"
            else:
                websiteContent=websiteRequest.content
                soup=BeautifulSoup(websiteContent,"html.parser")
                firstNews=soup.find("div",{"class":"StaticMediaMaximizer__container___3-px7Y"}).find("div",{"class":"StaticMediaMaximizer__hero-wrapper___3KRKmY"}).find("div",{"class":"StaticMediaMaximizer__hero___3tmwgq"}).find("a",{"class":"MediaStoryCard__basic_hero___fSAEnM"}).get("href")
                a=0

                for i in soup.find("div",{"class":"StaticMediaMaximizer__container___3-px7Y"}).find("div",{"class":"StaticMediaMaximizer__cards___2xyS1_"}).find_all('a',attrs={'class':'MediaStoryCard__no_meta___3iQjxw StaticMediaMaximizer__card___2_CdUh'}):
                    if a==0:
                        secondNews = i.get("href")
                    elif a==1:
                        thirdNews = i.get("href")
                    a=a+1

                url="https://www.reuters.com"
                firstUrl=url+firstNews
                secondUrl =url+secondNews
                thirdUrl =url+thirdNews


                def getContent(url):
                    try:
                        request=requests.get(url,timeout=30)
                        content=request.content
                        soup=BeautifulSoup(content,"html.parser")
                        topic = "News"
                        subtopic = "News"
                        name = "reutersNews"
                        iconUrl = "https://cdn.iconscout.com/icon/free/png-512/reuters-283443.png"
                        pageurl = url
                        newsImage = soup.find("meta",{"property":"og:image"}).get("content")
                        newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                        newsContent = ""
                        newsTags= soup.find("div",{"class":"ArticleBody__container___D-h4BJ"}).find("div",{"class":"ArticleBody__content___2gQno2 paywall-article"}).find_all('p')
                        for new in newsTags:
                            newsContent = newsContent+ " " + new.get_text().strip()

                        databaseTransactions.contentAdd(name, newsTitle, newsContent, newsImage, pageurl, iconUrl,topic,subtopic)
                    except:
                        print("Error!")
                getContent(firstUrl)
                getContent(secondUrl)
                getContent(thirdUrl)

        except:
            print("Error!")

    def skyNews():
        try:
            url="https://news.sky.com"
            websiteRequest = requests.get(url,timeout=30)
            if websiteRequest.status_code!=200:
                newsImage = "Error"
                newsTitle = "Error"
                newsContent = "Error"
            else:
                websiteContent=websiteRequest.content
                soup=BeautifulSoup(websiteContent,"html.parser")
                a=0

                for i in soup.find("div",{"class":"sdc-site-tiles__inner"}).find("div",{"class":"sdc-site-tiles__group"}).find_all('h3',attrs={'class':'sdc-site-tile__headline'}):
                    if a==0:
                        firstNews = i.find("a",{"class":"sdc-site-tile__headline-link"}).get("href")
                    elif a==1:
                        secondNews = i.find("a",{"class":"sdc-site-tile__headline-link"}).get("href")
                    elif a==2:
                        thirdNews = i.find("a",{"class":"sdc-site-tile__headline-link"}).get("href")
                    a=a+1

                url="https://news.sky.com"
                firstUrl=url+firstNews
                secondUrl =url+secondNews
                thirdUrl =url+thirdNews


                def getContent(url):
                    try:
                        request=requests.get(url,timeout=30)
                        content=request.content
                        soup=BeautifulSoup(content,"html.parser")
                        topic = "News"
                        subtopic = "News"
                        name = "skyNews"
                        iconUrl = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Sky-news-logo.png/1200px-Sky-news-logo.png"
                        pageurl = url
                        newsImage = soup.find("meta",{"property":"og:image"}).get("content")
                        newsTitle = soup.find("meta", {"property": "og:title"}).get("content")

                        try:

                            newsContent = ""
                            newsTags= soup.find("div",{"class":"sdc-site-layout-wrap site-wrap site-wrap-padding"}).find("div",{"class":"sdc-article-body sdc-article-body--story sdc-article-body--lead"})

                            for i in newsTags.find_all('div', attrs={'class': 'sdc-article-widget sdc-article-tweet'}):
                                i.replace_with("")

                            for i in newsTags.find_all('div', attrs={'class': 'sdc-site-video sdc-article-widget callfn'}):
                                i.replace_with("")

                            for i in newsTags.find_all('div', attrs={'class': 'sdc-article-widget sdc-article-podcast'}):
                                i.replace_with("")

                            for new in newsTags.find_all('p'):
                                newsContent = newsContent+ " " + new.get_text().strip()

                        except:
                            try:
                                newsContent = ""
                                newsTags = soup.find("div", {"class": "section-wrap"}).find("div",{"class": "sdc-article-header"}).find("div",{"class": "sdc-article-header__main"}).find("div",{"class": "sdc-article-header__titles"})

                                for i in newsTags.find_all('div', attrs={'class': 'sdc-article-widget sdc-article-tweet'}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={'class': 'sdc-site-video sdc-article-widget callfn'}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div',attrs={'class': 'sdc-article-widget sdc-article-podcast'}):
                                    i.replace_with("")

                                for new in newsTags.find_all('p'):
                                    newsContent = newsContent + " " + new.get_text().strip()

                            except:
                                try:
                                    newsContent = ""
                                    newsTags = soup.find("div", {"class": "Theme-Layer-BodyText--inner"})

                                    for i in newsTags.find_all('div',attrs={'class': 'sdc-article-widget sdc-article-tweet'}):
                                        i.replace_with("")
                                    for i in newsTags.find_all('div',attrs={'class': 'sdc-site-video sdc-article-widget callfn'}):
                                        i.replace_with("")
                                    for i in newsTags.find_all('div',attrs={'class': 'sdc-article-widget sdc-article-podcast'}):
                                        i.replace_with("")

                                    for new in newsTags.find_all('p'):
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


    def euronews():
        try:
            url="https://www.euronews.com"
            websiteRequest = requests.get(url,timeout=30)
            if websiteRequest.status_code!=200:
                newsImage = "Error"
                newsTitle = "Error"
                newsContent = "Error"
            else:
                websiteContent=websiteRequest.content
                soup=BeautifulSoup(websiteContent,"html.parser")

                firstNews= soup.find("section",{"class":"o-section o-template-topstories qa-topStories"}).find_all("article",{"class":"m-object"})[0].find("a").get("href")
                secondNews = soup.find("section",{"class":"o-section o-template-topstories qa-topStories"}).find_all("article",{"class":"m-object"})[1].find("a").get("href")
                thirdNews  = soup.find("section",{"class":"o-section o-template-topstories qa-topStories"}).find_all("article",{"class":"m-object"})[2].find("a").get("href")


                url="https://www.euronews.com"
                firstUrl=url+firstNews
                secondUrl =url+secondNews
                thirdUrl =url+thirdNews


                def getContent(url):
                    try:
                        request=requests.get(url,timeout=30)
                        content=request.content
                        soup=BeautifulSoup(content,"html.parser")
                        topic = "News"
                        subtopic = "News"
                        name = "euroNews"
                        iconUrl = "https://cdn.freelogovectors.net/wp-content/uploads/2019/01/euronews_logo.png"
                        pageurl = url
                        newsImage = soup.find("meta",{"property":"og:image"}).get("content")
                        newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                        try:
                            newsContent = ""
                            newsTags= soup.find("div",{"class":"o-article__body"}).find("article",{"class":"article-wrapper c-article__full_article"}).find("section",{"class":"row collapse jsBottomArticle u-overflow-visible u-margin-top-medium-down-2 u-margin-top-large-only-3 u-margin-top-xlarge-4"}).find("div",{"class":"column small-12 medium-10 xlarge-11 js-responsive-iframes-container"}).find("div",{"class":"c-article-content js-article-content article__content"}).find_all('p')

                            for new in newsTags:

                                newsContent = newsContent+ " " + new.get_text().strip()

                        except:
                            try:

                                newsTags = soup.find("div", {"class": "o-article__body"}).find("div", {
                                    "class": "c-article__full_article"}).find("div", {
                                    "class": "column small-12 medium-10 xlarge-11 js-responsive-iframes-container u-zindex--bottom"}).find(
                                    "div", {"class": "c-article-content js-article-content article__content"}).find_all(
                                    'p')


                                for i in newsTags.find_all('div', attrs={'class': 'c-advertising-sticky-floor'}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div', attrs={'class': 'widget widget--type-image widget--size-fullwidth widget--align-center'}):
                                    i.replace_with("")
                                for i in newsTags.find_all('div', attrs={'class': 'widget widget--type-related widget--size-fullwidth widget--align-center'}):
                                    i.replace_with("")
                                for new in newsTags:
                                    newsContent = newsContent + " " + new.get_text().strip()


                            except:
                                try:

                                    newsTags = soup.find("div", {"class": "o-article__body"}).find("div", {"class": "c-article__full_article"}).find("div", {"class": "column small-12 medium-10 xlarge-11 js-responsive-iframes-container u-zindex--bottom "}).find("div",{"class": "c-article-content c-article-content--travel js-article-content article__content "}).find_all('p')

                                    for i in newsTags.find_all('div'):
                                        i.replace_with("")

                                    for new in newsTags:
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



    def sputnik():
        try:
            url="https://sputniknews.com"
            websiteRequest = requests.get(url,timeout=30)
            if websiteRequest.status_code!=200:
                newsImage = "Error"
                newsTitle = "Error"
                newsContent = "Error"
            else:
                websiteContent=websiteRequest.content
                soup=BeautifulSoup(websiteContent,"html.parser")
                a=0
                firstNews=soup.find("div",{"class":"b-main-news m-count-5"}).find("div",{"class":"b-main-news__first"}).find("div",{"class":"b-main-news__first-content"}).find("div",{"class":"b-main-news__first-title"}).find("a").get("href")
                secondNews = soup.find("div", {"class": "b-main-news m-count-5"}).find("div",{"class":"b-main-news__second m-item-2"}).find("a",{"class":"b-main-news__second-title"}).get("href")
                thirdNews = soup.find("div", {"class": "b-main-news m-count-5"}).find("div",{"class":"b-main-news__second m-item-3"}).find("a",{"class":"b-main-news__second-title"}).get("href")
                url="https://sputniknews.com"
                firstUrl=url+firstNews
                secondUrl =url+secondNews
                thirdUrl =url+thirdNews


                def getContent(url):
                    try:
                        request=requests.get(url,timeout=30)
                        content=request.content
                        soup=BeautifulSoup(content,"html.parser")
                        topic = "News"
                        subtopic = "News"
                        name = "sputnikNews"
                        iconUrl = "https://st6232.ispot.cc/apks/rossiya-segodnya/com.sputniknews.sputnik/icon.png"
                        pageurl = url
                        newsImage = soup.find("meta",{"property":"og:image"}).get("content")
                        newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                        newsContent = ""
                        try:
                            newsTags= soup.find("div",{"class":"l-main m-oh"}).find("div",{"class":"b-article__text"})
                            for i in newsTags.find_all('div', attrs={'class': 'ria-tweet'}):
                                i.replace_with("")
                            for i in newsTags.find_all('div', attrs={'class': 'b-inject m-inject-min'}):
                                i.replace_with("")
                            for i in newsTags.find_all('div', attrs={'class': 'b-inject m-inject-free'}):
                                i.replace_with("")
                            for i in newsTags.find_all('div', attrs={'class': 'sp-instagram'}):
                                i.replace_with("")
                            for i in newsTags.find_all('iframe'):
                                i.replace_with("")
                            for new in newsTags.find_all():
                                newsContent = newsContent+ " " + new.text.strip()


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



    def washingtonPost():
        try:
            hdr = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
            url="https://www.washingtonpost.com"
            websiteRequest = requests.get(url, headers=hdr,timeout=30)
            if websiteRequest.status_code!=200:
                newsImage = "Error"
                newsTitle = "Error"
                newsContent = "Error"
            else:
                websiteContent=websiteRequest.content
                soup=BeautifulSoup(websiteContent,"html.parser")
                a=0
                firstNews = soup.find("div",{"class":"card relative hpgrid-item hpgrid-item--c-start hpgrid-item--c-spans hpgrid-item--r-spans table1-columns-main grid-top grid-center"}).find("h2").find("a").get("href")
                secondNews = soup.find("div",{"class":"card relative hpgrid-item hpgrid-item--c-start hpgrid-item--c-spans hpgrid-item--r-spans table1-columns-right grid-top grid-right"}).find("h2").find("a").get("href")
                try:
                    thirdNews = soup.find("div",{"class":"card relative hpgrid-item hpgrid-item--c-start hpgrid-item--c-spans hpgrid-item--r-spans table1-columns-right grid-pseudo-left grid-middle grid-right"}).find("h2").find("a").get("href")
                except:
                    thirdNews = soup.find("div",{"class":"card relative hpgrid-item hpgrid-item--c-start hpgrid-item--c-spans hpgrid-item--r-spans table1-columns-main grid-pseudo-left grid-pseudo-right grid-bottom grid-center"}).find("h2").find("a").get("href")
                firstUrl = firstNews
                secondUrl = secondNews
                thirdUrl = thirdNews


                def getContent(url):
                    try:
                        request=requests.get(url,timeout=30)
                        content=request.content
                        soup=BeautifulSoup(content,"html.parser")
                        topic = "News"
                        subtopic = "News"
                        name = "washingtonPostNews"
                        iconUrl = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/The_Logo_of_The_Washington_Post_Newspaper.svg/1200px-The_Logo_of_The_Washington_Post_Newspaper.svg.png"
                        pageurl = url
                        newsImage = soup.find("meta",{"property":"og:image"}).get("content")
                        newsTitle = soup.find("meta", {"property": "og:title"}).get("content")
                        try:
                            newsContent = ""
                            newsTags= soup.find("div",{"class":"relative"}).find("article",{"class":"b-l br-l mb-xxl-ns mt-xxs mt-md-l pr-lg-l col-8-lg mr-lg-l"}).find("div",{"class":"article-body"}).find_all('p')
                            for new in newsTags:
                                newsContent = newsContent+ " " + new.get_text().strip()


                        except:
                            try:

                                newsContent = ""
                                newsTags = soup.find("div",{"class":"relative"}).find("main", {"class": "flex-grid flex flex-wrap mr-auto ml-auto print-mt-none"}).find("article",{"class":"b-l br-l mb-xxl-ns mt-xxs mt-md-l pr-lg-l col-8-lg mr-lg-l mw-100"}).find("div",{"class":"article-body"}).find("section").find_all('p',attrs={'data-el':'text'})
                                for new in newsTags:
                                    newsContent = newsContent+ " " + new.get_text().strip()


                            except:
                                try:

                                    newsContent = ""
                                    newsTags = soup.find("main").find("article").find("div", {"class": "mb-md mt-md"}).find("div", {"class": "scrolly relative"}).find_all('div', attrs={'class': 'font--body font-xs-ns vh-100'})
                                    for new in newsTags:
                                        newsContent = newsContent+ " " + new.find("p").get_text().strip()


                                except:
                                    try:

                                        newsContent = ""
                                        newsTags = soup.find("section",{"id":"ent-pb-main"}).find("div",{"class":"ent-article-body ent-layout-centered"}).find("div",{"class": "main"}).find_all('p')
                                        for new in newsTags:
                                            newsContent = newsContent + " "+ new.get_text().strip()


                                    except:
                                        try:

                                            newsContent = ""
                                            newsTags = soup.find("article", {"class": "b-l br-l mb-xxl-ns mt-xxs mt-md-l pr-lg-l col-8-lg mr-lg-l"}).find("div", {"class": "article-body"}).find("div", {"class": "teaser-content"}).find("section").find_all('p')
                                            for new in newsTags:
                                                newsContent = newsContent + " " + new.get_text().strip()


                                        except:
                                            try:
                                                newsContent = ""
                                                newsTags = soup.find("main").find("article").find("div", {"class": "topper-grid"}).find("span").get_text()
                                                newsContent = newsContent + " " + newsTags.strip()


                                            except:
                                                try:
                                                    newsContent = ""
                                                    newsTags = soup.find("main").find("article").find("div", {"class": "topperwrapper"}).find("span").get_text()
                                                    newsContent = newsContent + " " + newsTags.strip()


                                                except:
                                                    try:
                                                        newsContent = ""
                                                        newsTags = soup.find("div",{"class":"story relative"}).find("div",{"class":"book-grid"}).find_all('div',{'class':'nested-elements book-text'})
                                                        for i in newsTags:
                                                            newsContent = newsContent + " " + i.find("h3").get_text().strip()+ " " + i.find_all("p")[0].get_text().strip()+ i.find_all("p")[1].get_text().strip()


                                                    except:
                                                        try:
                                                            newsContent = ""
                                                            newsTags = soup.find("div", {"class": "story relative"})
                                                            for i in newsTags.find_all('figure'):
                                                                i.replace_with("")
                                                            for i in newsTags.find_all('div'):
                                                                i.replace_with("")
                                                            for i in newsTags.find_all("p"):
                                                                newsContent = newsContent+ " " + i.get_text()

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


    bbc()
    aljazeera()
    dwNews()
    foxNews()
    rtNews()
    independent()
    time()
    chinaPost()
    france24()
    reuters()
    insider()
    skyNews()
    euronews()
    sputnik()
    washingtonPost()





