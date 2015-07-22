#!/usr/bin/env python
# encoding: utf-8

from line import LineClient
from Tkinter import *

root = Tk()
root.title("Line")

profile = StringVar()

testt = Label(root, textvariable=profile)
def UserLogin():
    username = usernameent.get()
    password = Passwordent.get()
    client = LineClient(username, password, is_mac=False, com_name="Linux_line")
    profile.set(client.profile)
    # profile = client.profile

usernamelbl = Label(root, text="UserName:")
passwordlbl = Label(root, text="Password:")

usernameent = Entry(root)
Passwordent = Entry(root)

loginbtn = Button(root, text="Login", command=UserLogin)

usernamelbl.pack()
usernameent.pack()
passwordlbl.pack()
Passwordent.pack()
loginbtn.pack()
testt.pack()

root.mainloop()
