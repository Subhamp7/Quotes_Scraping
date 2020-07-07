# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 15:28:54 2020

@author: subham
"""
try:
    from requests import get
    from bs4 import BeautifulSoup
except Exception as e:
    print("Unable to import module",e)
    
def quotes_list(topic):
    quote_list=[]
    owner_list =[]

    url_topic="https://www.brainyquote.com/search_results?q="+str(topic)
    soup=BeautifulSoup((get(url_topic)).text, 'html.parser')
    quotes=soup.find('div', id="quotesList")
    
    for index in quotes:
        try:
            quote_list.append(index.div.div.div.a.text)
            try:
                owner_list.append(index.div.div.div.div.a.text)
            except:
                owner_list.append(None)
        except:
            pass
    dict={"Quotes" : quote_list, "Aurthor" : owner_list}
    
    return dict


