import pandas as pd

FILE_PATH = "/home/shreshika_/AIAgents/aiagents/leads.xlsx"


def read_leads():

    df = pd.read_excel(FILE_PATH)

    text_cols = [
        "Industry",
        "Buyer Persona",
        "Email Verified (Y/N)",
        "Response Status",
        "Notes",
        "AI Suggested Outreach Message"
    ]

    for col in text_cols:
        df[col] = df[col].astype("object")

    return df


def get_pending_leads():

    df = read_leads()

    return df[df["Status"] == "Pending"]

def update_lead(row_index, result):

    df = read_leads()
    df.loc[row_index, "Industry"] = result["industry"]
    df.loc[row_index, "Buyer Persona"] = result["buyer_persona"]
    df.loc[
        row_index,
        "Lead Priority (AI Score)"
    ] = int(result["priority_score"])
    df.loc[
        row_index,
        "Email Verified (Y/N)"
    ] = result["email_verified"]
    df.to_excel(FILE_PATH, index=False)

def update_response_status(row_index,status):

    df = read_leads()

    df.loc[row_index,"Response Status"] = status

    df.to_excel(
        FILE_PATH,
        index=False
    )

def mark_processed(row_index):

    df = read_leads()

    df.loc[row_index,"Status"] = "Processed"

    df.to_excel(
        FILE_PATH,
        index=False
    )