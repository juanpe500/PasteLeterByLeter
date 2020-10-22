import os
import sys
import win32clipboard
import time
from pynput.keyboard import Key, Controller
import random

os.system("cls")
win32clipboard.OpenClipboard()
data = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()
speed=0.05

print("Pasting in 3 seconds, go to your editor...")
time.sleep(3)

def split(word): 
    return [char for char in word] 

words = data.split(" ")
keyboard = Controller()

def pasteStr(s):
    while True:
        try:
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(s)
            win32clipboard.CloseClipboard()
            keyboard.press(Key.ctrl)
            keyboard.press('v')
            keyboard.release(Key.ctrl)
            keyboard.release('v')
            if s == ".":
                keyboard.press(Key.ctrl)
                keyboard.press(Key.space)
                keyboard.release(Key.ctrl)
                keyboard.release(Key.space)
                time.sleep(random.randint(15,40)/100) 
            time.sleep(speed)
            return
        except:
            time.sleep(0.1)

helper=False
for i in words:
    for j in split(i):
        if '\n' in j or '\r' in j:
            if helper == True:
                pasteStr(j)
            helper=not helper
        else:
            pasteStr(j)
    pasteStr(" ")