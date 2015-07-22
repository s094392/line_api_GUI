#!/usr/bin/env python
# encoding: utf-8

from line import LineClient, LineBase
import Tkinter as tk

class Loginwindow:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.usernamelbl = tk.Label(master, text="UserName:")
        self.passwordlbl = tk.Label(master, text="Password:")
        self.usernameent = tk.Entry(master)
        self.passwordent = tk.Entry(master, show="*")
        self.loginbtn = tk.Button(master, text="login", command=self.login)
        self.usernamelbl.pack()
        self.usernameent.pack()
        self.passwordlbl.pack()
        self.passwordent.pack()
        self.loginbtn.pack()

    def login(self):
        self.username = self.usernameent.get()
        self.password = self.passwordent.get()
        self.client = LineClient(self.username, self.password, is_mac=False, com_name="Linux_line")
        print self.client.authToken
        self.mainwindow = tk.Toplevel(self.master)
        self.app = MainWindow(self.mainwindow, self.client)


class MainWindow:
    def __init__(self, master, client):
        self.master = master
        self.client = client
        self.profile_id = tk.StringVar()
        self.profile_id.set(self.client.profile.id)
        self.profile_name = tk.StringVar()
        self.profile_name.set(self.client.profile.name)
        self.profile_statusMessage = tk.StringVar()
        self.profile_statusMessage.set(self.client.profile.statusMessage)
        self.frame= tk.Frame(master)
        self.lineid = tk.Label(self.frame, textvariable=self.profile_id)
        self.linename = tk.Label(self.frame, textvariable=self.profile_name)
        self.linestatusMessage = tk.Label(self.frame, textvariable=self.profile_statusMessage)
        self.lineid.pack()
        self.linename.pack()
        self.linestatusMessage.pack()
        self.frame.pack()
        self.contacts = []

        for i in range(len(self.client.contacts)):
            contact_name = tk.StringVar()
            contact_name.set(self.client.contacts[i].name)
            self.contacts.append(tk.Button(self.frame, textvariable = contact_name, command = lambda i=i:self.gochat(i)).pack())

    def gochat(self, num):
        self.chatwindow = tk.Toplevel(self.master)
        self.app = Chatroom(self.chatwindow, num, self.client)

class Chatroom:
    def __init__(self, master, num, client):
        self.master = master
        self.frame = tk.Frame(master)
        self.client = client
        # self.frame.title(self.client.contact[num].name)
        self.chatroomname = tk.StringVar()
        self.chatroomname.set(self.client.contacts[num].name)
        self.chatroomnamelbl = tk.Label(self.frame, textvariable=self.chatroomname)
        self.inputboxent = tk.Entry(self.frame)
        def _wrapper():
            self.submitMessage(self.inputboxent.get(), num)
            self.inputboxent.delete(0, 'end')
        self.submitbtn = tk.Button(self.frame, text="Submit", command=_wrapper)
        self.chatroomnamelbl.pack()
        self.inputboxent.pack()
        self.submitbtn.pack()
        self.frame.pack()

    def submitMessage(self, message, id):
        self.client.contacts[id].sendMessage(message)

def main():
    root = tk.Tk()
    root.title("Line")
    root.geometry("350x650")
    app = Loginwindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()
# testt = Label(root, textvariable=profile)
# def UserLogin():
    # username = usernameent.get()
    # password = Passwordent.get()
    # client = LineClient(username, password, is_mac=False, com_name="Linux_line")
    # profile.set(client.profile)
    # MainWindow()
    # # profile = client.profile

# def MainWindow():
    # main = Tk()
    # main.title("Line")
    # line_name = Label(main, textvariable=profile).pack()
    # main.mainloop()

# usernamelbl = Label(root, text="UserName:")
# passwordlbl = Label(root, text="Password:")

# usernameent = Entry(root)
# Passwordent = Entry(root)

# loginbtn = Button(root, text="Login", command=UserLogin)

# usernamelbl.pack()
# usernameent.pack()
# passwordlbl.pack()
# Passwordent.pack()
# loginbtn.pack()
# testt.pack()

# root.mainloop()
