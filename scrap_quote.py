# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 15:28:54 2020

@author: subham
"""
from requests import get
from bs4 import BeautifulSoup
import flask

def quotes_list(topic):
    quote_name=""
    owner_name =""
    dict={}
    url_topic="https://www.brainyquote.com/search_results?q="+str(topic)
    soup=BeautifulSoup((get(url_topic)).text, 'html.parser')
    quotes=soup.find('div', id="quotesList")
    try:
        for index in quotes:
            try:
                quote_name=index.div.div.div.a.text
                try:
                    owner_name=index.div.div.div.div.a.text
                except: 
                    owner_name=None
                dict[quote_name]=owner_name
            except:
                pass
    except:
        dict={}
    return dict

