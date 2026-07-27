from flask import Flask, render_template

app = Flask(__name__)
# Disable template caching during development
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/books")
def books():
    return render_template("books.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)