from flask import request, Flask, render_template
from text_summary import summarizer

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="www.sathvik-ai-web.onrender.com")