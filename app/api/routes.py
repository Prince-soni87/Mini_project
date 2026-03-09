from flask import request, jsonify
from . import api_bp
from app.ai.gemini_service import analyze_pricing
import traceback

@api_bp.route("/chat", methods=["POST"])
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