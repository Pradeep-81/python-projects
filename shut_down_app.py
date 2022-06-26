from tkinter import *
import os


def restart():
    os.system("shutdown /r /t 1")


def restart_with_time():
    os.system("shutdown /r /t 20")


def shutdown():
    os.system("shutdown /s /t 1")


def logout():
    os.system("shutdown -l")


shut_down = Tk()

shut_down.title("shut down")
shut_down.geometry("500x500")
shut_down.config(background="pink")

r_button = Button(shut_down, text="Restart", font=("Time New Roman", 20, "bold"), relief=RAISED, cursor="plus",
                  command=restart)
r_button.place(x=200, y=50, height=50, width=150)

rt_button = Button(shut_down, text="Restart Time", font=("Time New Roman", 15, "bold"), relief=RAISED, cursor="plus",
                   command=restart_with_time)
rt_button.place(x=200, y=150, height=50, width=150)

s_button = Button(shut_down, text="Shut down", font=("Time New Roman", 15, "bold"), relief=RAISED, cursor="plus",
                  command=shutdown)
s_button.place(x=200, y=250, height=50, width=150)

l_button = Button(shut_down, text="Logout", font=("Time New Roman", 15, "bold"), relief=RAISED, cursor="plus",
                  command=logout)
l_button.place(x=200, y=350, height=50, width=150)

shut_down.mainloop()
