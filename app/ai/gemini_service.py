from google import genai
import os
from dotenv import load_dotenv


load_dotenv()
client=genai.Client(api_key=os.getenv("GENAI_API_KEY"))

def analyze_pricing(data):

    prompt = f"""
    You are an expert revenue optimizer.
    explain the reason behind the predicted price and suggest improvements to increase profit margin by 15%.

    Analyze this dataset and suggest pricing improvements
    to increase profit margin by 15%.

    User question:
    {data}
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text