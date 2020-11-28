from flask import Flask , render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("bootstrap.html")

@app.route("/bootstrap")
def bootstrap():
    return "Hello World"

app.run(debug=True)
