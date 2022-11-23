#!/usr/bin/env python
# coding: utf-8

# In[21]:


from tkinter import *
from tkinter import ttk
import tkinter.font as font
from ChainBlockMethods import blockUser, unblockUser, scanTweets
import webbrowser
from PIL import Image, ImageTk
from pathlib import Path

def call_back(event):
    webbrowser.open("https://github.com/jmale021/ChainBlock")
    
#def get_auth_url():
    #global oauth1_user_handler
    #oauth1_user_handler = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, callback = "oob")
    #webbrowser.open(oauth1_user_handler.get_authorization_url())
    
#def complete_auth():
   #global entry
   #verifier = entry.get()
   #global access_token
   #global access_token_secret
   #access_token, access_token_secret = oauth1_user_handler.get_access_token(verifier)
    
#def get_api():
    #api = tweepy.API(oauth1_user_handler, wait_on_rate_limit = True)
    #return api
    
def block_actions():
    #print("Program the block actions")
    username = blockUser()
    block_box.insert(INSERT, username + " has been blocked!\n")
    
def unblock_actions():
    #print("Program the unblock actions")
    username = unblockUser()
    block_box.insert(INSERT, username + " has been unblocked!\n")
    
def analytics_actions():
    #print("Program the analytics actions")
    path_to_file = 'block_targets.csv'
    path = Path(path_to_file)
    
    if path.is_file():
        block_box.insert(INSERT, path_to_file + " found!\n")
        
    else:
        block_box.insert(INSERT, path_to_file + " does not exist!\n")
    
def scan_actions():
    users = scanTweets()
    for name in users:
        block_box.insert(INSERT, name + " is a block target!\n")


# In[22]:


root = Tk()
root.title('ChainBlock')
icon_photo = Image.open("ChainBlock_logo_16.jpeg")
icon = ImageTk.PhotoImage(icon_photo)
root.iconphoto(False, icon)
root.geometry("700x510")

frame = Frame(root)
frame.pack()

bottom_frame = Frame(root)
bottom_frame.pack(side = BOTTOM)

font_size = font.Font(size = 16)

title_text = Label(frame, text = "ChainBlock Ver. 2.0", bg = "red", fg = "white")
title_text['font'] = font_size
title_text.pack(fill = X)
title_text.bind("<Button-1>", call_back)

#auth_button = Button(frame, text = "Authenticate", fg = "red", command = get_auth_url)
#auth_button['font'] = font_size
#auth_button.pack(side = TOP, pady = "5")

#entry = Entry(root, width = 7)
#entry.focus_set()
#entry.pack(side = TOP, pady = "5")

#pin_button = Button(frame, text = "Confirm PIN", fg = "red", command = complete_auth)
#pin_button['font'] = font_size
#pin_button.pack(side = TOP, pady = "5")

block_button = Button(frame, text = "Block People", width = "20", fg = "red", command = block_actions)
block_button['font'] = font_size
block_button.pack(side = TOP, pady = "5")

unblock_button = Button(frame, text = "Unblock People", width = "20", fg = "red", command = unblock_actions)
unblock_button['font'] = font_size
unblock_button.pack(side = TOP, pady = "5")

analytics_button = Button(frame, text = "View Analytics", width = "20", fg = "red", command = analytics_actions)
analytics_button['font'] = font_size
analytics_button.pack(side = TOP, pady = "5")

scan_button = Button(frame, text = "Scan", width = "20", fg = "red", command = scan_actions)
scan_button['font'] = font_size
scan_button.pack(side = TOP, pady = "5")

block_box = Text(bottom_frame, fg = "red", width = "50", height = "10", borderwidth = "2", relief = "ridge")
block_box['font'] = font_size
block_box.pack(side = BOTTOM, pady = "10")

root.mainloop()


# In[ ]:




