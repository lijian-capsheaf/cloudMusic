#!/usr/bin/python
# -*- coding: utf-8 -*-

# search.py

__author__ = "lijian"
__date__ = "2018.03.07"
__email__ = "lijian@capsheaf.com.cn"


from public_method import getJsonDate

# 


URL_SEARCH = "http://s.music.163.com/search/get/?"
SERACH_PARAM =  ["type", "s", "limit", "offset"]


def searchmusic(searchstr = ""):
    
    musiclist = []    
    

    # set param
    param = "type=1"
    param = param + "&" + "s=" + searchstr
    url = URL_SEARCH + PARAM
    
    searchresult = getJsonDate(url)
    # resolve json date
    






if __name__ == "__main__":
    print "This is a search program!"
