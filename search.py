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


def SearchMusicFromNet(searchstr = ""):
    # def var    
    musiclist = []
    music = []
    art = []

    code = int()
    result = {}
    songCount = int()
    songs = []
    
    album = {}
    album_picUrl = ""
    # album_artists = {}
    # album_artists_picUrl = ""
    # album_artists_id = int()
    # album_artists_name = ""
    album_id = int()
    album_name = ""
    name = ""
    page = ""
    artists = []
    # artist_picUrl = ""
    # artist_id = int()
    artist_name = ""
    # audio = ""
    id = int()
    # djProgramId = int()   

    # set param
    param = "type=1"
    param = param + "&" + "s=" + searchstr
    url = URL_SEARCH + param
    
    searchresult = getJsonDate(url)
    # resolve json date
    code = searchresult["code"]
    if code != 200:
        print "No search result!"
        return
    result = searchresult["result"]
    songCount = result["songCount"]
    songs = result["songs"]
    for song in songs:
        name = song["name"]
        page = song["page"]
        # audio = song["audio"]
        id = song["id"]
        # djProgramId = song["djProgramId"]
        album = song["album"]
        album_picUrl = album["picUrl"]
        # album_artists = album["artists"]
        # album_artists_picUrl = album_artists["picUrl"]
        # album_artists_id = album_artists["id"]
        # album_artists_name = album_artists["name"]
        # album_id = album["id"]
        # album_name = album["name"]
        artists = song["artists"]
        for artist in artists:
            # artist_picUrl = artist["picUrl"]
            # artist_id = artist["id"]
            artist_name = artist["name"]
            art.append(artist_name)
        
        # [name,page,id,album_picUrl,art]
        music.append(name)
        music.append(page)
        music.append(id)
        music.append(album_picUrl)
        music.append(artist_name)
        
        musiclist.append(music)

    return musiclist


if __name__ == "__main__":
    print "This is a search program!"
