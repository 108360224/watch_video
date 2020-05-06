# -*- coding: utf-8 -*-
"""
Created on Sat May  2 10:45:29 2020

@author: max
"""
from bs4 import BeautifulSoup
import requests
import re
from make_first_page import make_first_page
import numpy as np
import cv2
class Film():
    def __init__(self,URL):
        html = requests.get('http://www.99kubo.tv'+URL).text
        soup = BeautifulSoup(html, 'lxml')
        a=soup.select_one('body > div.main > div.list > div.listlf > dl > span > a:nth-child(3)')
        self.URL='http://www.99kubo.tv/'+a['href']
        html = requests.get(self.URL).text
        self.soup = BeautifulSoup(html, 'lxml')
        url_list=()
        img_list=()
        title_list=()
    
        
        ul=self.soup.select_one('body > div.main > div.list > div.listlf > ul')
        
        for li in ul.select('li'):
            a=li.select('a')[0]
            url_list+=(a['href'],)
            img=a.find_all('img')[0]
            im=img['data-original']
            img_list+=(im,)
            title_list+=(img['alt'],)
        self.film_list=(url_list,title_list,img_list)
        
    def get_film_list(self):
        return self.film_list
    def sort_by(self,sort):
        url_list=()
        img_list=()
        title_list=()
        tag=self.soup.select_one('body > div.main > div.list > div.listlf > div')
        a=tag.find_all('a')[-1]
        self.URL=re.sub(r'order.+%20desc','order-'+sort+'%20desc',self.URL)
        html = requests.get(self.URL).text
        self.soup = BeautifulSoup(html, 'lxml')
        
        ul=self.soup.select_one('body > div.main > div.list > div.listlf > ul')
        
        for li in ul.select('li'):
            a=li.select('a')[0]
            url_list+=(a['href'],)
            img=a.find_all('img')[0]


            im=img['data-original']
            img_list+=(im,)
            title_list+=(img['alt'],)
        self.film_list=(url_list,title_list,img_list)
    def goto_area(self,area):
        url_list=()
        img_list=()
        title_list=()
        tag=self.soup.select_one('body > div.main > div.list > div.listlf > div')
        a=tag.find_all('a')[-1]
        self.URL=re.sub(r'area.+tag','area-'+area+'-tag',self.URL)
        html = requests.get(self.URL).text
        self.soup = BeautifulSoup(html, 'lxml')
        
        ul=self.soup.select_one('body > div.main > div.list > div.listlf > ul')
        
        for li in ul.select('li'):
            a=li.select('a')[0]
            url_list+=(a['href'],)
            img=a.find_all('img')[0]


            im=img['data-original']
            img_list+=(im,)
            title_list+=(img['alt'],)
        self.film_list=(url_list,title_list,img_list)
    def load_new_film(self):
        url_list=()
        img_list=()
        title_list=()
        tag=self.soup.select_one('body > div.main > div.list > div.listlf > div')
        a=tag.find_all('a')[-1]
        html = requests.get('http://www.99kubo.tv/'+a['href']).text
        self.soup = BeautifulSoup(html, 'lxml')
        
        ul=self.soup.select_one('body > div.main > div.list > div.listlf > ul')
        
        for li in ul.select('li'):
            a=li.select('a')[0]
            url_list+=(a['href'],)
            img=a.find_all('img')[0]


            im=img['data-original']
            img_list+=(im,)
            title_list+=(img['alt'],)
        self.film_list=(url_list,title_list,img_list)
        
