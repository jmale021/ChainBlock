#!/usr/bin/env python
# coding: utf-8

# In[55]:



#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tweepy
import re


# In[2]:


access_token = '2712395911-ehqFfEGiM5COVQg149vqT5miIcvM8SorJmchg0N'
access_token_secret = 'K9GuOkmrf1PuwUjUA7lblH3KGotsvIev4vvyYtGxu9Wd0'
consumer_key = 'LKi9NfPzoRzF7Ha54SAd9bezO'
consumer_secret = 'PO6jkanwHnPltE9umZtTFnElEJ9GSWuxpso3SsEixg5mH3tMf2'


# In[3]:


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


# In[4]:


# If the authentication was successful, this should print the
# screen name / username of the account
print(api.verify_credentials().screen_name)


# In[5]:


_id = "103770785"
user = api.get_user(user_id=_id)


# In[6]:


try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print('Error! Failed to get request token.')


# In[7]:


#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)


# In[8]:


user = api.get_user(screen_name='NFT_Kaneki')
print(user.id)


# In[9]:


#print(user.screen_name)
#print(user.followers_count)
#for friend in user.friends():
#   print(friend.screen_name)#Amount of followers


# In[10]:
followers = api.get_followers(user_id = api.get_user(screen_name = "NFT_Kaneki"), count = 30)
#print(followers)
print()
print("FOLLOWERS:")
for follower in followers:
    print(follower.screen_name + ",")
    if("NFT" in follower.screen_name):
        print("bruh blocked")
# check followers usernames to block        
followers = api.get_followers(screen_name = "NFT_Kaneki", count = 30)
#print(followers)
print()
print("FOLLOWERS:")
for follower in followers:
    print(follower.screen_name + ",")
    #if("NFT" in follower.screen_name):
        #print("bruh blocked")
    #if("Nft" in follower.screen_name):
        #print("bruh blocked")
    #if(re.search(r"Nft",follower.screen_name)):
        #print("bruh blocked")
    if(re.search(r"nft",follower.screen_name.lower())):
        print("bruh blocked")
print(api.get_user(screen_name = "NFT_Kaneki"))


# In[ ]:





# In[ ]:




