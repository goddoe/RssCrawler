from RssFeeder import RssFeeder

class RssFeedManager(object):
    
    def __init__(self, _client):
        self.client		= _client
        self.rssFeeder	        = []


    def addRssFeed(self, _url, _collection, _category):
        self.rssFeeder.append( RssFeeder(_url, _collection, _category) )

    def runCrawler(self):
        
        for rssFeeder in self.rssFeeder:
            data = rssFeeder.runCrawl()
            self.storeData(data)
    
        print("Crawl Done!")


    def storeData(self, data):
        ## if mongodb
        db		= self.client['rss']
        coll	        = db[data['collection']]

        for item in data['items'] :
            result = coll.replace_one({'_id': item['_id']}, item, upsert=True)
 
