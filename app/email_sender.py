import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email(content):
    message = Mail(
        from_email=os.getenv("EMAIL_SENDER"),
        to_emails=os.getenv("EMAIL_RECEIVER"),
        subject="🚀 Daily AI Digest",
        plain_text_content=content
    )

    try:
        sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
        sg.send(message)
    except Exception as e:
        print("Email error:", e)