#!/usr/bin/python
# -*- coding: utf-8 -*-

# public_method.py

__author__      = "lijian"
__date__        = "2018.03.07"
__email__       = "lijian@capsheaf.com.cn"

CONFPATH = "./cloudMusic.conf"

# default config
DEFAULT_MUSCI_PATH = "/media/cloudMusic/music/"
DEFAULT_LYRIC_PATH = "/media/cloudMusic/lyric/"
DEFAULT_PICTURE_PATH = "/media/cloudMusic/picture/"





import os
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
 
# set default
def setDefaultConf():
    prompt = "This is a config file to set where is the download file directory!"
    if not os.path.exists(CONFPATH):
        os.mknod(CONFPATH)
    with open(CONFPATH, "w") as f:
        f.write("# " + prompt + "\n\n")
        f.write("MUSIC_PATH=" + DEFAULT_MUSIC_PATH)
        f.write("LYRIC_PATH=" + DEFAULT_LYRIC_PATH)
        f.write("PICTURE_PATH=" + DEFAULT_PICTURE_PATH)
        f.close()
    
# read config file
def getConf(flags = []):
    if not os.path.exists(CONFPATH):
        setDefaultConf()

    result = []
    with open(CONFPATH, "r") as f:
        fls = f.readlines()
        for flag in flags:
            for fl in fls():
                if fl.startswith(flag):
                    result.append(fl.split(flag + "=")[1])
                    break
                else:
                    continue
                result.append("")
        return result


# write congif file
def setConf(flags = {}):
    pass   


    

# get url from file
def readUrl(flags = []):
    pass

# set url to file
def writeUrl(flags = {}):
    pass

# get versioninfo
def printVersion(program_name = ""):
    pass
