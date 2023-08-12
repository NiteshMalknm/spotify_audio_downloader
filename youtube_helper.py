from Singleton import Singleton

def getYTUrl(rawTitle):
    ydlObj=Singleton.getydlInstance()
    metaData=ydlObj.extract_info(f"ytsearch:{rawTitle}", download=False)['entries'][0]
    return metaData["url"]
    
def getYTDownload(rawTitle):
    ydlObj=Singleton.getydlInstance()
    metaData=ydlObj.extract_info(f"ytsearch:{rawTitle}", download=True)['entries'][0]
    return metaData['requested_downloads'][0]['filepath']