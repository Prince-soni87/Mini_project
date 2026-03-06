from flask import request, jsonify
from . import api_bp
from app.ai.gemini_service import analyze_pricing

@api_bp.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()
    message = data.get("message")

    try:
        reply = analyze_pricing(message)
    except Exception as e:
        print(e)

        reply = "AI service is temporarily unavailable. But the predicted price is based on demand and cost from the uploaded dataset."

    return jsonify({"reply": reply})