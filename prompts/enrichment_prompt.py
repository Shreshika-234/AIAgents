def get_enrichment_prompt(company: str) -> str:

    return f"""
            You are an expert B2B CRM analyst.

            Analyze the company below.

            Company: {company}

            Return ONLY JSON.

            {{
                "industry": "",
                "buyer_persona": "",
                "priority_score": 0
            }}

            Rules:

            - industry must be exactly ONE industry.
            - buyer_persona must be exactly ONE realistic decision-maker for purchasing B2B software or AI solutions.
            - Examples of buyer_persona:
                - Head of Payments
                - VP Engineering
                - Director of Technology
                - Head of AI
                - Chief Product Officer
                - Procurement Manager
                - CIO
                - CTO
            - Do NOT always return CEO or CTO.
            - priority_score must be an integer between 0 and 100.
            - Estimate the score based on the company's overall business value and likelihood of being a high-value B2B customer.
            - Larger, well-known enterprises should generally receive higher scores than smaller or less established companies.
            - Do NOT return objects.
            - Do NOT return arrays.
            - Do NOT return explanations.
            - Return ONLY valid JSON.
"""