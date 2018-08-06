# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 21:10:10 2018

@author: SilverDoe
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    db = sqlite3.connect(app.config['DATABASE'])
    f= app.open_resource('schema.sql')
    db.cursor().executescript(f.read())
    print("hello called")
    return "Hello World!"

if __name__ == "__main__":
    app.run()
    
    
    