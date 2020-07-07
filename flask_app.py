# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 18:05:45 2020

@author: subham
"""

from flask import Flask, request, render_template
from scrap_quote import quotes_list

app=Flask(__name__)

@app.route('/')
def home():
    input_topic=request.args['topic']
    return quotes_list(input_topic)
    

if __name__ == "__main__":
    app.run()
    
    
