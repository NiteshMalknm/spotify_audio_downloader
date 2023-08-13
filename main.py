from Singleton import Singleton
import spotify_helper
import time
import requests
import events_handler
from threading import Thread
import youtube_helper

env=Singleton.getEnvInstance();
obj=Singleton.getydlInstance();
startMsg=env.get('DEFAULT','telegram_startMsg').replace(r"\n" , "\n") #Need to convert Text into string literals


def events_reader():
    offset=int(env.get('DEFAULT','offset'))
    while True:
        time.sleep(int(env.get('DEFAULT','read_msg_timeout')))
        param={"offset":offset}
        resp=requests.get(env.get('DEFAULT','telegram_baseurl')+env.get('DEFAULT','bot_token')+env.get('DEFAULT','telegram_getupdateurl'),param)
        resp=resp.json()
        print('Number of msg '+str(len(resp["result"]))+' in current cycle')
        if len(resp["result"]) != 0:
            for result in resp["result"]:
               if "text" in result["message"]:
                if result["message"]["text"] == '/start':
                        Thread(target = msgStart, args = (result,)).start()
                elif result["message"]["text"].startswith('https://open.spotify.com/track'):
                        Thread(target = msgSpotifyLink, args = (result,)).start()
            offset=resp["result"][-1]["update_id"] + 1  
        
def msgStart(result):
    reqParam={
              "chat_id":result["message"]["chat"]["id"],
              "text":startMsg
             }
    events_handler.sendMsg(reqParam)
    
def msgSpotifyLink(result):
    rawTitle=spotify_helper.getTitleArtists(result["message"]["text"])
    fileName=youtube_helper.getYTDownload(rawTitle)
    audio_file=open(fileName,'rb')
    reqParam={
             "chat_id":result["message"]["chat"]["id"],
             "reply_to_message_id":result["message"]["message_id"]
             }
    files={
    "audio":audio_file
    }
    events_handler.sendAudio(reqParam,files)

#Entry Point    
events_reader()