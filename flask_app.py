from flask import Flask, render_template, request
from web_map import create_map
from urllib.error import HTTPError

app = Flask(__name__)


@app.route("/")
def start(name=None):
    """
    (None -> html)
    This function calls page index.html
    returns: index.html page
    """

    return render_template("index.html", name=name)


@app.route("/application", methods=["POST"])
def application():
    """
    () -> (html)
    This function uses html queries type of "GET" and
    builds a web map
    returns: html map with markers of user`s friends
    """
    user = str(request.form.get("name"))
    if len(user.split()) > 1:
        return render_template("error.html")
    else:
        create_map(user)
        return render_template("map.html")


if __name__ == "__main__":
    app.run(debug=True)
