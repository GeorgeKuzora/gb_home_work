import logging

from flask import (
    Flask,
    Response,
    abort,
    make_response,
    redirect,
    render_template,
    request,
    url_for,
)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(name=__name__)

app = Flask(__name__)


@app.route("/greet/", methods=["GET", "POST"])
def greet():
    if request.method == "POST":
        username = request.cookies.get("username")
        email = request.cookies.get("email")
        logger.info(f"logout {username}")
        response = make_response(redirect(url_for("submit"), code=301))
        response.delete_cookie("username", username)
        response.delete_cookie("email", email)
        return response

    username = request.cookies.get("username", "")
    email = request.cookies.get("email", "")
    if not username:
        abort(404)
    context = {
        "username": username,
        "email": email,
    }
    return render_template("greet.html", **context)


@app.route("/submit/", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        username = request.form.get("username", "")
        email = request.form.get("email", "")
        response = make_response(redirect(url_for("greet"), 301))
        response.set_cookie("username", username)
        response.set_cookie("email", email)

        return response
    return render_template("form.html")


@app.errorhandler(404)
def page_not_found(e):
    logger.warning(e)
    context = {"title": "Страница не найдена", "url": request.base_url}
    return render_template("404.html", **context), 404


if __name__ == "__main__":
    app.run()
