#!/usr/bin/env python
# coding: utf-8

# In[15]:


import requests
import json


channel_id = "UCUHHRiLeH7sO46GJBRGweag"
api_key = "AIzaSyAJDQModwPQ6zah6VUdl32iOO7sIIYEQXI"


base_url = "https://www.googleapis.com/youtube/v3/"


channel_params = {
    "part": "snippet,statistics",
    "id": channel_id,
    "key": api_key
}


channel_response = requests.get(base_url + "channels", params=channel_params)
channel_data = channel_response.json()


channel_name = channel_data["items"][0]["snippet"]["title"]
subscription_count = channel_data["items"][0]["statistics"]["subscriberCount"]
view_count = channel_data["items"][0]["statistics"]["viewCount"]
video_count = channel_data["items"][0]["statistics"]["videoCount"]


print(f"Channel name: {channel_name}")
print(f"Subscription count: {subscription_count}")
print(f"View count: {view_count}")
print(f"Video count: {video_count}")


playlist_params = {
    "part": "snippet",
    "channelId": channel_id,
    "key": api_key
}


playlist_response = requests.get(base_url + "playlists", params=playlist_params)
playlist_data = playlist_response.json()


for playlist in playlist_data["items"]:
    playlist_title = playlist["snippet"]["title"]
    playlist_id = playlist["id"]
    print(f"Playlist title: {playlist_title}")
    print(f"Playlist ID: {playlist_id}")


# In[6]:


api_key='AIzaSyAJDQModwPQ6zah6VUdl32iOO7sIIYEQXI'


# In[ ]:


api_service_name = "youtube"
    api_version = "v3"
    

    
    
    youtube = build(
        api_service_name, api_version, developerKey=api_key)

    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id="@dbagenesis"
    )
    response = request.execute()

    print(response)


# In[7]:


from googleapiclient.discovery import build
import pandas as pd
import seaborn as sns


# In[6]:


pip install google-api-python-client


# In[27]:


api_key = 'AIzaSyCb4klqpmrUL94sCT5DUb2pqB830KDykiE'
channel_id = 'UCghywW5RkhfCT-58iWdwEUg'
youtube = build('youtube','v3',developerKey=api_key)


# In[29]:


def get_channel_stats(youtube, channel_id):
    request = youtube.channels().list(
                part ='snippet,contentDetails,statistics',
                id= 'channel_id')
    response = request.execute()
    return response


# In[34]:


api_key = 'AIzaSyAJDQModwPQ6zah6VUdl32iOO7sIIYEQXI'
channel_id = 'UC_x5XG1OV2P6uZZ5FSM9Ttw'
youtube = build('youtube','v3',developerKey=api_key)
def get_channel_stats(youtube, channel_id):
    request = youtube.channels().list(
                part ='snippet,contentDetails,statistics',
                id= 'channel_id')
    response = request.execute()
    return response



   


# In[35]:


get_channel_stats(youtube, channelId)


# In[47]:


def get_channel_stats(youtube, channel_id):
    request = youtube.channels().list(
                part='snippet,contentDetails,statistics',
                id=channel_id)
    response = request.execute()
    
    data = dict(Channel_Id=channel_id,
          Channel_name=response['items'][0]['snippet']['title'],
          Subscribers=response['items'][0]['statistics']['subscriberCount'],
          Views=response['items'][0]['statistics']['viewCount'],
          Total_videos=response['items'][0]['statistics']['videoCount'],
          playlist_id=response['items'][0]['contentDetails']['relatedPlaylists']['uploads']) 
    
    return data


# In[48]:


get_channel_stats(youtube, channel_id)


# In[32]:


import os


# In[49]:


channel_response = youtube.channels().list(
    part='snippet,statistics',
    id=channel_id
).execute()

# Extract the channel details
channel_data = channel_response['items'][0]
channel_title = channel_data['snippet']['title']
subscriber_count = channel_data['statistics']['subscriberCount']

# Print the channel details
print(f'Channel title: {channel_title}')
print(f'Subscriber count: {subscriber_count}')

