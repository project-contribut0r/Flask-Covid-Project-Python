from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField

app = Flask(__name__)

newsSnippets = [  #Collection of news snippets hardcode or fetch as appropriate
  {
    'title': 'filler blahblahblah',  # We fetch these from elsewhere might be hardcoded time dependent
    'timePeriod': 'filler blahblahblah',
    'content': 'filler blahblahblah'
    # Not sure is we can store image source within data structure as variable is so include above
  }
]

@app.route("/")
@app.route("/home")  #Included as this really should default to the homepage
def hello():
  return "<h1>home</h1>"

@app.route("/graph")
def graph():
  return "<h1> Graph to compare Covid and Crime Rates </h1>"

@app.route("/about")
def about():
  return "<h1> Author notes on legal, ethical and political data requirements </h1>"

