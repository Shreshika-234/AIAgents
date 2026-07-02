from pathlib import Path
from typing import List

import pandas as pd

from models.lead import Lead
from utils.logger import logger


class ExcelService:
    def __init__(self,file_path:str):
        self.file_path = Path(file_path)
        self.df = pd.read_excel(self.file_path)
        text_columns = [
            "Industry",
            "Buyer Persona",
            "Response Status",
            "Notes",
            "AI Suggested Outreach Message",
            "Email Verified (Y/N)"
        ]

        self.df[text_columns] = (
            self.df[text_columns]
            .astype("object")
        )

        self.df[text_columns] = (
            self.df[text_columns]
            .fillna("")
        )

    def load_leads(self)->List[Lead]:
        leads = []

        for _,row in self.df.iterrows():
            email_verified = row["Email Verified (Y/N)"]
            priority_score = row["Lead Priority (AI Score)"]

            # Handle NaN values
            if pd.isna(email_verified) or email_verified == "":
                email_verified = None
            else:
                email_verified = str(email_verified).upper() == "Y"

            if pd.isna(priority_score):
                priority_score = None
            else:
                priority_score = int(priority_score)
            lead = Lead(

                lead_name=row["Lead Name"],
                email=row["Email"],
                contact_number=str(row["Contact Number"]),
                company=row["Company"],
                industry=row["Industry"],
                email_verified=email_verified,
                priority_score=priority_score,
                buyer_persona=row["Buyer Persona"],
                response_status=row["Response Status"],
                notes=row["Notes"],
                outreach_message=row["AI Suggested Outreach Message"],
                status=row["Status"]
            )

            leads.append(lead)
            
        logger.info(f"{len(leads)} leads loaded.")

        return leads

    def get_pending_leads(self)->List[Lead]:
        leads = self.load_leads()
        return [lead for lead in leads if lead.status.lower() == "pending"]
    
    # def update_lead(self,email:str,lead:Lead):
    #     idx = self.df[self.df["Email"] == email].index
    #     if len(idx) == 0:
    #         return 
    #     i = idx[0]

    #     self.df.loc[i, "Industry"] = lead.industry
    #     self.df.loc[i, "Buyer Persona"] = lead.buyer_persona
    #     self.df.loc[i, "Lead Priority (AI Score)"] = lead.priority_score
    #     self.df.loc[i, "Email Verified (Y/N)"] = lead.email_verified

    def update_lead(self, email: str, lead: Lead):

        idx = self.df[self.df["Email"] == email].index

        if len(idx) == 0:
            return

        i = idx[0]

        self.df.loc[i, "Industry"] = lead.industry

        self.df.loc[i, "Buyer Persona"] = (
            lead.buyer_persona
            if isinstance(lead.buyer_persona, str)
            else str(lead.buyer_persona)
        )

        self.df.loc[i, "Lead Priority (AI Score)"] = lead.priority_score

        self.df.loc[i, "Email Verified (Y/N)"] = (
            "Y" if lead.email_verified else "N"
        )


    def update_outreach(self,email:str,message:str):
        idx = self.df[self.df["Email"] == email].index
        if len(idx) == 0:
            return 
        self.df.loc[idx[0],"AI Suggested Outreach Message"] = message

    def update_response(self,email:str,lead:Lead):
        idx = self.df[self.df["Email"] == email].index
        if len(idx) == 0:
            return 
        self.df.loc[idx[0],"Response Status"] = lead.response_status
        self.df.loc[idx[0],"Notes"] = lead.notes

    def mark_processed(self,email:str):
        idx = self.df[self.df["Email"] == email].index
        if len(idx) == 0:
            return 
        self.df.loc[idx[0],"Status"] = "Processed"

    def save(self):
        self.df.to_excel(self.file_path,index=False)
        logger.info("Excel updated succeddfully.")