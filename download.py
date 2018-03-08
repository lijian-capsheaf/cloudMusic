#!/usr/bin/python
# -*- coding: utf-8 -*-

# download.py

__author__ = "lijian"
__date_start__ = "2018.03.02"
__date_start__ = "..."
__email__ = "lijian@capsheaf.com.cn"
__version__ = "v1.0.0"

#
#
# info
#
#


import urllib,urllib2
import requests
import json
import os
from optparse import OptionParser

# %s is music id
URL_MUSIC = "http://music.163.com/song/media/outer/url?id=%s.mp3"
# %s is lyric id
URL_LYRIC = "http://music.163.com/api/song/lyric?os=web&id=%s&lv=-1&kv=-1&tv=-1"


# default path
DEFAULT_MUSIC_PATH = "/media/cloudMusic/music/"
DEFAULT_LYRIC_PATH = "/media/cloudMusic/lyric/"
DEFAULT_PICTURE_PATH = "/media/cloudMusic/picture"

# name
__PROGRAM__ = "Reptile of Music"

# 
def downloadMusic(url):
    musicname = "test"
    musicpath = MUSIC_PATH + musicname + ".mp3"
    urllib.urlretrieve(url,musicpath)
    print url


def downloadLRC(url, l_id):
    htmlcontent = urllib2.urlopen(url)
    hjson = json.loads(htmlcontent.read())
    lyric = hjson["lrc"]["lyric"]
    lyricfile = LYRIC_PATH + l_id + ".lrc"
    if not os.path.exists(lyricfile):
        os.system("touch lyricfile")
    try:
        lrcf = open(lyricfile, "w+")
        lrcf.write(lyric.encode("utf-8"))
    except Exception,e:
        print str(e)
    finally:
        lrcf.close()

def downloadPic(url,p_id):
    pass


def download(id = "", mode = "", ):
    url = "http://music.163.com/song/media/outer/url?id=167937.mp3"
    url2 = "http://music.163.com/api/song/lyric?os=web&id=1234567&lv=-1&kv=-1&tv=-1"
    downloadMusic(url)
    # downloadLRC(url2, "1234567")

    # write option
    opt = OptionParser()
    opt.add_option("-v", "--version",
                   action="store_true",
                   dest="version",
                   help="show the version of this command")

    opt.add_option("-a", "--all",
                   action="store_true",
                   dest="all",
                   help="download all")

    opt.add_option("-m", "--music",
                   action="store",
                   dest="mname",
                   help="download music")
    
    opt.add_option("-l", "--lyric",
                   action="store",
                   dest="lname",
                   help="download lyric")

    opt.add_option("-p", "--picture",
                   action="dtore",
                   dest="pname",
                   help="download picture")
    opt.add_option("setMusicUrl",
                   action="store"
                   dest="setMU",
                   help="set music download url")
    opt.add_option("setLyricUrl",
                   action="store"
                   dest="setLU",
                   help="set lyric download url")

    (option, args) = opt.parse_args()

    # resolve option
    # cat version
    if option.version:
        printVersion(__PROGRAM__)
        return
    # download all
    if option.all



__all__ =["download"]

if __name__ == "__main__":
    download()
