#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tweepy
import time
import webbrowser


# In[3]:


ACCESS_TOKEN = '2712395911-iuFwRZCt2Q2GlptqQY3GKAadaSDXy0dNr5DZtQq'
ACCESS_SECRET = 'OUPZxFtXW8g7IdSTzX5a6Ib5HjscrZgt1s7kfdjALzpu4'
CONSUMER_KEY = 'AYw8duD2eqWRXN6utsfbYRgDl'
CONSUMER_SECRET = 'NzLMSEzpnHwkabi3GsOM8Vx2U5WkLVWxjmML1IDAVGHp2bzVi6'
bearer_token='AAAAAAAAAAAAAAAAAAAAAPIXbgEAAAAAOfvRG%2B7YjOXHyR%2FqcFmPeXX8WNA%3D9C5LjlxUKCI89RRCZ7NQPra4zL0NDEs9mIOvj9BM73JhGXZFtB'


# In[4]:


callback_uri= 'oob'


# In[5]:


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET,callback_uri)
redirect_url = auth.get_authorization_url()
print(redirect_url)


# In[6]:


webbrowser.open(redirect_url)


# In[7]:


user_pin_input = input("What is the pin value? ")


# In[8]:


auth.get_access_token(user_pin_input)


# In[9]:


print(auth.access_token,auth.access_token_secret)


# In[10]:


api = tweepy.API(auth)


# In[11]:


#will not work without elevated access from twitter
#me = api.get_user()
#print(me.screen_name)


# In[12]:


#Must use client if you only have essential access
client = tweepy.Client(consumer_key=CONSUMER_KEY,
                       consumer_secret=CONSUMER_SECRET,
                       access_token=ACCESS_TOKEN,
                       access_token_secret=ACCESS_SECRET)


# In[13]:



#response = client.create_tweet(text='hello world')

#print(response)


# In[14]:


client = tweepy.Client(bearer_token=bearer_token)

# Replace User ID
id = '44196397'

tweets = client.get_liked_tweets(id=id, tweet_fields=['context_annotations','created_at','geo'])

for tweet in tweets.data:
    print(tweet)


# In[15]:


#nft tweet and shows all users who retweeted the tweet
id = '1519300117265801216'
users = client.get_retweeters(id=id, user_fields=['profile_image_url'])

for user in users.data:
    print(user)


# In[16]:


# mute a user
id = '1354481209187856385'
result = client.mute(target_user_id=user.id)
print(f"user muted? {result.data['muting']}")

