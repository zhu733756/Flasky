# -*- coding: utf-8 -*-
"""
@author: zh
"""

#the first flask program
# from flask import Flask
#
# app=Flask(__name__)
# @app.route("/")
# def index():
#     return "<h1>hello,world!</h1>"
#
# @app.route("/user/<name>")
# def user(name):
#     return "<h1>hello,%s</h1>"%name
#
# if "__main__"==__name__:
#
#     app.run(debug=True)

# #request and response
# from flask import Flask,request,make_response,redirect,abort
#
# app=Flask(__name__)
#
# @app.route("/")
# def index():
#     return "<h1>hello,world!</h1>"
#
# @app.route("/headers")
# def return_headers():
#     user_agent=request.headers.get("User-Agent")
#     return "<h1>Hello,your user-agent is %s</h1>"%user_agent
#
# @app.route("/mapurl")
# def return_app_mapurl():
#     return "<h1>hello,%s</h1>"%app.url_map
#
# @app.route("/bad_request")
# def return_bad_request():
#     return "<h1>Bad requests</h1>",400
#
# @app.route("/make_response")
# def make_a_response():
#     response=make_response("<h1>make a cookie!</ha>")
#     response.set_cookie("zhu733756","hello")
#     return response
#
# @app.route("/redirect")
# def return_redirect():
#     return redirect("https://www.baidu.com")
#
# @app.route("/abort")
# def return_abort():
#     return abort(404)
#
# if "__main__"==__name__:
#
#     app.run(debug=True)

#shell script modec
from flask_script import Manager
from flask import Flask
app=Flask(__name__)

@app.route("/")
def index():
    return "<h1>hello,world!</h1>"

@app.route("/user/<name>")
def user(name):
    return "<h1>hello,%s</h1>"%name

if __name__=="__main__":
    app.run()
    manager = Manager(app)
    manager.run()