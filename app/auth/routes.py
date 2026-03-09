from flask import render_template,request,redirect,url_for,flash
from . import auth_bp
from ..extensions import db,bcrypt
from ..models import User
from flask_login import login_user,logout_user
from sqlalchemy.exc import IntegrityError

@auth_bp.route("/login",methods=["GET","POST"])
def login():

    if request.method=="POST":

        email=request.form["email"]
        password=request.form["password"]

        user=User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password,password):

            login_user(user)
            return redirect("/dashboard")
        else:
            flash("Invalid email or password. Please try again.", "error")
            return redirect("/auth/login")

    return render_template("login.html")


@auth_bp.route("/register",methods=["GET","POST"])
def register():

    if request.method=="POST":

        username=request.form["username"]
        email=request.form["email"]
        password=request.form["password"]

        # Check if email already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email already registered! Please login with a different account.", "error")
            return redirect("/auth/register")

        hashed=bcrypt.generate_password_hash(password).decode("utf-8")

        user=User(username=username,email=email,password=hashed)

        db.session.add(user)
        db.session.commit()

        flash("Registration successful! Please login.", "success")
        return redirect("/auth/login")

    return render_template("register.html")


@auth_bp.route("/logout")
def logout():

    logout_user()
    return redirect("/")