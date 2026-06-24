from services.llm_service import generate_outreach

def create_outreach_message(lead):

    return generate_outreach(
        lead_name=lead["Lead Name"],
        company=lead["Company"],
        industry=lead["Industry"],
        persona=lead["Buyer Persona"]
    )