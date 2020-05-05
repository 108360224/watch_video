# -*- coding: utf-8 -*-
"""
Created on Tue May  5 09:41:15 2020

@author: max
"""

from bs4 import BeautifulSoup
import requests
import re

def search(word):
    w=re.sub(r' ','%20',word)
    html = requests.get('http://www.99kubo.tv/index.php?s=home-vod-innersearch&q='+w).text
    soup = BeautifulSoup(html, 'lxml')
    ires=soup.select_one('#ires')
    
    href_list=()
    img_list=()
    text_list=()
    for li in ires.select('li'):
        a=li.select('a')
        href=a[0]['href']
        img=a[0].find('img')['src']
        a2=li.select_one('h3').find('a').contents
        text=''
        for t in a2:
            if isinstance(t, str):
                text+=t
            else:
                text+=t.find('font').string
        
        text=re.sub(r'-.+','',text)
        href_list+=(href,)
        img_list+=(img,)
        text_list+=(text,)
    return (href_list,text_list,img_list)

if __name__=="__main__":
    s=search('好 好')
    print(s[0])
    print(s[1])