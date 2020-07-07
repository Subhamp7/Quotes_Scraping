# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 15:28:54 2020

@author: subham
"""
from requests import get
from bs4 import BeautifulSoup

def quotes_list(topic):
    quote_list=[]
    owner_list =[]
    url_topic="https://www.brainyquote.com/search_results?q="+str(topic)
    soup=BeautifulSoup((get(url_topic)).text, 'html.parser')
    quotes=soup.find('div', id="quotesList")
    try:
        for index in quotes:
            try:
                quote_list.append(index.div.div.div.a.text)
                try:
                    owner_list.append(index.div.div.div.div.a.text)
                except:
                    owner_list.append(None)
            except:
                pass
    except:
        quote_list=[]
        owner_list=[]
    dict={"Quotes" : quote_list, "Aurthor" : owner_list}
    return dict
