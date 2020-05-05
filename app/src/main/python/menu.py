# -*- coding: utf-8 -*-
"""
Created on Sat May  2 10:47:12 2020

@author: max
"""

from bs4 import BeautifulSoup
import requests
import re
class Menu():
    def __init__(self,URL='http://www.99kubo.tv'):
        html = requests.get(URL).text
        self.soup = BeautifulSoup(html, 'lxml')
        self.URL=URL
        
    
        re_channel=re.compile('mm\d{0,3}')
        channel_elem = self.soup.select_one('body > div.top > div.menu > div.mainmenu_top')
        menu_href = tuple(a['href'] for a in channel_elem.find_all('a',{'id':re_channel,'target':""}))
        menu_string = tuple(a.string for a in channel_elem.find_all('a',{'id':re_channel,'target':""}))
        
        self.menu_list=(menu_string,menu_href)
        
    
    
    
        sort_elem = self.soup.select_one('body > div.top > div.menu > div.mainmenu_bottom')
        sort_elem_ul=sort_elem.select('ul')
        re_href=re.compile('$(?!html)')
        sort_href=tuple(tuple(re.sub(r'^(?!/)','/',a['href']) for a in ul.find_all('a',{'href':re_href}) if re.match(r'(?!\d){1,4}', a.string))[:-10] for ul in sort_elem_ul)+((),)
        sort_string=tuple(tuple(a.string for a in ul.find_all('a',{'href':re_href}) if re.match(r'(?!\d){1,4}', a.string))[:-10] for ul in sort_elem_ul)+((),)
        
        self.sort_list=(sort_string,sort_href)
        
    
    def get_menu_list(self):
        return self.menu_list
    
    def get_child_list(self):
        return self.sort_list
    
    def get_link(self,menu,sort=''):
        URL=self.URL
        try:
            if sort=='':
                URL+=self.menu_list[1][self.menu_list[0].index(menu)]
            else:
                dex=self.menu_list[0].index(menu)
                URL+=self.sort_list[1][dex][self.sort_list[0][dex].index(sort)]
        except:
            URL+=""
        return URL