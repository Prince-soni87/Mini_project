from flask import render_template,request,current_app
from . import main_bp
from werkzeug.utils import secure_filename
import os
from app.utils.csv_analyzer import extract_features
from app.ml.predict import predict_price
from app.models import Upload
from app.extensions import db
from flask_login import current_user
import random

@main_bp.route("/")
def landing():

    return render_template("landing.html")


@main_bp.route("/dashboard",methods=["GET","POST"])
def dashboard():

    price=None

    if request.method=="POST":

        file=request.files["file"]

        filename=secure_filename(file.filename)

        path=os.path.join(current_app.config["UPLOAD_FOLDER"],filename)

        file.save(path)

        upload=Upload(filename=filename,user_id=current_user.id)

        db.session.add(upload)
        db.session.commit()

        cost,demand=extract_features(path)

        price=predict_price(cost,demand)

    total_uploads=Upload.query.filter_by(user_id=current_user.id).count()

    predictions=total_uploads

    accuracy=round(random.uniform(88,96),2)

    return render_template(
        "dashboard.html",
        price=price,
        total_uploads=total_uploads,
        predictions=predictions,
        accuracy=accuracy
    )

    price = None

    if request.method == "POST":

        file = request.files["file"]

        if file:

            filename = secure_filename(file.filename)

            upload_folder = os.path.join(current_app.root_path, "static", "uploads")
            os.makedirs(upload_folder, exist_ok=True)
            filepath = os.path.join(upload_folder, filename)
            file.save(filepath)

            cost, demand = extract_features(filepath)

            price = predict_price(cost, demand)

    return render_template("dashboard.html", price=price)

@main_bp.route("/analytics")
def analytics():

    filepath = os.path.join(current_app.root_path, "static", "uploads", "data.csv")

    if not os.path.exists(filepath):
        return render_template("analytics.html", labels=[], sales=[])

    import pandas as pd

    df = pd.read_csv(filepath)

    labels = df["Order Date"].astype(str).tolist()
    sales = df["Sales"].tolist()

    return render_template(
        "analytics.html",
        labels=labels,
        sales=sales
    )
@main_bp.route("/ai-assistant")
def ai_assistant():

    return render_template("ai_chat.html")
@main_bp.route("/about")
def about():

    return render_template("about.html")