

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def analyze_pricing(message, cost=None, demand=None, price=None):

    try:
        # ✅ Correct condition
        if cost is not None and demand is not None and price is not None:

            prompt = f"""
You are an expert pricing strategist.

Given:
Cost = {cost}
Demand = {demand}
Predicted Price = ₹{price}

Task:
1. Explain in EXACTLY 2 lines why this price is optimal.
2. Give 1 practical improvement suggestion.
3. Answer must be specific to the data (NOT generic).

Keep answer short and clear.
"""

        else:
            prompt = f"""
User asked: {message}

Respond briefly and ask the user to provide cost and demand for better analysis.
"""

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5
        )

        return response.choices[0].message.content

    except Exception as e:
        print("AI ERROR:", str(e))
        return f"AI Error: {str(e)}"