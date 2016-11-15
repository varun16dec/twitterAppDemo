import os
import sys
from tweepy import Cursor
from twitterClient import getTwitterClient

if __name__=='__main__':
    client = getTwitterClient()

    for status in Cursor(client.home_timeline).items(100) : 
                         #process a single tweet
                         print(str(status.text).encode("utf-8",errors="ignore"))

