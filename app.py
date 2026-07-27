from flask import Flask
app = Flask(__name__)
@app.route("/")
@app.route("/")
def home():
    return "Welcome to the Library Management System!"


if __name__ == "__main__":
    app.run(debug=True)