#!/usr/bin/env python
# coding: utf-8

# In[132]:


# In[27]:



#!/usr/bin/env python
# coding: utf-8


# In[133]:


# In[1]:


import tweepy
import re
import requests
from PIL import Image


# In[134]:


# In[2]:


access_token = '2712395911-ehqFfEGiM5COVQg149vqT5miIcvM8SorJmchg0N'
access_token_secret = 'K9GuOkmrf1PuwUjUA7lblH3KGotsvIev4vvyYtGxu9Wd0'
consumer_key = 'LKi9NfPzoRzF7Ha54SAd9bezO'
consumer_secret = 'PO6jkanwHnPltE9umZtTFnElEJ9GSWuxpso3SsEixg5mH3tMf2'


# In[135]:


# In[3]:


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
# This call should automatically manage rate limits by pausing if a limit is reached
# api - tweepy.API(auth, wait_on_rate_limit = True)


# In[143]:


# In [31]:
# This block automatically scans users tweeting using the specified hashtag in printer.filter field
class StreamListener(tweepy.Stream):
    def on_status(self, status):
        print(status.user.screen_name + " tweeted: " + status.text)

def streamTweets():
    printer = StreamListener(consumer_key, consumer_secret, access_token, access_token_secret)
    printer.filter(track = ["NewNFTProfilePic"])

    


# In[ ]:




