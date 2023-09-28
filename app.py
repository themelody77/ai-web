from flask import request, Flask, render_template
from text_summary import summarizer

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ansBot")
def predictionbot():
    return render_template("rewrite.html",summary = "Rewritten Text")

@app.route("/getSummary",methods=["GET","POST"])
def return_summary():
    summary_length = request.form['size']
    rawtxt = request.form['rawtext']
    summary = summarizer(rawtxt,summary_length)
    print(summary)
    return render_template("rewrite.html",summary=summary)