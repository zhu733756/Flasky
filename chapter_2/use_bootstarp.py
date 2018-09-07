# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name：     
   Description：
-------------------------------------------------
__author__ = 'zhu733756'
"""

from flask_bootstrap import Bootstrap
from flask import render_template,Flask
from datetime import datetime
from flask_moment import Moment

app=Flask(__name__)
moment=Moment(app)
bootstrap=Bootstrap(app)

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/")
# def index():
#     return render_template("index2.html")

@app.route("/")
def index():
    return render_template("index3.html",
                           current_time=datetime.utcnow())

# @app.route("/user/<name>")
# def user(name):
#     return render_template("user_2.html",name=name)

# @app.route("/user/<name>")
# def user(name):
#     return render_template("user_3.html",name=name)

@app.route("/user/<name>")
def user(name):
    return render_template("user_4.html",name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"),500

if __name__=="__main__":
    app.run(debug=True)