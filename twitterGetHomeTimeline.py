import json
from tweepy import Cursor
from twitterClient import getTwitterClient

if __name__=='__main__':
    client=getTwitterClient()

    with open('home_timeline.jsonl','w') as f:
        for page in Cursor(client.home_timeline,count=200).pages(4):
            for status in page:
                f.write(json.dumps(status._json)+"\n")
