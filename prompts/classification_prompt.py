def get_classification_prompt(customer_reply: str) -> str:

    return f"""
You are a CRM assistant.

Classify the following customer reply.

Return ONLY JSON.

{{
    "category":"",
    "sentiment":"",
    "notes":""
}}

Rules:

- category must be one of:
    Interested
    Not Interested
    Request More Info
    No Response

- sentiment must be one of:
    Positive
    Neutral
    Negative

- notes should be a one-line summary of what the customer wants.

Reply:

{customer_reply}
"""