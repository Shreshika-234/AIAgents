from models.lead import Lead

from services.groq_service import GroqService
from services.email_verification_service import VerificationService

from utils.logger import logger

class VerificationAgent:

    def __init__(self):
        self.groq = GroqService()
        self.verifier = VerificationService()


    def execute(self,lead:Lead)->Lead:
        logger.info(f"Verification Agent -> {lead.company}")
        verification = self.verifier.verify_email(lead.email)
        lead.email_verified = verification["verified"]
        enrichment = self.groq.enrinch_company(lead.company)

        lead.industry = enrichment["industry"]
        lead.buyer_persona = enrichment["buyer_persona"]
        lead.priority_score = enrichment["priority_score"]
        return lead