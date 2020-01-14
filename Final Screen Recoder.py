import tkinter
#import tkMessageBox
import time
import os
from tkinter import *
import webbrowser
import cv2
import numpy as np
import pyautogui
import winsound
import logging
from pynput.mouse import Listener
logging.basicConfig(filename="mouse_log.txt",level=logging.DEBUG, format="%(asctime)s: %(message)s")

FREQ = 2500
DUR = 150
screen_size=(1366,768)
fourcc=cv2.VideoWriter_fourcc(*"XVID")
out=cv2.VideoWriter("output.avi",fourcc,5.0,(screen_size))


after_id = None
secs = 0
def on_click(x,y,button,pressed):
    logging.info("Mouse Clicked at ".format(x,y,button))
def ScreenRe():
    global after_id
    global secs
    # with Listener(on_click=on_click) as listener:
    #     listener.join()
    secs += 1
    if secs % 1 == 0:  # every other second
        img = pyautogui.screenshot()
        frame=np.array(img)
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        out.write(frame)
        cv2.imshow('show',frame)
    after_id = top.after(1000, ScreenRe)  # check again in 1 second

def start():
    global secs
    secs = 0
    ScreenRe()  # start repeated checking

def stop():
    global after_id
    if after_id:
        top.after_cancel(after_id)
        after_id = None

top = tkinter.Tk()
top.title('ScreenRecorder')
top.geometry('200x100')

recordphoto = PhotoImage(file='record.png')
stopPhoto= PhotoImage(file='stop.png')
startButton = tkinter.Button(top, image=recordphoto, command=start)
stopButton = tkinter.Button(top, image=stopPhoto, command=stop)
startButton.pack()
stopButton.pack()
top.mainloop()