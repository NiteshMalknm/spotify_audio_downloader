from Singleton import Singleton

def getTitleArtists(url):
    spotipyObj=Singleton.getSpotipyInstance()
    resp=spotipyObj.track(url)
    artists=""
    for artist in resp["artists"]:
        artists=artists+" "+artist["name"]
    return resp["name"]+" "+artists

