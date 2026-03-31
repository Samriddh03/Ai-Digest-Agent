import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

SENDER = os.getenv("EMAIL_SENDER")
PASSWORD = os.getenv("EMAIL_PASSWORD")
RECEIVER = os.getenv("EMAIL_RECEIVER")


def send_email(content):
    msg = MIMEText(content, "plain")
    msg["Subject"] = "🚀 Daily AI Digest"
    msg["From"] = SENDER
    msg["To"] = RECEIVER

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER, PASSWORD)
        server.send_message(msg)