# -*- coding: utf-8 -*-
"""
Created on Fri May  1 02:09:11 2020

@author: max
"""

import requests
import re
def get_m3u8(URL):
    response = requests.get('http://www.99kubo.tv'+URL)
    payload=response.text
    try:
        video_link=re.findall(r"http.{1,100}index.m3u8", payload)[0]
        video_link=re.sub(r"\\","",video_link)
        video_link=re.sub(r"/index.m3u8","/1000k/hls",video_link)
        video_link=video_link+"/index.m3u8"
    except:
        video_link='not exit'
    '''
    m3u8_file = requests.get(video_link+"/index.m3u8", allow_redirects=True)
    print(m3u8_file.content[0:200])
    dot=re.compile(b',\n')
    new_m3u8_file=re.sub(dot,bytes(',\n'+video_link,"utf-8"),m3u8_file.content)
    open('index.m3u8', 'wb').write(new_m3u8_file)
    '''
    return video_link

if __name__=="__main__":
    URL='http://www.99kubo.tv/vod-play-id-151292-sid-0-pid-1-ck.html'
    g=get_m3u8(URL)
    print(g)
    