from PIL import Image

ASCII_CHARS = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'.⠀'
FRAME_SIZE = (36, 11) # (width, height)
IMAGE_FILEPATH = "FILEPATH"

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

f = open("output.txt", "w", encoding="utf-8")
f.write(convert_ascii(Image.open(IMAGE_FILEPATH)))
f.close()
