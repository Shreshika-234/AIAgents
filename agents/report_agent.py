from services.excel_service import read_leads

def generate_report():

    df = read_leads()

    total_leads = len(df)

    verified = (df["Email Verified (Y/N)"] == "Y").sum()

    avg_score = df["Lead Priority (AI Score)"].mean()

    report = f"""
        Campaign Summary
        Total Leads: {total_leads}
        Verified Emails: {verified}
        Average Priority Score:
        {avg_score:.2f}
    """

    return report