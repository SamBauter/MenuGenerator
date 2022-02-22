from flask import Flask, render_template, \
    request, redirect, url_for
from menu_model import db, save_db
from random import sample

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday']

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", recipes=db)


@app.route('/add_recipe', methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {"title": request.form['r_title'],
                  "url": request.form['r_url']}
        db.append(recipe)
        save_db()
        return redirect(url_for("index"))
    else:
        return render_template("add_recipe.html")


@app.route('/generate_menu')
def generate_menu():
    indexes = sample(range(len(db)), 7)
    recipes = [db[i] for i in indexes]
    return render_template("generate_menu.html", days_recipes=zip(days, recipes))
