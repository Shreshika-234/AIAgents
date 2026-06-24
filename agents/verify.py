from services.llm_service import enrich_lead

def verify_email(email):

    if "@" in email and "." in email:
        return "Y"

    return "N"


def process_lead(lead):

    result = enrich_lead(lead["Company"])

    result["email_verified"] = verify_email(lead["Email"])

    return result