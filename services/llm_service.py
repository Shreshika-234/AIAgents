import os
import json
import re

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def enrich_lead(company):

    prompt = f"""
                You are an expert B2B sales analyst.

                Analyze the company below.

                Company: {company}

                Return ONLY a JSON object.

                Fields:
                - industry
                - buyer_persona
                - priority_score (1-100)

                Example:

                {{
                    "industry":"FinTech",
                    "buyer_persona":"CTO",
                    "priority_score":92
                }}
            """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ],
        temperature=0
    )

    content = response.choices[0].message.content

    print(content)

    match = re.search(
        r"\{.*\}",
        content,
        re.DOTALL
    )

    if not match:
        raise ValueError("No JSON found")

    return json.loads(
        match.group()
    )


def generate_outreach(lead_name,company,industry,persona):

    prompt = f"""
        You are an expert B2B sales representative.

        Lead Name: {lead_name}
        Company: {company}
        Industry: {industry}
        Buyer Persona: {persona}

        Generate a personalized outreach email.

        Keep it professional and concise.
        Add Name at regards as 
        Return only the email text.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content