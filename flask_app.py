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
    return render_template('home.html')
    
@app.route('/search' , methods=['GET', 'POST'])
def search():
    input_topic=request.form['topic']
    return render_template('home.html', quotes_result= quotes_list(input_topic,2))

if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    
