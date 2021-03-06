#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return Pefinance

class Pefinance(BaseFeedBook):
    title                 = u'经济新闻-人民网'
    description           = u'经济新闻-人民网。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = " "
    coverfile             = " "
    oldest_article        = 14400    #下载多长时间之内的文章，小于等于365则单位为天，大于365则单位为秒，0为不限制,4*60*60
    deliver_times         = [8,12,16,20]
    
    feeds = [
            (u'经济新闻', 'http://www.people.com.cn/rss/finance.xml'),
            ]
    
    def fetcharticle(self, url, opener, decoder):
        #每个URL都增加一个后缀full=y，如果有分页则自动获取全部分页
        url += '?full=y'
        return BaseFeedBook.fetcharticle(self,url,opener,decoder)
