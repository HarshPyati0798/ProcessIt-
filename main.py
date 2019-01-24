import numpy as np
import cv2
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk

root = Tk()
root.title('Process It')

def getImage():
    filename = filedialog.askopenfilename(
            parent = root,
            title = 'Choose image for processing',
    )
    return filename
    
def displayImage():
    file = getImage()
    if file is not (None or ''):
        image = Image.open(file)
        image_np = np.array(image)
        image = cv2.cvtColor(image_np,cv2.COLOR_BGR2RGB)
        makeWindow(image)
    
        
def makeWindow(image):
    global img
    img = cv2.resize(image,(600,500))
    while True:
        cv2.imshow('Image',img)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cv2.destroyAllWindows()
    button2.lift()

def greyScale():
    image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image,(600,500))
    while True:
        cv2.imshow('Image',image)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cv2.destroyAllWindows()
    
def blur():
    image = cv2.blur(img,(10,10))
    image = cv2.resize(image,(600,500))
    while True:
        cv2.imshow('Image',image)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cv2.destroyAllWindows()

def remNoise():
    kernel = np.ones(shape = (5,5))
    image = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
    image = cv2.resize(image,(600,500))
    while True:
        cv2.imshow('Image',image)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cv2.destroyAllWindows()
    
def threshHold():
    image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,image = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
    image = cv2.resize(image,(600,500))
    while True:
        cv2.imshow('Image',image)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cv2.destroyAllWindows()
    
def blend():
    img1 = img
    img2 = getImage()
    if img2 is not (None or ''):
        img2 = Image.open(img2)
        img2 = np.array(img2)
        img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
    img1 = cv2.resize(img1,(1200,1200))
    img2 = cv2.resize(img2,(1200,1200))
    blended = cv2.addWeighted(
            src1 = img1,
            alpha = 0.5,
            src2 = img2,
            beta = 0.5,
            gamma = 0
    )
    blended = cv2.resize(blended,(600,500))
    while True:
        cv2.imshow('Image',blended)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cv2.destroyAllWindows()
    
    
    
        
button1 = Button(text = 'Upload an Image',command = displayImage,width = 30,fg = '#31f40e',bg ='white',font=10)
button1.pack(pady = 5)

label1 = Label(text = 'List of Options:(Make sure you have uploaded the image)',font =6,bd = 4,fg = '#31f40e',bg ='white')
label1.pack(pady = 5)

button2 = Button(text ='Black N White',font = 5,command = greyScale,fg = '#31f40e',bg ='white')
button2.pack(pady = 5)

button3 = Button(text ='Blur It',font = 5,command = blur,fg = '#31f40e',bg ='white')
button3.pack(pady = 5)

button4 = Button(text ='Remove Noise',font = 5,command = remNoise,fg = '#31f40e',bg ='white')
button4.pack(pady =5)

button5 = Button(text = 'Thresholding',font = 5,command = threshHold,fg = '#31f40e',bg ='white')
button5.pack(pady = 5)

button6 = Button(text = 'Blend with another image',font = 5,command = blend,fg = '#31f40e',bg ='white')
button6.pack(pady = 5)



root.configure(background = '#31f40e')
root.mainloop()