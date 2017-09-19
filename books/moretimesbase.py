#!/usr/bin/env python
# -*- coding:utf-8 -*-
deliver_times = [8,12,16,20] #deliver_times=[6,14,22] 6:00,14:00,22:00三次推送
oldest_article        = 0    #下载多长时间之内的文章，小于等于365则单位为天，大于365则单位为秒，0为不限制28800,oldest_article=28800 #8*60*60
