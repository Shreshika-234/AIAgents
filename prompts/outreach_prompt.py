def get_outreach_prompt(
    lead_name: str,
    company: str,
    industry: str,
    persona: str
) -> str:

    return f"""
You are an experienced B2B Sales Executive.

Lead Name: {lead_name}
Company: {company}
Industry: {industry}
Buyer Persona: {persona}

Your objective is to write a professional cold outreach email that feels natural and personalized.

Return ONLY valid JSON.

{{
    "subject":"",
    "body":""
}}

Rules:

- Write as a sales representative from ABC Solutions.
- Address the recipient as "Dear {lead_name},".
- Mention {company} naturally.
- Mention the {industry} industry naturally.
- If appropriate, briefly acknowledge the recipient's role and responsibilities.
- Briefly explain how ABC Solutions can solve a business problem.
- End with a polite invitation for a 20-minute meeting if nessary.
- Keep the email under 200 words.
- Use a professional and conversational tone.
- Do NOT exaggerate or make false claims.
- End exactly as:

Best regards,

Sales Team
ABC Solutions

- Return ONLY valid JSON.
- Escape every newline using \\n.
"""