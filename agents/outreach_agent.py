from models.lead import Lead

from services.groq_service import GroqService
from services.send_email_service import EmailService

from utils.logger import logger


class OutreachAgent:

    def __init__(self):

        self.groq = GroqService()
        self.email_service = EmailService()


    def generate_message(self,lead: Lead) -> Lead:

        logger.info(f"Generating outreach for {lead.lead_name}")

        message = self.groq.generate_outreach(
            lead_name=lead.lead_name,
            company=lead.company,
            industry=lead.industry,
            persona=lead.buyer_persona
            )
        lead.email_subject = message["subject"]
        lead.outreach_message = message["body"]

        return lead


    def send_email(self,lead: Lead) -> bool:

        logger.info(f"Sending email to {lead.email}")

        return self.email_service.send_email(

            recipient=lead.email,
            subject=lead.email_subject,
            body=lead.outreach_message

        )
    
    def classify_response(self,lead: Lead,customer_reply: str) -> Lead:

        logger.info(f"Classifying response from {lead.email}")
        result = self.groq.classify_response(customer_reply)
        lead.response_status = result.get("category","No Response")
        
        # Save sentiment in Notes
        lead.notes =  result.get("notes","")

        return lead