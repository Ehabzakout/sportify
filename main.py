
from flask import render_template,Flask
from api.auth.register import register
from api.auth.login import login
from api.sports import get_sports
from api.playground import get_playgrounds


app = Flask("sportify")
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

def html_page(page):
   return render_template("pages/"+page + ".html")


@app.route("/")
def home_page():
    return  html_page("index")

@app.route("/sports")
def sport_page ():
    return html_page("sports")

@app.route("/results")
def result_page ():
    return html_page("results")

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
   
@app.route("/api/sports", methods=["GET"])
def sports (): 
    return get_sports()


@app.route("/api/playgrounds", methods=["GET"])
def playgrounds (): 
    return get_playgrounds()

if __name__ == "__main__":   
  app.run(debug=True)
