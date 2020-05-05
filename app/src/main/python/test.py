# -*- coding: utf-8 -*-
"""
Created on Sat May  2 10:45:29 2020

@author: max
"""
from bs4 import BeautifulSoup
import requests
import re
from urllib.parse import unquote
from make_first_page import make_first_page
class Film():
    def __init__(self,url):

        html = requests.get('http://www.99kubo.tv'+url).text
        soup = BeautifulSoup(html, 'lxml')
        a=soup.select_one('body > div.main > div.list > div.listlf > dl > span > a:nth-child(3)')

        self.URL='http://www.99kubo.tv/'+a['href']

        html = requests.get(self.URL).text

        self.soup = BeautifulSoup(html, 'lxml')
        url_list=()
        img_list=()
        #title_list=()


        ul=self.soup.select_one('body > div.main > div.list > div.listlf > ul')

        for li in ul.select('li'):
            a=li.select('a')[0]
            url_list+=(a['href'],)
            img=a.find_all('img')[0]
            im=make_first_page(img['data-original'],img['alt'])
            img_list+=(im,)
            #title_list+=(img['alt'],)
        self.film_list=(url_list,img_list)

    def get_film_list(self):
        return self.film_list

    def load_new_film(self):
        url_list=()
        img_list=()
        #title_list=()
        tag=self.soup.select_one('body > div.main > div.list > div.listlf > div')
        a=tag.find_all('a')[-1]
        html = requests.get('http://www.99kubo.tv/'+a['href']).text
        self.soup = BeautifulSoup(html, 'lxml')
        ul=self.soup.select_one('body > div.main > div.list > div.listlf > ul')

        for li in ul.select('li'):
            a=li.select('a')[0]
            url_list+=(a['href'],)
            img=a.find_all('img')[0]
            im=make_first_page(img['data-original'],img['alt'])
            img_list+=(im,)
            #title_list+=(img['alt'],)
        self.film_list=(url_list,img_list)
