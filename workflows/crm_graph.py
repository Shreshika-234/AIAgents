from langgraph.graph import StateGraph, END

from workflows.state import CRMState


class CRMGraph:

    def __init__(self,verification_agent,outreach_agent,excel_service):

        self.verification_agent = verification_agent
        self.outreach_agent = outreach_agent
        self.excel_service = excel_service

        workflow = StateGraph(CRMState)

        # Verification Node
        workflow.add_node(
            "verification",
            self.verification_node
        )

        # Outreach Node
        workflow.add_node(
            "outreach",
            self.outreach_node
        )

        
        # Graph Flow
        workflow.set_entry_point("verification")

        workflow.add_edge(
            "verification",
            "outreach"
        )

        workflow.add_edge(
            "outreach",
            END
        )

        self.graph = workflow.compile()

    
    # Verification Node
    def verification_node(self, state: CRMState):

        lead = state["lead"]
        lead = self.verification_agent.execute(lead)
        self.excel_service.update_lead(
            email=lead.email,
            lead=lead
        )

        return {
            "lead": lead
        }

    
    # Outreach Node
    def outreach_node(self, state: CRMState):

        lead = state["lead"]
        lead = self.outreach_agent.generate_message(lead)

        self.excel_service.update_outreach(
            email=lead.email,
            message=lead.outreach_message
        )

        self.outreach_agent.send_email(lead)

        self.excel_service.mark_processed(lead.email)

        return {
            "lead": lead
        }

    
    def run(self, lead):

        return self.graph.invoke({
            "lead": lead
        })