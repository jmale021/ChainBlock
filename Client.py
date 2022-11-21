#!/usr/bin/env python
# coding: utf-8

# In[7]:


from tkinter import *
import tkinter.font as font
from Demo2 import StreamListener, streamTweets
import webbrowser
from PIL import Image, ImageTk

def call_back(event):
    webbrowser.open("https://github.com/jmale021/ChainBlock")
    
def block_actions():
    print("Program the block actions")
    
def unblock_actions():
    print("Program the unblock actions")
    
def analytics_actions():
    print("Program the analytics actions")


# In[8]:


root = Tk()
icon_photo = Image.open("ChainBlock_logo_16.jpeg")
icon = ImageTk.PhotoImage(icon_photo)
root.iconphoto(False, icon)
root.geometry("800x600")

frame = Frame(root)
frame.pack()

bottom_frame = Frame(root)
bottom_frame.pack(side = BOTTOM)

font_size = font.Font(size = 16)

title_text = Label(frame, text = "ChainBlock Ver. 2.0", bg = "red", fg = "white")
title_text['font'] = font_size
title_text.pack(fill = X)
title_text.bind("<Button-1>", call_back)

block_button = Button(frame, text = "Block People", fg = "red", command = block_actions)
block_button['font'] = font_size
block_button.pack(side = TOP, pady = "5")

unblock_button = Button(frame, text = "Unblock People", fg = "red", command = unblock_actions)
unblock_button['font'] = font_size
unblock_button.pack(side = TOP, pady = "5")

analytics_button = Button(frame, text = "View Analytics", fg = "red", command = analytics_actions)
analytics_button['font'] = font_size
analytics_button.pack(side = TOP, pady = "5")

#can cause lag and/or the app to crash, but functional
scan_button = Button(frame, text = "Scan", fg = "red", command = streamTweets)
scan_button['font'] = font_size
scan_button.pack(side = TOP, pady = "5")

root.mainloop()

