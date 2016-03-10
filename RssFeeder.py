import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime
import re



class RssFeeder(object):

    def __init__(self, _url, _collection, _category):
        self.url			= _url
        self.collection	                = _collection
        self.data			= {}
        self.category                   = _category

    def runCrawl(self):
        response	= requests.get(self.url)
        
        soup		= bs(response.content, "html.parser")
        items_soup	= soup.find_all("item")
        items		= []

        self.data['collection']	        = self.collection
        self.data['category']           = self.category


        for item in items_soup:

            title	= item.title.text
            link	= item.link.text
            desc	= item.description.text

            if item.pubdate is not None:
                pubdate     = item.pubdate.text
                pubdate     = self.dateParsing(pubdate)
            else:
                # pubdate가 없을때 현재시간을 pubdate로 함
                pubdate     = datetime.now()


            insert_data = {
                "_id"			: link,
                "pubdate"		: pubdate,
                "title"			: title,
                "description"	        : desc,
                "category"              : self.category
            }

            print("="*30)
            print(pubdate)
            print(self.collection)
            print(desc[:100])
            items.append( insert_data )

        self.data['items']	= items

        return self.data


    ##
    # pubdate 를 datetime 객체로만들어 return
    # input : pubdate(pubdate에 해당하는 문자열)
    # output: datetime object
    def dateParsing(self, _pubdate):
        parser_type1            = re.compile('[a-zA-Z]+, \d+ [a-zA-Z]+ \d+ \d+:\d+:\d+ GMT')
        parser_type2            = re.compile('[a-zA-Z]+, \d+ [a-zA-Z]+ \d+ \d+:\d+:\d+ .0900')
        parser_type3            = re.compile('\d+-\d+-\d+ \d+:\d+:\d+')
        parser_type4            = re.compile('\d+.0900')

        result1     = parser_type1.search(_pubdate)
        result2     = parser_type2.search(_pubdate)
        result3     = parser_type3.search(_pubdate)
        result4     = parser_type4.search(_pubdate)


        if result1 is not None:
            pubdate = result1.group()
            pubdate = pubdate[:-4]
            pubdate = datetime.strptime(pubdate,"%a, %d %b %Y %H:%M:%S")
        elif result2 is not None:
            pubdate = result2.group()
            pubdate = pubdate[:-6]
            pubdate = datetime.strptime(pubdate,"%a, %d %b %Y %H:%M:%S")
        elif result3 is not None:
            pubdate = result3.group()
            pubdate = datetime.strptime(pubdate,"%Y-%m-%d %H:%M:%S")
        elif result4 is not None:
            pubdate = result4.group()
            year    = int(pubdate[:4])
            month   = int(pubdate[4:6])
            day     = int(pubdate[6:8])
            hour    = int(pubdate[8:10])
            minute  = int(pubdate[10:12])
            sec     = int(pubdate[12:14])

            pubdate = datetime(year, month, day, hour, minute, sec)


        if result1 is None and result2 is None and result3 is None and result4 is None:
            print("parsing error!")
            exit()

        return pubdate
 
