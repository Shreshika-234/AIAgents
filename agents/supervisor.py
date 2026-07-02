import os

from agents.verification_agent import VerificationAgent
from agents.outreach_agent import OutreachAgent
from services.excel_service import ExcelService
from workflows.crm_graph import CRMGraph
from agents.report_agent import ReportAgent

from utils.logger import logger


class SupervisorAgent:

    def __init__(self, excel_path: str):

        self.excel = ExcelService(excel_path)
        self.verification_agent = VerificationAgent()
        self.outreach_agent = OutreachAgent()
        self.report_agent = ReportAgent()
        self.graph = CRMGraph(
            verification_agent=self.verification_agent,
            outreach_agent=self.outreach_agent,
            excel_service=self.excel
        )

    def run(self):

        logger.info("Supervisor Started")

        pending_leads = self.excel.get_pending_leads()

        logger.info(f"Found {len(pending_leads)} pending leads.")

        # Process all pending leads using LangGraph workflow
        for lead in pending_leads:
            try:

                logger.info(f"Processing {lead.lead_name}")

                self.graph.run(lead)

            except Exception as e:
                logger.exception(f"Failed processing {lead.email} : {e}")

        # Simulated customer replies (replace with Gmail/Outlook/SendGrid in production)
        demo_customer_replies = {

            "john@stripe.com":
                "This looks interesting. Let's schedule a demo next week.",

            "sarah@microsoft.com":
                "Can you send me more technical documentation?",

            "david@amazon.com":
                "Thanks, but we are not interested at the moment.",

            "emma@openai.com":
                ""
        }

        # Classify customer replies and update CRM
        for lead in pending_leads:

            try:

                customer_reply = demo_customer_replies.get(lead.email,"")

                updated_lead = self.outreach_agent.classify_response(lead,customer_reply)

                self.excel.update_response(
                    updated_lead.email,
                    updated_lead
                )

            except Exception as e:

                logger.exception(
                    f"Failed classifying reply for {lead.email}: {e}"
                )

        self.excel.save()
        
        # Generate AI campaign report
        report = self.report_agent.generate_report(self.excel)

        os.makedirs("reports", exist_ok=True)

        with open("reports/campaign_report.txt", "w") as f:
            f.write(report)

        logger.info(report)
        logger.info("Campaign report saved to reports/campaign_report.txt")
        
        logger.info("Supervisor Finished")