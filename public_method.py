#!/usr/bin/python
# -*- coding: utf-8 -*-

# public_method.py

__author__      = "lijian"
__date__        = "2018.03.07"
__email__       = "lijian@capsheaf.com.cn"


import urllib,urllib2
import json

# get html content, return "str"
def getHtmlContent(url):
    try:
        page = urllib.urlopen(url)
        return page.read()
    except:
        page = urllib2.urlopen(url)
        return page.read()

# get json date return dic
def getJsonDate(url):
    htmlcontent = getHtmlContent(url)
    urljson = json.loads(htmlcontent)
    return urljson

# print error info
def error(errstr):
    print str
 
# read config file
def getConf(flag = []):
    pass

# write congif file
def setConf(flag = []):
    pass

# get url from file
def readUrl(flag = []):
    pass

