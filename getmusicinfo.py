#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "lijian"
__date__ = "2018.03.02"
__email__ = "lijian@capsheaf.com.cn"

# getmusicinfo.py
#
# This is a test program for our self,
# if some problems happend, please connect to me
#
#

import urllib
import re

URL_SONG_INFO = "http://music.163.com/#/song?id="
URL_SONG_MPS = ""
MAXID = 9999999999

# read all html content
def getHtmlContent(url):
    page = urllib.urlopen(url)
    return page.read()

# get music name from html content
def getMusicName():
    pass


# 
def getMusicURL(MusicID)

# set music id from 0 to MAXID
def setMusicID(oldID = 0):
    
    pass


def main():

    id = "1234567"
    url = URL_SONG + id
    print getHtmlContent(url)

main()









