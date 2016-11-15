import sys
import time
import json
from tweepy import Stream
from tweepy.streaming import StreamListener
from twitterClient import getTwitterAuth

class CustomListener(StreamListener):
    """
    Custom StreamListener for streamin
    Twitter data
    """

    def on_data(self, data):
        try:
           # jsonData=json.loads(data)
           # print(str(jsonData['text']).encode("utf-8",errors="ignore"))
            text=getTweets(data)
            if text != None :
                print(getTweets(data))
                return True
        except BaseException as e:
            sys.stderr.write("Error on_data : {}\n".format(e))
            time.sleep(5)
        return True

    def on_error(self, status):
        if status == 420:
            sys.stderr.write("Rate limit Exceeded\n")
            return  False
        else:
            sys.stderr.write("Error{}\n".format(status))
            return True

def getTweets(data):
    jsonData=json.loads(data)
    return jsonData.get('text')
    

if __name__ == '__main__':
    auth=getTwitterAuth()
    twitterStream=Stream(auth,CustomListener())
    twitterStream.userstream(encoding='utf-8')

