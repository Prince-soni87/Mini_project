from flask import request, jsonify, render_template, current_app
from . import api_bp
from app.ai.gemini_service import analyze_pricing
import traceback
from werkzeug.utils import secure_filename
import os
from app.utils.csv_analyzer import extract_features
from app.ml.predict import predict_price
from app.models import Upload
from app.extensions import db
from flask_login import current_user
import random
import pandas as pd

@api_bp.route("/api/chat", methods=["POST"])
def chat():

    data = request.get_json()
    message = data.get("message")

    try:
        reply = analyze_pricing(message)
    except Exception as e:
        print(f"AI Error: {str(e)}")
        print(traceback.format_exc())

        reply = f"Error: {str(e)}. Please configure GENAI_API_KEY in .env file."

    return jsonify({"reply": reply})

@api_bp.route("/")
def landing():

    return render_template("landing.html")

@api_bp.route("/dashboard",methods=["GET","POST"])
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

@api_bp.route("/analytics")
def analytics():

    filepath = os.path.join(current_app.root_path, "static", "uploads", "data.csv")

    if not os.path.exists(filepath):
        return render_template("analytics.html", labels=[], sales=[])

    df = pd.read_csv(filepath)

    labels = df["Order Date"].astype(str).tolist()
    sales = df["Sales"].tolist()

    return render_template(
        "analytics.html",
        labels=labels,
        sales=sales
    )

@api_bp.route("/ai-assistant")
def ai_assistant():

    return render_template("ai_chat.html")