#!/usr/bin/env python
# coding: utf-8

import tkinter.font as font
import webbrowser
from functools import partial
from pathlib import Path
from tkinter import *
from tkinter import ttk

from ChainBlockMethods import blockUser, unblockUser, scanTweets
from PIL import Image, ImageTk


def call_back(event):
    webbrowser.open("https://github.com/jmale021/ChainBlock")


def unblockWindow():
    newWindow = Toplevel(root)
    newWindow.title("Unblock Users")
    icon_photo = Image.open("ChainBlock_logo_16.jpeg")
    icon = ImageTk.PhotoImage(icon_photo)
    newWindow.iconphoto(False, icon)
    newWindow.geometry("300x300")

    title = Label(newWindow, text="Select a user to unblock.",  bg="red", fg="white")
    title["font"] = font_size
    title.pack(fill=X)

    # read in the list of blocked users to fill a dropdown menu
    with open("blocked_users.txt", "r") as blocked_users:
        # strip newline characters from text file
        temp = blocked_users.readlines()
        targets = [x.strip("\n") for x in temp]

    dropdown = ttk.Combobox(newWindow, values=targets, state="readonly")
    dropdown.pack(side=TOP, pady="10")

    unblock_confirm = Button(
        newWindow,
        text="Unblock",
        width="20",
        compound=CENTER,
        fg="red",
        command=partial(unblock_actions, dropdown),
    )
    unblock_confirm["font"] = font_size
    unblock_confirm.pack(side=BOTTOM, pady="10")


# def get_auth_url():
# global oauth1_user_handler
# oauth1_user_handler = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, callback = "oob")
# webbrowser.open(oauth1_user_handler.get_authorization_url())

# def complete_auth():
# global entry
# verifier = entry.get()
# global access_token
# global access_token_secret
# access_token, access_token_secret = oauth1_user_handler.get_access_token(verifier)

# def get_api():
# api = tweepy.API(oauth1_user_handler, wait_on_rate_limit = True)
# return api


def block_actions():
    with open("block_targets.txt", "r") as block_targets:
        with open("blocked_users.txt", "a") as blocked_users:
            # strip newline characters from text file
            temp = block_targets.readlines()
            targets = [x.strip("\n") for x in temp]
            # block all targeted users, provide user feedback and write to list of blocked users
            for user in targets:
                username = blockUser(user)
                block_box.insert(INSERT, "@" + username + " has been blocked!\n")
                blocked_users.write(username + "\n")
                # must also delete the blocked user from block_targets
                with open("block_targets.txt", "w+") as update_targets:
                    temp2 = update_targets.readlines()
                    for y in temp2:
                        if y.strip("\n") != user:
                            block_targets.write(y + "\n")


def unblock_actions(user):
    # grab the selected user, unblock and provide feedback
    target = user.get()
    username = unblockUser(target)
    block_box.insert(INSERT, "@" + username + " has been unblocked!\n")

    # must also delete the unblocked user from blocked_users
    with open("blocked_users.txt", "r") as update_blocks:
        temp = update_blocks.readlines()
    with open("blocked_users.txt", "w") as update_blocks:
        for x in temp:
            if x.strip("\n") != username:
                update_blocks.write(x)


def analytics_actions():
    path_to_file = "blocked_users.txt"
    path = Path(path_to_file)

    if path.is_file():
        block_box.insert(INSERT, path_to_file + " found!\n")

    else:
        block_box.insert(INSERT, path_to_file + " does not exist!\n")


def scan_actions():
    users = scanTweets()
    with open("block_targets.txt", "a+") as block_targets:
        for name in users:
            block_box.insert(INSERT, "@" + name + " is a block target!\n")
            block_targets.write(name + "\n")


root = Tk()
root.title("ChainBlock")
icon_photo = Image.open("ChainBlock_logo_16.jpeg")
icon = ImageTk.PhotoImage(icon_photo)
root.iconphoto(False, icon)
root.geometry("700x510")

frame = Frame(root)
frame.pack()

bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)

font_size = font.Font(size=16)

title_text = Label(frame, text="ChainBlock Ver. 2.0", bg="red", fg="white")
title_text["font"] = font_size
title_text.pack(fill=X)
title_text.bind("<Button-1>", call_back)

# auth_button = Button(frame, text = "Authenticate", fg = "red", command = get_auth_url)
# auth_button['font'] = font_size
# auth_button.pack(side = TOP, pady = "5")

# entry = Entry(root, width = 7)
# entry.focus_set()
# entry.pack(side = TOP, pady = "5")

# pin_button = Button(frame, text = "Confirm PIN", fg = "red", command = complete_auth)
# pin_button['font'] = font_size
# pin_button.pack(side = TOP, pady = "5")

scan_button = Button(frame, text="Scan", width="20", fg="red", command=scan_actions)
scan_button["font"] = font_size
scan_button.pack(side=TOP, pady="5")

block_button = Button(frame, text="Block People", width="20", fg="red", command=block_actions)
block_button["font"] = font_size
block_button.pack(side=TOP, pady="5")

unblock_button = Button(frame, text="Unblock People", width="20", fg="red", command=unblockWindow)
unblock_button["font"] = font_size
unblock_button.pack(side=TOP, pady="5")

analytics_button = Button(frame, text="View Analytics", width="20", fg="red", command=analytics_actions)
analytics_button["font"] = font_size
analytics_button.pack(side=TOP, pady="5")

block_box = Text(bottom_frame, fg="red", width="50", height="10", borderwidth="2", relief="ridge")
block_box["font"] = font_size
block_box.pack(side=BOTTOM, pady="10")

root.mainloop()
