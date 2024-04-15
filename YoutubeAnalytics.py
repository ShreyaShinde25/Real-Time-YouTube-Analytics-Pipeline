import requests
from constants import YOUTUBE_API_KEY
from pprint import pprint
import json

if __name__=="__main__":
    response=requests.get("https://www.googleapis.com/youtube/v3/videos",
                          {
                              'key':YOUTUBE_API_KEY,
                              'id':"8EClhdzv16k",
                              'part': 'snippet,statistics,status' 
                          })

# print(response.text)
response=json.loads(response.text)['items']

for video in response:
    video_res={
   'title':video['snippet']['title'],
   'likes':int(video['statistics'].get('likeCount',0)),
   'comments':int(video['statistics'].get('commentCount',0)),
   'views':int(video['statistics'].get('viewCount',0)),
   'favorites':int(video['statistics'].get('favoriteCount',0)),
   'thumnnail':video['snippet']['thumbnails']['default']['url']
    }

    print(pprint(video_res))
    


