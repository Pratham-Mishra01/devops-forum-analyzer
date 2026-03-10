# render_template is a tool that builds HTML pages
from flask import Flask, render_template
import json
import threading
import time
import subprocess

# initializing application
app=Flask(__name__)

def auto_refresh():

    while True:
        subprocess.run(["python", "pipeline.py"])
        time.sleep(60)

# when user visits homepage, run the func immediately below this
@app.route("/")
def home():
    # opening file in "r"(read-only) and saving the content in a variable "analysis"
    with open("data/analysis.json","r") as f:
        analysis=json.load(f)
    '''looks for index.html in a folder named "templates"
     and makes it available in html under the same name''' 
    return render_template("index.html",analysis=analysis)

@app.route("/topics")
def topics():
    with open("data/analysis.json", "r") as f:
        analysis = json.load(f)
    topic_analysis = analysis.get("topic_analysis", {})
    return render_template("topics.html", topic_analysis=topic_analysis)


if __name__=="__main__":
    threading.Thread(target=auto_refresh, daemon=True).start()
    app.run(debug=False)