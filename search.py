#!/usr/bin/python
# -*- coding: utf-8 -*-

# search.py

__author__ = "lijian"
__date__ = "2018.03.07"
__email__ = "lijian@capsheaf.com.cn"



# 


URL_SEARCH = "http://s.music.163.com/search/get/?"
SERACH_PARAM =  ["type", "s", "limit", "offset"]


def searchmusic(searchstr = ""):
    param = "type=1"
    param = param + "&" + "s=" + searchstr
    url = URL_SEARCH + PARAM
    
    








