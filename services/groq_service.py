import json 
import re
from typing import Dict

from groq import Groq
from config import config
from utils.logger import logger


from prompts.enrichment_prompt import get_enrichment_prompt
from prompts.outreach_prompt import get_outreach_prompt
from prompts.classification_prompt import get_classification_prompt
from prompts.report_prompt import get_report_prompt

class GroqService:

    def __init__(self):
        self.client = Groq(
            api_key=config.GROQ_API_KEY
        )
        self.model="llama-3.3-70b-versatile"


    # Common LLM Invocation
    def _invoke(self,prompt:str,temperature:float=0) -> str:
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role":"user","content":prompt}
                ],
                temperature = temperature
            )
            return response.choices[0].message.content.strip()
        
        except Exception as e:
            logger.exception(e)
            raise


    # Extract JSON from LLM response
    def _extract_json(self,response:str)->Dict:
        match = re.search(r"\{.*\}",response,re.DOTALL)
        if not match:
            raise ValueError("Groq did not return valid JSON")
        return json.loads(match.group())
    

    # Company Enrichment
    def enrinch_company(self,company:str)->Dict:

        prompt = get_enrichment_prompt(company)
        response = self._invoke(prompt)

        return self._extract_json(response)
    

    # Outreach Email Generation
    def generate_outreach(self,lead_name: str,company: str,industry: str,persona: str)->str:

        prompt = get_outreach_prompt(lead_name,company,industry,persona)
        response = self._invoke(prompt,temperature=0.7)
        result = self._extract_json(response)
        result["body"] = result["body"].replace("\\n", "\n")

        return result
    

    # Customer Reply Classification
    def classify_response(self,customer_reply:str)->Dict:

        prompt = get_classification_prompt(customer_reply)
        response = self._invoke(prompt)

        return self._extract_json(response)
    
    
    # Campaign Report Generation
    def generate_campaign_report(self,summary:str)->str:

        prompt = get_report_prompt(summary)

        return self._invoke(prompt,temperature=0.3)