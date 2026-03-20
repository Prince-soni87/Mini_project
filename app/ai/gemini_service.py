from google import genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize client
client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))


def analyze_pricing(data):

    prompt = f"""
You are an expert revenue optimizer.

Explain the reason behind pricing and suggest improvements 
to increase profit margin by 15%.

User input:
{data}
"""

    try:
        response = client.models.generate_content(
            model="gemini-flash-latest",   # ✅ YOUR API SUPPORTED MODEL
            contents=prompt
        )

        return response.text

    except Exception as e:
        print("AI ERROR:", str(e))
        return f"AI Error: {str(e)}"