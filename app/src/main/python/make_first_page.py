# -*- coding: utf-8 -*-
"""
Created on Sat May  2 11:26:18 2020

@author: max
"""
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import requests
def make_first_page(src,text):
    def cv2ImgAddText(img, text, left, top, textColor=(0, 0, 0), textSize=10):
        if (isinstance(img, np.ndarray)):  #判断是否OpenCV图片类型
            img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(img)
        fontText = ImageFont.truetype("font/simsun.ttc", textSize, encoding="utf-8")
        draw.text((left, top), text, textColor, font=fontText)
        return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
    
    
    try:
        response = requests.get(src,timeout=3)
        nparr = np.frombuffer(response.content, np.uint8)
        im = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    except:
        im=np.zeros((90,120,3), np.uint8)
    im=cv2.resize(im,(90,120))
    im=cv2.copyMakeBorder(src=im,left=0,right=0,top=0,bottom=25,borderType=cv2.BORDER_CONSTANT,value=[255, 255, 255])
    tex=''
    if len(text)>12:
        if len(text)>24:
            tex=text[:12]+'\n'+text[12:24]+'\n'+text[24:]
    else:
        tex=text
    
    im=cv2ImgAddText(im,tex,2,121)
    #cv2.imwrite("CV.jpg", im)
    
    return im