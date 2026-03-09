import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GENAI_API_KEY"))

def analyze_pricing(data):

    prompt = f"""
You are an expert revenue optimizer.

Explain the reason behind the predicted price and suggest improvements 
to increase profit margin by 15%.

Analyze this dataset and suggest pricing improvements
to increase profit margin by 15%.

User question:
{data}
"""

    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(prompt)

    return response.text