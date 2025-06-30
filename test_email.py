#!/usr/bin/env python3
"""
Simple email test script to debug email sending issues
"""

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load environment variables
load_dotenv('config.env')

def test_email_connection():
    """Test email connection and send a simple test email."""
    
    # Get email settings
    email_sender = os.getenv('EMAIL_SENDER')
    email_password = os.getenv('EMAIL_PASSWORD')
    email_recipient = os.getenv('EMAIL_RECIPIENT')
    
    print("🔍 Email Configuration Check:")
    print(f"Sender: {email_sender}")
    print(f"Recipient: {email_recipient}")
    print(f"Password: {'*' * len(email_password) if email_password else 'NOT SET'}")
    print()
    
    if not all([email_sender, email_password, email_recipient]):
        print("❌ Missing email configuration!")
        return False
    
    try:
        print("🔌 Testing SMTP connection...")
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = email_sender
        msg['To'] = email_recipient
        msg['Subject'] = "Test Email from Tesphase Bot"
        
        body = """
        This is a test email from your Tesphase Girlfriend Bot!
        
        If you receive this, the email configuration is working correctly.
        
        Time sent: {time}
        """.format(time=os.popen('date /t & time /t').read().strip())
        
        msg.attach(MIMEText(body, 'plain'))
        
        print("📧 Connecting to Gmail SMTP...")
        
        # Connect to Gmail SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        print("🔐 Attempting login...")
        server.login(email_sender, email_password)
        
        print("📤 Sending email...")
        text = msg.as_string()
        server.sendmail(email_sender, email_recipient, text)
        server.quit()
        
        print("✅ Email sent successfully!")
        print(f"📧 Check your inbox at: {email_recipient}")
        print("📁 Also check your spam/junk folder")
        
        return True
        
    except smtplib.SMTPAuthenticationError as e:
        print(f"❌ Authentication failed: {e}")
        print("💡 Make sure you're using an App Password, not your regular Gmail password")
        print("🔗 Generate App Password: https://myaccount.google.com/apppasswords")
        return False
        
    except smtplib.SMTPRecipientsRefused as e:
        print(f"❌ Recipient email rejected: {e}")
        print("💡 Check if the recipient email address is correct")
        return False
        
    except smtplib.SMTPServerDisconnected as e:
        print(f"❌ Server disconnected: {e}")
        print("💡 Check your internet connection")
        return False
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def check_gmail_settings():
    """Provide guidance on Gmail settings."""
    print("\n🔧 Gmail Setup Checklist:")
    print("1. ✅ Enable 2-Step Verification")
    print("2. ✅ Generate App Password:")
    print("   - Go to: https://myaccount.google.com/apppasswords")
    print("   - Select 'Mail' and your device")
    print("   - Copy the 16-character password")
    print("3. ✅ Use App Password in config.env (not regular password)")
    print("4. ✅ Make sure 'Less secure app access' is OFF")
    print("5. ✅ Check spam/junk folder for test emails")

if __name__ == "__main__":
    print("🧪 Tesphase Email Test")
    print("=" * 30)
    
    success = test_email_connection()
    
    if not success:
        check_gmail_settings()
    
    print("\n💡 If still not working, try:")
    print("- Check your internet connection")
    print("- Verify Gmail account settings")
    print("- Try a different email address for testing") 