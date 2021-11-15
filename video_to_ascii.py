# -*- coding: utf-8 -*-

from PIL import Image
import cv2

ASCII_CHARS = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'.⠀'
FRAME_SIZE = (36, 11) # (width, height)
VIDEO_FILEPATH = "FILEPATH"
VIDEO_LENGTH = 219 # seconds

'''
convert vid to frames
1 resize
2 convert to grayscale
3 convert pixel to ascii char
'''

def resize(img):
    global FRAME_SIZE
    return img.resize(FRAME_SIZE)

def grayscale(img):
    return img.convert("L")

def convert_ascii(img):
    global FRAME_SIZE
    img = grayscale(resize(img))
    imgpix = list(img.getdata())
    chars = [ASCII_CHARS[int(pixel/3.69)] for pixel in imgpix]
    chars = "".join(chars)
    asciiout = [chars[i:i+FRAME_SIZE[0]] for i in range(0, len(chars), FRAME_SIZE[0])]
    return "\n".join(asciiout)

vid = cv2.VideoCapture(VIDEO_FILEPATH)
frame = []
timenow = 0
outputfile = open("output.txt", "w", encoding="utf-8")
while timenow <= VIDEO_LENGTH*1000:
    vid.set(0, timenow)
    success, img = vid.read()
    if success:
        cv2.imwrite("output.jpg", img)
    frame.append(convert_ascii(Image.open("output.jpg")))
    print(frame[-1])
    outputfile.write(frame[-1]+"\n")
    timenow += 100
outputfile.close()
