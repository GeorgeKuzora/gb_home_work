import logging

from flask import Flask, render_template

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(name=__name__)

app = Flask(__name__)

categories_data = {
    "clothes": {
        "title": "Одежда",
        "items": [
            {"title": "Coat", "description": "Nice coat", "price": 10},
            {"title": "Pants", "description": "Nice pants", "price": 15},
            {"title": "Socks", "description": "Nice Socks", "price": 5},
        ],
    },
    "tech": {
        "title": "Техника",
        "items": [
            {"title": "Phone", "description": "Nice phone", "price": 100},
            {"title": "Computer", "description": "Nice computer", "price": 150},
            {"title": "Keyboard", "description": "Nice keyboard", "price": 50},
        ],
    },
}


@app.route("/")
def main():
    return render_template("base.html")


@app.route("/categories/<category>/")
def get_category(category):
    if context := categories_data.get(category):
        return render_template("category.html", **context)


if __name__ == "__main__":
    app.run()
