import requests
from Singleton import Singleton

env=Singleton.getEnvInstance();

def sendMsg(reqParam):
    requests.get(env.get('DEFAULT','telegram_baseurl')+env.get('DEFAULT','bot_token')+env.get('DEFAULT','telegram_sendmsgurl'),data=reqParam)
    
def sendAudio(reqParam,files):
    resp=requests.get(env.get('DEFAULT','telegram_baseurl')+env.get('DEFAULT','bot_token')+env.get('DEFAULT','telegram_sendaudiourl'),data=reqParam,files=files)
    print(resp.text)
    