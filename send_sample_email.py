#!/usr/bin/env python3
"""
Send a sample girlfriend email to see the full formatting
"""

import os
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv


load_dotenv('config.env')

def send_sample_girlfriend_email():
    """Send a sample girlfriend email with full HTML formatting."""
    
    email_sender = os.getenv('EMAIL_SENDER')
    email_password = os.getenv('EMAIL_PASSWORD')
    email_recipient = os.getenv('EMAIL_RECIPIENT')
    
    if not all([email_sender, email_password, email_recipient]):
        print("❌ Email configuration incomplete!")
        return
    
    # Random girlfriend message
    morning_messages = [
        f"Good morning, sunshine! ☀️ Time to make Tesphase shine brighter than ever! Your solar energy startup is going to change the world, and I believe in you! 💚",
        f"Rise and shine, my love! 🌅 Another beautiful day to work on Tesphase. The sun is up, and so should your motivation be! Let's make today count! ⚡",
        f"Morning, babe! 🌞 Tesphase is waiting for your brilliant ideas. Remember, every solar panel you help install is a step toward a greener future. You've got this! 🌱",
        f"Hey gorgeous! ☀️ Time to wake up and conquer the solar energy world with Tesphase! Your passion for renewable energy is what drives me crazy (in a good way)! 💪",
        f"Good morning, my solar warrior! ⚡ Tesphase needs your attention today. Let's make the world a better place, one solar panel at a time! 🌍"
    ]
    
    message = random.choice(morning_messages)
    
    # Beautiful HTML email
    html_message = f"""
    <html>
    <body style="font-family: Arial, sans-serif; background-color: #f0f8ff; padding: 20px;">
        <div style="background-color: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h1 style="color: #2E8B57; text-align: center;">🌞 Good Morning, Solar Warrior! 🌞</h1>
            <p style="font-size: 18px; color: #333; line-height: 1.6;">{message}</p>
            
            <div style="background-color: #f8f9fa; padding: 20px; border-radius: 8px; margin: 20px 0;">
                <h3 style="color: #2E8B57;">📋 Today's Tesphase Focus Areas:</h3>
                <ul style="color: #555;">
                    <li>🔋 Solar panel efficiency research</li>
                    <li>💡 Renewable energy innovation</li>
                    <li>🌍 Environmental impact analysis</li>
                    <li>📊 Market research and competitor analysis</li>
                    <li>🤝 Partnership development</li>
                    <li>💰 Funding strategy and investor outreach</li>
                </ul>
            </div>
            
            <div style="background-color: #e8f5e8; padding: 15px; border-radius: 8px; margin: 20px 0; border-left: 4px solid #2E8B57;">
                <h4 style="color: #2E8B57; margin-top: 0;">💡 Today's Motivation:</h4>
                <p style="color: #555; margin-bottom: 0;">"Every great solar energy company started with a single idea and determination. Your Tesphase vision has the power to change the world!"</p>
            </div>
            
            <div style="text-align: center; margin-top: 30px;">
                <p style="color: #666; font-style: italic;">Remember: You're not just building a startup, you're building a greener future! 🌱</p>
                <p style="color: #2E8B57; font-weight: bold; font-size: 20px;">You've got this! 💚</p>
            </div>
            
            <div style="text-align: center; margin-top: 20px; padding-top: 20px; border-top: 1px solid #eee;">
                <p style="color: #999; font-size: 12px;">💌 Sent with love by your Tesphase Girlfriend Bot ⚡</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = email_sender
        msg['To'] = email_recipient
        msg['Subject'] = "🌞 Sample: Your Tesphase Girlfriend Email! ☀️"
        
        # Add HTML body
        msg.attach(MIMEText(html_message, 'html'))
        
        # Send email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_sender, email_password)
        text = msg.as_string()
        server.sendmail(email_sender, email_recipient, text)
        server.quit()
        
        print("✅ Sample girlfriend email sent successfully!")
        print(f"📧 Check your inbox at: {email_recipient}")
        print("🎨 This shows the beautiful HTML formatting you'll get daily!")
        
    except Exception as e:
        print(f"❌ Error sending email: {e}")

if __name__ == "__main__":
    print("💌 Sending Sample Girlfriend Email...")
    print("=" * 40)
    send_sample_girlfriend_email() 