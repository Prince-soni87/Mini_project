import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
api_key = os.getenv("GENAI_API_KEY")

if not api_key or api_key == "your_api_key_here":
    raise ValueError("GENAI_API_KEY not configured. Please set it in .env file. Get your key from: https://makersuite.google.com/app/apikey")

genai.configure(api_key=api_key)

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

    # Models to try in order
    models_to_try = [
        "gemini-2.5-flash",
        "gemini-1.5-pro",
        "gemini-1.5-flash",
        "gemini-pro"
    ]
    
    last_error = None
    for model_name in models_to_try:
        try:
            print(f"Trying model: {model_name}")
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)
            print(f"Success with model: {model_name}")
            return response.text
        except Exception as e:
            last_error = e
            print(f"Model {model_name} failed: {str(e)}")
            continue
    
    # If all models fail, raise the last error
    if last_error:
        raise last_error
    else:
        raise Exception("No models available")