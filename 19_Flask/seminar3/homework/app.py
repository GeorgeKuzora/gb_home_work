import logging

from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

from .forms import RegisterForm
from .models import User, bcrypt, db

logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SECRET_KEY"] = "my_key"
bcrypt.init_app(app)
db.init_app(app)
csrf = CSRFProtect(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("OK")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if request.method == "POST" and form.validate():
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        password = form.password.data
        user = User(name=name, surname=surname, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        logger.info(f"User {user = } created")
    return render_template("register.html", form=form)


# @app.post("/register")
# def register_post():
#     form = RegisterForm()
#     if form.validate():
#         name = form.name.data
#         surname = form.surname.data
#         email = form.email.data
#         password = form.password.data
#         user = User(name=name, surname=surname, email=email, password=password)
#         db.session.add(user)
#         db.session.commit()
#         logger.info(f"User {user = } created")
#     return render_template("register.html", form=form)
