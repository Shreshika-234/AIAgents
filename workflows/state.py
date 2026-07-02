from typing import TypedDict, Optional

from models.lead import Lead


class CRMState(TypedDict):

    lead: Lead

    report: Optional[str]