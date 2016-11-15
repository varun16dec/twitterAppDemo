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
            jsonData=json.loads(data)
            print(data)
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

if __name__ == '__main__':
    auth=getTwitterAuth()
    twitterStream=Stream(auth,CustomListener())
    twitterStream.userstream(encoding='utf-8')

