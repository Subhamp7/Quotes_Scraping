# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 15:28:54 2020

@author: subham
"""
from requests import get
from bs4 import BeautifulSoup
import re

def quotes_list(topic,pages):
    quotes=[]
    try:
        for index in range(1,pages,1):
            url_topic="https://www.goodreads.com/search?page={}&q={}&qid=FpMJ3rkiq0&search_type=quotes&tab=quotes&utf8=%E2%9C%93".format(index,topic)
            soup=BeautifulSoup((get(url_topic)).text, 'html.parser')
            quotes_all=soup.find_all('div', class_="quoteText")
            
            for index_1 in quotes_all:
                data_text=re.sub(r'\s+',' ',index_1.text)
                if(len(data_text)<200):
                    quotes.append(data_text)
        if(len(quotes)==0):
            quotes=["Oops no results"]
    except:
        quotes=["Oops no results"]
    return quotes 
