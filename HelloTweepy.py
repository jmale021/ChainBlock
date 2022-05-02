#!/usr/bin/env python
# coding: utf-8

# In[19]:


import tweepy


# In[20]:


access_token = '2712395911-ehqFfEGiM5COVQg149vqT5miIcvM8SorJmchg0N'
access_token_secret = 'K9GuOkmrf1PuwUjUA7lblH3KGotsvIev4vvyYtGxu9Wd0'
consumer_key = 'LKi9NfPzoRzF7Ha54SAd9bezO'
consumer_secret = 'PO6jkanwHnPltE9umZtTFnElEJ9GSWuxpso3SsEixg5mH3tMf2'


# In[21]:


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


# In[22]:


# If the authentication was successful, this should print the
# screen name / username of the account
print(api.verify_credentials().screen_name)


# In[23]:


_id = "103770785"
user = api.get_user(user_id=_id)


# In[24]:


try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print('Error! Failed to get request token.')


# In[25]:


public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)


# In[26]:


user = api.get_user(screen_name='NFT_Kaneki')
print(user.id)


# In[27]:


print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
   print(friend.screen_name)#Amount of followers


# In[29]:



api.create_block(screen_name='NFT_Kaneki')


# In[ ]:




