# render_template is a tool that builds HTML pages
from flask import Flask, render_template
import json

# initializing application
app=Flask(__name__)

# when user visits homepage, run the func immediately below this
@app.route("/")
def home():
    # opening file in "r"(read-only) and saving the content in a variable "analysis"
    with open("data/analysis.json","r") as f:
        analysis=json.load(f)
    '''looks for index.html in a folder named "templates"
     and makes it available in html under the same name''' 
    return render_template("index.html",analysis=analysis)

if __name__=="__main__":
    app.run(debug=True)