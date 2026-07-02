from services.groq_service import GroqService
from services.excel_service import ExcelService

from utils.logger import logger


class ReportAgent:

    def __init__(self):
        self.groq = GroqService()

    def generate_report(self,excel: ExcelService) -> str:

        logger.info("Generating Campaign Report")

        df = excel.df
        total = len(df)
        # verified = (df["Email Verified (Y/N)"] == True).sum()
        verified = (df["Email Verified (Y/N)"] == "Y").sum()
        processed = (df["Status"] == "Processed").sum()
        interested = (df["Response Status"] == "Interested").sum()

        summary = f"""
                Total Leads : {total}
                Verified : {verified}
                Processed : {processed}
                Interested : {interested}

        """

        report = self.groq.generate_campaign_report(summary)

        return report