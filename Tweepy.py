#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tweepy
import time
import webbrowser


# In[2]:


ACCESS_TOKEN = '2712395911-iuFwRZCt2Q2GlptqQY3GKAadaSDXy0dNr5DZtQq'
ACCESS_SECRET = 'OUPZxFtXW8g7IdSTzX5a6Ib5HjscrZgt1s7kfdjALzpu4'
CONSUMER_KEY = 'AYw8duD2eqWRXN6utsfbYRgDl'
CONSUMER_SECRET = 'NzLMSEzpnHwkabi3GsOM8Vx2U5WkLVWxjmML1IDAVGHp2bzVi6'


# In[3]:


callback_uri= 'oob'


# In[4]:


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET,callback_uri)
redirect_url = auth.get_authorization_url()
print(redirect_url)


# In[5]:


webbrowser.open(redirect_url)


# In[6]:


user_pin_input = input("What is the pin value? ")


# In[7]:


auth.get_access_token(user_pin_input)







