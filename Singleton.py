from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from backports import configparser
from yt_dlp import YoutubeDL
class Singleton:
    
    spotipyObj=None
    Environment=None
    ydlObj=None
    
    @staticmethod
    def getSpotipyInstance():
        if Singleton.spotipyObj is None:
            Singleton.spotipyObj=spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=Singleton.Environment.get('DEFAULT','spotify_clientId'),client_secret=Singleton.Environment.get('DEFAULT','spotify_client_secret')))        
            print("spotipy obj is created")
        return Singleton.spotipyObj

    @staticmethod
    def getEnvInstance():
        if Singleton.Environment is None:
            Singleton.Environment=configparser.RawConfigParser()
            Singleton.Environment.read('application.properties')
            print("env obj is created")
        return Singleton.Environment
        
    @staticmethod
    def getydlInstance():
        if Singleton.ydlObj is None:
            ydl_opts ={
                'outtmpl': 'audio/%(playlist_title)s',
                'format': 'bestaudio/best',
                'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
                                  }],
                        }
            Singleton.ydlObj=YoutubeDL(ydl_opts) 
            print("ydl obj is created")
        return Singleton.ydlObj