# Get the playlist details
playlist_response = youtube.playlists().list(
    part='snippet,contentDetails',
    channelId=channel_id
).execute()

# Extract the playlist details
playlist_data = playlist_response['items'][0]
playlist_title = playlist_data['snippet']['title']
playlist_id = playlist_data['id']

# Print the playlist details
print(f'Playlist title: {playlist_title}')
print(f'Playlist ID: {playlist_id}')

# Get the playlist items
playlist_items = []
next_page_token = None
while True:
    playlist_items_response = youtube.playlistItems().list(
        part='snippet',
        playlistId=playlist_id,
        maxResults=50,
        pageToken=next_page_token
    ).execute()

    playlist_items.extend(playlist_items_response['items'])

    next_page_token = playlist_items_response.get('nextPageToken')
    if not next_page_token:
        break

# Extract the video details from the playlist items
videos = []
for item in playlist_items:
    video_data = item['snippet']['resourceId']['videoId']
    video_title = item['snippet']['title']
    videos.append({
        'id': video_data,
        'title': video_title
    })

# Print the video details
for video in videos:
    print(f'Video ID: {video["id"]}')
    print(f'Video title: {video["title"]}')

    # Get the video details
    video_response = youtube.videos().list(
        part='statistics',
        id=video['id']
    ).execute()

    # Extract the video statistics
    video_data = video_response['items'][0]
    like_count = video_data['statistics']['likeCount']
    comment_count = video_data['statistics']['commentCount']

    # Print the video statistics
    print(f'Likes: {like_count}')
    print(f'Comments: {comment_count}')


# In[52]:


api_key = 'AIzaSyAJDQModwPQ6zah6VUdl32iOO7sIIYEQXI'
channel_ids = ["UCghywW5RkhfCT-58iWdwEUg",  #Vahcheff channelid
              "UCjNgqJ_FMLntYVzq7daw1TQ",  #Druve channelid
            "UCKDxs_s5a-IeGgnvcbCvGVg"    # Ramkumar swaminadhan channelid
             ]
youtube = build('youtube','v3',developerKey=api_key)


# In[57]:


def get_channel_stats(youtube, channel_ids):
    request = youtube.channels().list(
                part='snippet,contentDetails,statistics',
                id=','.join(channel_ids))
    response = request.execute()
    
    data = dict(Channel_Id=channel_id,
          Channel_name=response['items'][0]['snippet']['title'],
          Subscribers=response['items'][0]['statistics']['subscriberCount'],
          Views=response['items'][0]['statistics']['viewCount'],
          Total_videos=response['items'][0]['statistics']['videoCount'],
          playlist_id=response['items'][0]['contentDetails']['relatedPlaylists']['uploads']) 
    
    return response


# In[58]:


get_channel_stats(youtube, channel_ids)


# In[61]:


def get_channel_stats(youtube, channel_ids):
    all_data =[]
    request = youtube.channels().list(
                part='snippet,contentDetails,statistics',
                id=','.join(channel_ids))
    response = request.execute()
    for i in range(len(response['items'])):
        data = dict(Channel_Id=channel_id,
                  Channel_name=response['items'][i]['snippet']['title'],
                  Subscribers=response['items'][i]['statistics']['subscriberCount'],
                  Views=response['items'][i]['statistics']['viewCount'],
                  Total_videos=response['items'][i]['statistics']['videoCount'],
                  playlist_id=response['items'][i]['contentDetails']['relatedPlaylists']['uploads'])
        all_data.append(data)
    
    return all_data


# In[62]:


get_channel_stats(youtube, channel_ids)


# In[64]:


channel_statistics = get_channel_stats(youtube,channel_ids)


# In[65]:


Channel_data=pd.DataFrame(channel_statistics)
Channel_data


# In[67]:


type(channel_data)


# In[69]:


pip install psycopg2


# In[73]:


import psycopg2
get_ipython().system('pip install pymongo')


# In[74]:


import pandas as pd
import json


# In[75]:


from pymongo import MongoClient

