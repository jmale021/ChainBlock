#!/usr/bin/env python
# coding: utf-8

# In[120]:


# In[27]:



#!/usr/bin/env python
# coding: utf-8


# In[121]:


# In[1]:


import tweepy
import re
import requests
from PIL import Image


# In[122]:


# In[2]:


access_token = '2712395911-ehqFfEGiM5COVQg149vqT5miIcvM8SorJmchg0N'
access_token_secret = 'K9GuOkmrf1PuwUjUA7lblH3KGotsvIev4vvyYtGxu9Wd0'
consumer_key = 'LKi9NfPzoRzF7Ha54SAd9bezO'
consumer_secret = 'PO6jkanwHnPltE9umZtTFnElEJ9GSWuxpso3SsEixg5mH3tMf2'


# In[123]:


# In[3]:


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
# This call should automatically manage rate limits by pausing if a limit is reached
# api - tweepy.API(auth, wait_on_rate_limit = True)


# In[124]:


# In[4]:


# If the authentication was successful, this should print the
# screen name / username of the account
print(api.verify_credentials().screen_name)


# In[125]:


# In[5]:


_id = "103770785"
user = api.get_user(user_id=_id)


# In[126]:


# In[6]:


try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print('Error! Failed to get request token.')


# In[127]:


# In[7]:


#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)


# In[128]:


# In[8]:


user = api.get_user(screen_name='NFT_Kaneki')
print(user.id)
print(user.name)
print(user.screen_name)
avatar = user.profile_image_url
image = Image.open(requests.get(avatar, stream=True).raw)
image.show()


# In[129]:


# In[9]:


#print(user.screen_name)
#print(user.followers_count)
#for friend in user.friends():
#   print(friend.screen_name)#Amount of followers


# In[130]:


# In[30]:


generalBlockList = ["LeoStudio_LS","TheHoodersNFT","NFTEngineer","NFT_Origins"]
followers = api.get_followers(screen_name = "TheHoodersNFT")
# check follows of a user for NFT accounts in generasl block list
for follower in followers:
    for target in generalBlockList:
        if(target in follower.screen_name):
            print(target + "Is a BLOCK TARGET ^^.")
        else: 
            print("Not a Block Target")


# In[ ]:


# In [31]:
# This block automatically scans users tweeting using the specified hashtag in printer.filter field
class StreamListener(tweepy.Stream):
    def on_status(self, status):
        print(status.user.screen_name + " tweeted: " + status.text)

def streamTweets():
    printer = StreamListener(consumer_key, consumer_secret, access_token, access_token_secret)
    printer.filter(track = ["NewNFTProfilePic"])
    
streamTweets()    


# In[ ]:




