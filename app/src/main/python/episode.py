# -*- coding: utf-8 -*-
"""
Created on Sat May  2 10:44:48 2020

@author: max
"""

from bs4 import BeautifulSoup
import requests
import re
class Episode():
    def __init__(self,URL):
        self.URL='http://www.99kubo.tv'+URL
        html = requests.get(self.URL).text
        self.soup = BeautifulSoup(html, 'lxml')
    
        
        ul=self.soup.select_one('body > div.main > div.topRow > div > ul > div > div')
        url_list=()
        string_list=()
        for a in ul.find_all('a'):
            url_list+=(a['href'],)
            string_list+=(a.string,)
        self.ep_list=(string_list,url_list)
    def get_ep_list(self):
        return self.ep_list
    def get_ep_link(self,ep):
        return self.ep_list[1][self.ep_list[0].index(ep)]