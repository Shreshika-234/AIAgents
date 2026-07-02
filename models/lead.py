from pydantic import BaseModel
from typing import Optional


class Lead(BaseModel):

    lead_name: str
    email: str
    contact_number: str
    company: str
    industry: Optional[str] = None
    email_verified: Optional[bool] = None
    email_subject: str | None = None
    priority_score: Optional[int] = None
    buyer_persona: Optional[str] = None
    response_status: Optional[str] = None
    notes: Optional[str] = None
    outreach_message: Optional[str] = None
    status: str


