def get_report_prompt(summary: str) -> str:

    return f"""
You are a Sales Manager preparing a CRM campaign report.

Campaign Statistics

{summary}

Rules:

- Use ONLY the statistics provided.
- Do NOT invent campaign names, objectives, or duration.
- Do NOT assume information that is not provided.
- Write in a professional business tone.
- Highlight both strengths and weaknesses.
- Provide practical recommendations based only on the campaign results.
- Keep the report under 350 words.

Use exactly these sections:

# Campaign Performance Report

## Executive Summary

## Campaign Metrics

## Key Insights

## Recommendations

## Conclusion
"""