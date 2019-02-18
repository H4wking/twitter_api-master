from flask import Flask, render_template, request
from web_map import create_map


app = Flask(__name__)


@app.route("/")
def start(name=None):
    """
    (None) -> html
    Render index.html.
    """
    return render_template("index.html", name=name)


@app.route("/application", methods=["POST"])
def map():
    """
    () -> html
    Render web map based on given account.
    """
    user = str(request.form.get("name"))
    if len(user.split()) > 1:
        return render_template("error.html")
    else:
        create_map(user)
        return render_template("map.html")


if __name__ == "__main__":
    app.run(debug=True)
