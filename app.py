from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

from config.config import Config
from models.query import get_recipes_without_ingredients

app = Flask(__name__, template_folder="app/templates")
app.config.from_object(Config)
# app.config["MYSQL_HOST"] = "localhost"
# app.config["MYSQL_USER"] = "root"
# app.config["MYSQL_PASSWORD"] = "password"
# app.config["MYSQL_DB"] = "recipiesDB"
#
db = SQLAlchemy(app)


def temp():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM your_table_name")
    data = cursor.fetchall()
    cursor.close()
    return str(data)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/search", methods=["POST"])
def search():
    print("search hit")
    # Get lists of included and excluded ingredients
    include_ingredients = request.form.getlist("include-ingredient")
    exclude_ingredients = request.form.getlist("exclude-ingredient")
    recipes = [
        {"title": "Recipe 1", "link": "/recipe1"},
        {"title": "Recipe 2", "link": "/recipe2"},
        {"title": "Recipe 3", "link": "/recipe3"},
    ]
    print(get_recipes_without_ingredients(exclude_ingredients))
    # For demonstration purposes, print the selected ingredients to console
    print("Included Ingredients:", include_ingredients)
    print("Excluded Ingredients:", exclude_ingredients)

    # Here you would typically query your database based on the selected ingredients
    # and return the results to the user.
    # For this example, we'll just return a simple text response.
    print("Recipes searched! Check server logs for selected ingredients.")
    return render_template("search_results.html", recipes=recipes)


if __name__ == "__main__":
    app.run(debug=True)
preferences: list = ["dairy", "chicken", "beef", "pork", "other_meat", "eggs"]
