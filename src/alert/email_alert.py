import smtplib
from email.mime.text import MIMEText

class EmailAlert():
    """
    Sends email alerts when suspicious content is detected
    """
    def __init__(self, smtp_server, smtp_port, sender, password, receiver):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender = sender
        self.password = password
        self.receiver = receiver
    
    def send_alert(self, subject, body):
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["Body"] = self.sender
        msg["To"] = self.receiver
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender, self.password)
                server.send_message(msg)
            print("[INFO] Alert sent successfully.")
        except Exception as e:
            print(f"[ERROR] Failed to send email: {e}")