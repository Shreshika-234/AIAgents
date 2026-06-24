from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def classify_response(email_reply):

    prompt = f"""
        You are a sales response classifier.

        Classify the response into exactly one category:

        1. Interested
        2. Not Interested
        3. Request More Info
        4. No Response

        Return ONLY the category name.

        Customer Response:
        {email_reply}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()