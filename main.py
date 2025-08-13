
from flask import render_template,Flask,request,jsonify
from api.auth.register import register
from api.auth.login import login

import json

app = Flask("sportify")
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

def html_page(page):
   return render_template("pages/"+page + ".html")


@app.route("/")
def home_page():
    return  html_page("index")
    
@app.route("/about")
def about_page():
   return html_page("about")

@app.route("/login")
def login_page():
   return html_page("auth/login")

@app.route ("/register")
def register_page():
   return html_page("auth/register")


@app.route("/api/auth/register", methods=["POST"])
def add_user():
    return register()
   
@app.route("/api/auth/login", methods=["POST"])
def login_user():
    return login()
   

if __name__ == "__main__":   
  app.run(debug=True)
