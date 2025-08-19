
from flask import render_template,Flask
from api.auth.register import register
from api.auth.login import login
from api.sports import get_sports
from api.playground import get_playgrounds
from api.user import get_user_info,update_user_password,delete_user_account
from api.booking import booking,create_book,cancel_book

app = Flask("sportify")
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

def html_page(page):
   return render_template("pages/"+page + ".html")


# Routes 
@app.route("/")
def home_page():
    return  html_page("index")

@app.route("/sports")
def sport_page ():
    return html_page("sports")

@app.route("/results")
def result_page ():
    return html_page("results")

@app.route("/booking")
def booking_page():
   content= booking()
   page = html_page("booking")
   new_page= page.replace("$$booking$$",content)
   return new_page

@app.route("/about")
def about_page():
   return html_page("about")

@app.route("/login")
def login_page():
   return html_page("auth/login")

@app.route ("/register")
def register_page():
   return html_page("auth/register")


@app.route ("/profile/info")
def user_page():
   return html_page("profile/user-info")

@app.route ("/profile/update")
def update_page():
   return html_page("profile/update")

@app.route ("/profile/delete")
def delete_page():
   return html_page("profile/delete")




# APi requests
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

@app.route("/api/booking", methods=["POST"])
def booking_court (): 
    return create_book()

@app.route("/api/booking", methods=["DELETE"])
def cancel_booking (): 
    return cancel_book()

@app.route("/api/user-info/<int:id>", methods=["GET"])
def user_Info (id): 
    return get_user_info(id)

@app.route("/api/password/update", methods=["PATCH"])
def update_password (): 
    return update_user_password()

@app.route("/api/delete-user/<int:id>", methods=["DELETE"])
def delete_user (id): 
    return delete_user_account(id)

if __name__ == "__main__":   
  app.run(debug=True)
