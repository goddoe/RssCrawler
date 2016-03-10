import os
from pymongo import MongoClient
from RssFeedManager import RssFeedManager


def main():
    
    # CMD 화면 클리어
    os.system("clear")

    # c는 { "전자신문": "etnews"} 와 같이 
    # 한글이름을 MongoDB에 저장할 collection 이름과 매칭된 Dictionary
    c                   = collection_name_generator()

    # MongoDB에 접속
    client              = MongoClient("")
    
    # rssFeederManager에게 MongoClient 객체를 넘겨 접근 할 수있게함
    rssFeederManager	= RssFeedManager(client)


    #########
    ## Description
    ## addRssFeed("rss url", "collection name", "category")

    # 매일경제
    rssFeederManager.addRssFeed("http://file.mk.co.kr/news/rss/rss_30100041.xml", c['매일경제'],    '경제')
    rssFeederManager.addRssFeed("http://file.mk.co.kr/news/rss/rss_30200030.xml", c['매일경제'],    '정치')
    rssFeederManager.addRssFeed("http://file.mk.co.kr/news/rss/rss_50400012.xml", c['매일경제'],    '사회')
    rssFeederManager.addRssFeed("http://file.mk.co.kr/news/rss/rss_30300018.xml", c['매일경제'],    '국제')
    rssFeederManager.addRssFeed("http://file.mk.co.kr/news/rss/rss_50100032.xml", c['매일경제'],    '기업경영')
    rssFeederManager.addRssFeed("http://file.mk.co.kr/news/rss/rss_50200011.xml", c['매일경제'],    '증권')
    rssFeederManager.addRssFeed("http://file.mk.co.kr/news/rss/rss_50300009.xml", c['매일경제'],    '부동산')

    # 한국경제
    rssFeederManager.addRssFeed("http://rss.hankyung.com/new/news_main.xml",    c['한국경제'],      '주요뉴스')
    rssFeederManager.addRssFeed("http://rss.hankyung.com/new/news_stock.xml",   c['한국경제'],      '증권')
    rssFeederManager.addRssFeed("http://rss.hankyung.com/new/news_economy.xml", c['한국경제'],      '경제')
    rssFeederManager.addRssFeed("http://rss.hankyung.com/new/news_industry.xml",c['한국경제'],      'it')
    rssFeederManager.addRssFeed("http://rss.hankyung.com/new/news_estate.xml",  c['한국경제'],      '부동산')
    rssFeederManager.addRssFeed("http://rss.hankyung.com/new/news_politics.xml",c['한국경제'],      '정치')
    rssFeederManager.addRssFeed("http://rss.hankyung.com/new/news_society.xml", c['한국경제'],      '사회')
    
    # 연합뉴스
    rssFeederManager.addRssFeed("http://www.yonhapnews.co.kr/RSS/economy.xml",  c['연합뉴스'],      '경제')
    rssFeederManager.addRssFeed("http://www.yonhapnews.co.kr/RSS/stock.xml",    c['연합뉴스'],      '증권')
    rssFeederManager.addRssFeed("http://www.yonhapnews.co.kr/RSS/society.xml",  c['연합뉴스'],      '사회')

    #헤럴드경제
    rssFeederManager.addRssFeed("http://biz.heraldcorp.com/common/rss_xml.php?ct=1",    c['헤럴드경제'], '경제')
    rssFeederManager.addRssFeed("http://biz.heraldcorp.com/common/rss_xml.php?ct=4",    c['헤럴드경제'], '재테크')

    #이데일리
    rssFeederManager.addRssFeed("http://rss.edaily.co.kr/stock_news.xml",       c['이데일리'],      '증권')
    rssFeederManager.addRssFeed("http://rss.edaily.co.kr/economy_news.xml",     c['이데일리'],      '경제')
    rssFeederManager.addRssFeed("http://rss.edaily.co.kr/finance_news.xml",     c['이데일리'],      '금융')
    rssFeederManager.addRssFeed("http://rss.edaily.co.kr/bondfx_news.xml",      c['이데일리'],      '채권 외환')
    rssFeederManager.addRssFeed("http://rss.edaily.co.kr/enterprise_news.xml",  c['이데일리'],      '기업')
    rssFeederManager.addRssFeed("http://rss.edaily.co.kr/realestate_news.xml",  c['이데일리'],      '부동산')

    # 머니투데이
    rssFeederManager.addRssFeed("http://rss.mt.co.kr/mt_news.xml",              c['머니투데이'],    '경제')
    rssFeederManager.addRssFeed("http://rss.mt.co.kr/mt_news_stock.xml",        c['머니투데이'],    '투자')

    # 전자신문
    rssFeederManager.addRssFeed("http://rss.etnews.com/Section022.xml",         c['전자신문'],      '금융')
    rssFeederManager.addRssFeed("http://rss.etnews.com/Section024.xml",         c['전자신문'],      '경제')
    rssFeederManager.addRssFeed("http://rss.etnews.com/Section026.xml",         c['전자신문'],      '부동산')
    rssFeederManager.addRssFeed("http://rss.etnews.com/Section05.xml",          c['전자신문'],      '국제')

    #경향신문
    rssFeederManager.addRssFeed("http://www.khan.co.kr/rss/rssdata/politic_news.xml",   c['경향신문'], '정치')
    rssFeederManager.addRssFeed("http://www.khan.co.kr/rss/rssdata/economy_news.xml",   c['경향신문'], '경제')
    rssFeederManager.addRssFeed("http://www.khan.co.kr/rss/rssdata/society_news.xml",   c['경향신문'], '경제')
    rssFeederManager.addRssFeed("http://www.khan.co.kr/rss/rssdata/kh_world.xml",       c['경향신문'], '국제')

    # run
    rssFeederManager.runCrawler()

# 사실 굳이 이렇게 안하고 바로 addRssFeed 두번째
# 파라미터에 영문 콜랙션 이름 넣으셔도 됩니다!
def collection_name_generator():
    coll_name_of                = {}
    coll_name_of['매일경제']    = 'mk'
    coll_name_of['한국경제']    = 'hankyung'
    coll_name_of['머니투데이']  = 'mt'
    coll_name_of['연합뉴스']    = 'yonhapnews'
    coll_name_of['헤럴드경제']  = 'heraldcorp'
    coll_name_of['이데일리']    = 'edaily'
    coll_name_of['전자신문']    = 'etnews'
    coll_name_of['경향신문']    = 'khan'

    return coll_name_of

if __name__=='__main__':
    main()

