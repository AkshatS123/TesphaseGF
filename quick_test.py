#!/usr/bin/env python3
"""
Quick test - send email to sender address to verify delivery
"""

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv('config.env')

def send_test_to_sender():
    """Send test email to the sender address itself."""
    
    email_sender = os.getenv('EMAIL_SENDER')
    email_password = os.getenv('EMAIL_PASSWORD')
    
    print(f"📧 Sending test email to: {email_sender}")
    
    try:
        msg = MIMEMultipart()
        msg['From'] = email_sender
        msg['To'] = email_sender  # Send to self
        msg['Subject'] = "Self-Test: Tesphase Bot Email Working"
        
        body = """
        This is a self-test email from your Tesphase Girlfriend Bot!
        
        If you receive this email, the bot is working correctly.
        
        The issue might be:
        1. Emails to s.akshat@gmail.com are being filtered
        2. Check spam/junk folder
        3. Gmail settings need adjustment
        
        Time: """ + os.popen('date /t & time /t').read().strip()
        
        msg.attach(MIMEText(body, 'plain'))
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_sender, email_password)
        
        text = msg.as_string()
        server.sendmail(email_sender, email_sender, text)
        server.quit()
        
        print("✅ Self-test email sent!")
        print(f"📧 Check your inbox at: {email_sender}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    send_test_to_sender() 