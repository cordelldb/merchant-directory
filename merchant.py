from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    favorite_food = ["Tacos, Tikka Misala, Lasagne, Falafle"]
    return render_template("index.html", favorite_food=favorite_food)

# http://127.0.0.1:5000/user/Cordell
@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name=name)

# CREATE CUSTOM ERROR PAGES
# INVALID URL

@app.errorhandler(404)    
def page_not_found(e):
        return render_template("404.html"), 404
    
@app.errorhandler(500)    
def page_not_found(e):
        return render_template("500.html"), 500
