from flask import request, Flask, render_template
from text_summary import summarizer

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/getSummary",methods=["POST"])
def return_summary():
    summary_length = request.form['size']
    rawtxt = request.form['rawtext']
    return render_template("summary.html",summary=rawtxt,len=summary_length)