# -*- coding: utf-8 -*-

from PIL import Image
import cv2
import time
from pynput.keyboard import Key, Controller
import pyperclip as pc

ASCII_CHARS = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'.⠀'

'''
convert vid to frames
1 resize
2 convert to grayscale
3 convert pixel to ascii char
'''

keyboard = Controller()

keyboard.press(Key.ctrl)
keyboard.release(Key.ctrl)

def resize(img):
    return img.resize((36, 11))

def grayscale(img):
    return img.convert("L")

def convert_ascii(img):
    img = grayscale(resize(img))
    imgpix = list(img.getdata())
    chars = [ASCII_CHARS[int(pixel/3.69)] for pixel in imgpix]
    chars = "".join(chars)
    
    asciiout = [chars[i:i+36] for i in range(0, len(chars), 36)]
    return "\n".join(asciiout)

w = input()

time.sleep(2)

vid = cv2.VideoCapture("FILEPATH")
frame = []
timenow = 0
vidlen = 219
while timenow <= vidlen*1000:
    print(timenow)
    vid.set(0, timenow)
    success, img = vid.read()
    if success:
        cv2.imwrite("output.jpg", img)
    frame.append(convert_ascii(Image.open("output.jpg")))
    if w != "w":
        print(frame[-1])
        timenow += 100
        time.sleep(0.3)
    else:
        pc.copy(frame[-1])
        with keyboard.pressed(Key.ctrl):
            keyboard.press("v")
            keyboard.release("v")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        timenow += 100
        time.sleep(0.3)
