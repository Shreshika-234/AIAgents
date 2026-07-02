# AIAgents

AIAgents is a lightweight AI-powered lead management and outreach workflow built in Python. It processes pending leads from an Excel file, enriches and verifies contact data, generates outreach messages using Groq, classifies customer replies, updates the spreadsheet, and writes a campaign report.

## Features

- Load leads from `data/leads.xlsx`
- Verify email addresses using `email-validator`
- Enrich company data and buyer persona using a Groq LLM model
- Generate personalized outreach emails
- Simulate sending outreach and classify customer replies
- Save updated lead status back to the Excel workbook
- Generate a summarized campaign report in `reports/campaign_report.txt`

## Project Structure

- `main.py` — entrypoint that starts the `SupervisorAgent`
- `config.py` — loads API keys from environment variables
- `agents/` — workflow agents for verification, outreach, reporting, and supervision
- `services/` — external integrations for Groq, email verification, Excel, and email logging
- `workflows/` — orchestration graph and workflow state definitions
- `models/lead.py` — lead model definition
- `prompts/` — prompt templates for enrichment, outreach, classification, and reporting

## Requirements

- Python 3.11+ recommended
- `pip install -r requirements.txt`

## Environment Variables

Create a `.env` file in the project root with the following values:

```env
GROQ_API_KEY=your_groq_api_key
HUNTER_API_KEY=your_hunter_api_key
SENDGRID_API_KEY=your_sendgrid_api_key
```

> Only `GROQ_API_KEY` is required for the current AI workflow. The other keys are included for future integrations.

## Usage

1. Place your lead workbook at `data/leads.xlsx`.
2. Ensure pending leads are marked with `Status = Pending`.
3. Run the application:

```bash
python3 main.py
```

4. After execution:
   - `data/leads.xlsx` is updated with verification, outreach, and reply status
   - `reports/campaign_report.txt` contains the generated campaign summary

## Notes

- `services/send_email_service.py` currently logs email content instead of sending real email.
- Customer replies are simulated in `agents/supervisor.py` for demo purposes.
- The Groq model used is `llama-3.3-70b-versatile` and can be adjusted in `services/groq_service.py`.

## Extend

- Hook a real email provider into `EmailService`
- Replace simulated replies with live inbox parsing
- Add support for additional Excel columns and CRM integrations
