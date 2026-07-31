from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():

    search = request.args.get("search", "").strip()

    df = pd.read_excel("books.xlsx")
    print(df.columns)

    if search:

        mask = (
            df["Book"].astype(str).str.contains(search, case=False, na=False)
            |
            df["Author"].astype(str).str.contains(search, case=False, na=False)
        )

        df = df[mask]

    books = df.to_dict(orient="records")

    return render_template(
        "index.html",
        books=books,
        search=search
    )

if __name__ == "__main__":
    app.run(debug=True)