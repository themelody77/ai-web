from flask import request, Flask, render_template
from text_summary import summarizer
from abstract_summary import getAbstractSummary
import os
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",bid="563386da-64a0-49ef-84f1-75226b98180b")

@app.route("/ansBot")
def predictionbot():
    return render_template("rewrite.html",summary = "Rewritten Text",bid="563386da-64a0-49ef-84f1-75226b98180b")

@app.route("/satBot")
def satBot():
    return render_template("chatbot.html",bid="563386da-64a0-49ef-84f1-75226b98180b")

@app.route("/getSummary",methods=["GET","POST"])
def return_summary():
    summary_length = request.form['size']
    rawtxt = request.form['rawtext']
    action = request.form['sumtype']
    if action == "nlp":
        summary = summarizer(rawtxt,summary_length)
        print(summary)
        return render_template("rewrite.html",summary=summary)
    elif action == "abstract":
        summary = getAbstractSummary(rawtxt,summary_length)
        print(summary)
        return render_template("rewrite.html",summary=summary)