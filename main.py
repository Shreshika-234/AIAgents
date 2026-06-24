from services.excel_service import (
    get_pending_leads,
    update_lead,
    update_outreach_message,
    mark_processed

)

from agents.verify import process_lead
from agents.outreach import create_outreach_message

leads = get_pending_leads()

for idx, lead in leads.iterrows():

    print(f"Processing {lead['Lead Name']}")

    result = process_lead(lead)
    update_lead(idx, result)
    leads_updated = get_pending_leads()
    current_lead = leads_updated.loc[idx]
    message = create_outreach_message(current_lead)
    update_outreach_message(idx,message)

    mark_processed(idx)

    print(f"Completed {lead['Lead Name']}")