# Import dependencies
from flask import Flask, render_template

# Create instance of Flask App
app = Flask(__name__)

# Define 1st Route
@app.route("/")
def home():
    return render_template("index.html")
# Connect
# def home():
#     return("Home Page")


# Define 2nd Route
@app.route("/about")
def about():
    return("Abut me")

# Define 3rd Route
# @app.route("/blog")
# def blog():
#     return render_template("index.html")


# Running app server
if(__name__ == '__main__'):
    app.run(debug=True)

