#!/usr/bin/env python3
"""
Tesphase Girlfriend Bot - Automated Startup Reminder System
A bot that acts as a supportive "girlfriend" to remind you about your solar energy startup
and creates daily video summaries of your progress.
"""

import os
import json
import logging
import schedule
import time
from datetime import datetime, timedelta
from typing import List, Dict, Any
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import random
import requests
from dotenv import load_dotenv
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import pyttsx3
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip, TextClip, ImageClip
import threading

# Load environment variables
load_dotenv('config.env')

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('tesphase_bot.log'),
        logging.StreamHandler()
    ]
)

class TesphaseGirlfriendBot:
    def __init__(self):
        self.startup_name = os.getenv('STARTUP_NAME', 'Tesphase')
        self.startup_description = os.getenv('STARTUP_DESCRIPTION', 'Solar Energy Startup')
        self.email_sender = os.getenv('EMAIL_SENDER')
        self.email_password = os.getenv('EMAIL_PASSWORD')
        self.email_recipient = os.getenv('EMAIL_RECIPIENT')
        
        # Initialize text-to-speech engine
        self.tts_engine = pyttsx3.init()
        self.tts_engine.setProperty('rate', 150)
        self.tts_engine.setProperty('volume', 0.9)
        
        # Create directories
        self.create_directories()
        
        # Load progress data
        self.progress_file = 'tesphase_progress.json'
        self.load_progress()
        
        # Motivational messages
        self.morning_messages = [
            f"Good morning, sunshine! ☀️ Time to make Tesphase shine brighter than ever! Your solar energy startup is going to change the world, and I believe in you! 💚",
            f"Rise and shine, my love! 🌅 Another beautiful day to work on Tesphase. The sun is up, and so should your motivation be! Let's make today count! ⚡",
            f"Morning, babe! 🌞 Tesphase is waiting for your brilliant ideas. Remember, every solar panel you help install is a step toward a greener future. You've got this! 🌱",
            f"Hey gorgeous! ☀️ Time to wake up and conquer the solar energy world with Tesphase! Your passion for renewable energy is what drives me crazy (in a good way)! 💪",
            f"Good morning, my solar warrior! ⚡ Tesphase needs your attention today. Let's make the world a better place, one solar panel at a time! 🌍"
        ]
        
        self.reminder_messages = [
            f"Hey babe! 💕 Just checking in - how's Tesphase coming along? Don't forget to work on your solar energy startup today! I'm rooting for you! 🌟",
            f"Hi love! 🌞 Quick reminder: Tesphase won't build itself! Time to put on your solar energy hat and get to work! You're amazing! 💚",
            f"Hey there, sunshine! ☀️ Tesphase is calling your name! Your solar energy startup needs some TLC today. Go make it happen! ⚡",
            f"Hi babe! 💕 Just a friendly reminder that Tesphase is waiting for your magic touch! Your solar energy vision is going to change lives! 🌱",
            f"Hey gorgeous! 🌟 Tesphase time! Your solar energy startup is your baby, and babies need attention! Go nurture it! 💪"
        ]

    def create_directories(self):
        """Create necessary directories for the bot."""
        directories = ['videos', 'images', 'audio', 'logs']
        for directory in directories:
            os.makedirs(directory, exist_ok=True)

    def load_progress(self):
        """Load progress data from JSON file."""
        try:
            if os.path.exists(self.progress_file):
                with open(self.progress_file, 'r') as f:
                    self.progress_data = json.load(f)
            else:
                self.progress_data = {
                    'start_date': datetime.now().strftime('%Y-%m-%d'),
                    'daily_tasks': [],
                    'milestones': [],
                    'total_work_hours': 0,
                    'last_reminder': None
                }
                self.save_progress()
        except Exception as e:
            logging.error(f"Error loading progress: {e}")
            self.progress_data = {
                'start_date': datetime.now().strftime('%Y-%m-%d'),
                'daily_tasks': [],
                'milestones': [],
                'total_work_hours': 0,
                'last_reminder': None
            }

    def save_progress(self):
        """Save progress data to JSON file."""
        try:
            with open(self.progress_file, 'w') as f:
                json.dump(self.progress_data, f, indent=2)
        except Exception as e:
            logging.error(f"Error saving progress: {e}")

    def send_email_reminder(self, subject: str, message: str, attachment_path: str = None):
        """Send email reminder with optional attachment."""
        if not all([self.email_sender, self.email_password, self.email_recipient]):
            logging.error("Email configuration incomplete. Please check your .env file.")
            return False

        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = self.email_sender
            msg['To'] = self.email_recipient
            msg['Subject'] = subject

            # Add body
            msg.attach(MIMEText(message, 'html'))

            # Add attachment if provided
            if attachment_path and os.path.exists(attachment_path):
                with open(attachment_path, "rb") as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename= {os.path.basename(attachment_path)}'
                )
                msg.attach(part)

            # Send email
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.email_sender, self.email_password)
            text = msg.as_string()
            server.sendmail(self.email_sender, self.email_recipient, text)
            server.quit()

            logging.info(f"Email sent successfully: {subject}")
            return True

        except Exception as e:
            logging.error(f"Error sending email: {e}")
            return False

    def create_morning_reminder(self):
        """Create and send morning reminder email."""
        message = random.choice(self.morning_messages)
        
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
                
                <div style="text-align: center; margin-top: 30px;">
                    <p style="color: #666; font-style: italic;">Remember: Every great solar energy company started with a single idea and determination!</p>
                    <p style="color: #2E8B57; font-weight: bold;">You've got this! 💚</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        subject = f"🌞 Morning Motivation: Time to Make Tesphase Shine! ☀️"
        self.send_email_reminder(subject, html_message)
        
        # Update progress
        self.progress_data['last_reminder'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.save_progress()

    def create_daily_video(self):
        """Create a daily video summary about Tesphase progress."""
        try:
            # Create video content
            video_script = self.generate_video_script()
            
            # Create video with text overlay
            video_path = self.create_video_with_text(video_script)
            
            # Add audio narration
            final_video_path = self.add_audio_narration(video_path, video_script)
            
            logging.info(f"Daily video created: {final_video_path}")
            return final_video_path
            
        except Exception as e:
            logging.error(f"Error creating daily video: {e}")
            return None

    def generate_video_script(self):
        """Generate script for daily video."""
        today = datetime.now().strftime('%B %d, %Y')
        
        script = f"""
        Hey babe! It's {today} and I wanted to remind you about Tesphase, your amazing solar energy startup!
        
        Remember why you started this journey - to make the world a greener place, one solar panel at a time.
        
        Today's focus areas for Tesphase:
        • Research solar panel efficiency improvements
        • Explore renewable energy innovations
        • Analyze market opportunities
        • Connect with potential partners
        • Work on your funding strategy
        
        Your passion for solar energy is what makes you special. Don't let that fire go out!
        
        Go make Tesphase shine today! I believe in you! 💚
        """
        
        return script

    def create_video_with_text(self, script: str):
        """Create video with text overlay."""
        # Create a simple video with text
        width, height = 1280, 720
        duration = 15  # seconds
        
        # Create frames
        frames = []
        fps = 30
        
        for i in range(duration * fps):
            # Create background
            frame = np.zeros((height, width, 3), dtype=np.uint8)
            
            # Add gradient background
            for y in range(height):
                color = int(255 * (1 - y / height))
                frame[y, :] = [0, color//2, color//2]  # Green gradient
            
            # Add text overlay
            frame_pil = Image.fromarray(frame)
            draw = ImageDraw.Draw(frame_pil)
            
            # Try to use a default font, fallback to basic if not available
            try:
                font = ImageFont.truetype("arial.ttf", 40)
            except:
                font = ImageFont.load_default()
            
            # Add title
            title = f"Tesphase Daily Reminder - {datetime.now().strftime('%B %d, %Y')}"
            draw.text((width//2 - 300, 50), title, fill=(255, 255, 255), font=font)
            
            # Add script text (simplified for video)
            lines = [
                "Hey babe! Time to work on Tesphase!",
                "",
                "Your solar energy startup needs you!",
                "",
                "Focus areas for today:",
                "• Solar panel research",
                "• Market analysis", 
                "• Partnership development",
                "",
                "You've got this! 💚"
            ]
            
            y_offset = 150
            for line in lines:
                draw.text((width//2 - 200, y_offset), line, fill=(255, 255, 255), font=font)
                y_offset += 50
            
            frames.append(np.array(frame_pil))
        
        # Save video
        video_path = f"videos/tesphase_reminder_{datetime.now().strftime('%Y%m%d')}.mp4"
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(video_path, fourcc, fps, (width, height))
        
        for frame in frames:
            out.write(frame)
        
        out.release()
        return video_path

    def add_audio_narration(self, video_path: str, script: str):
        """Add audio narration to video."""
        try:
            # Generate audio from script
            audio_path = f"audio/narration_{datetime.now().strftime('%Y%m%d')}.mp3"
            
            # Use text-to-speech
            self.tts_engine.save_to_file(script, audio_path)
            self.tts_engine.runAndWait()
            
            # Combine video and audio
            video_clip = VideoFileClip(video_path)
            audio_clip = AudioFileClip(audio_path)
            
            # Ensure audio matches video duration
            if audio_clip.duration > video_clip.duration:
                audio_clip = audio_clip.subclip(0, video_clip.duration)
            
            final_video = video_clip.set_audio(audio_clip)
            final_path = f"videos/tesphase_final_{datetime.now().strftime('%Y%m%d')}.mp4"
            final_video.write_videofile(final_path, codec='libx264')
            
            # Clean up
            video_clip.close()
            audio_clip.close()
            final_video.close()
            
            return final_path
            
        except Exception as e:
            logging.error(f"Error adding audio narration: {e}")
            return video_path

    def send_evening_summary(self):
        """Send evening summary with video attachment."""
        video_path = self.create_daily_video()
        
        message = random.choice(self.reminder_messages)
        
        html_message = f"""
        <html>
        <body style="font-family: Arial, sans-serif; background-color: #f0f8ff; padding: 20px;">
            <div style="background-color: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                <h1 style="color: #2E8B57; text-align: center;">🌅 Evening Check-in: Tesphase Update 🌅</h1>
                <p style="font-size: 18px; color: #333; line-height: 1.6;">{message}</p>
                
                <div style="background-color: #f8f9fa; padding: 20px; border-radius: 8px; margin: 20px 0;">
                    <h3 style="color: #2E8B57;">📊 Today's Progress Summary:</h3>
                    <p style="color: #555;">I've created a daily video reminder for you! Check the attachment for your personalized Tesphase motivation video.</p>
                </div>
                
                <div style="text-align: center; margin-top: 30px;">
                    <p style="color: #666; font-style: italic;">Tomorrow is another opportunity to make Tesphase even better!</p>
                    <p style="color: #2E8B57; font-weight: bold;">Keep shining! ⚡</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        subject = f"🌅 Evening Update: Your Tesphase Journey Continues! 💚"
        
        if video_path:
            self.send_email_reminder(subject, html_message, video_path)
        else:
            self.send_email_reminder(subject, html_message)

    def run_scheduler(self):
        """Run the scheduled tasks."""
        # Morning reminder at 8:00 AM
        schedule.every().day.at("08:00").do(self.create_morning_reminder)
        
        # Evening summary at 6:00 PM
        schedule.every().day.at("18:00").do(self.send_evening_summary)
        
        # Mid-day reminder at 2:00 PM
        schedule.every().day.at("14:00").do(self.create_morning_reminder)
        
        logging.info("Tesphase Girlfriend Bot started! Scheduling tasks...")
        logging.info("Morning reminder: 8:00 AM")
        logging.info("Mid-day reminder: 2:00 PM") 
        logging.info("Evening summary: 6:00 PM")
        
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute

    def test_email(self):
        """Test email functionality."""
        subject = "🧪 Test Email: Tesphase Girlfriend Bot is Working! 💚"
        message = """
        <html>
        <body style="font-family: Arial, sans-serif; background-color: #f0f8ff; padding: 20px;">
            <div style="background-color: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                <h1 style="color: #2E8B57; text-align: center;">🎉 Tesphase Girlfriend Bot Test 🎉</h1>
                <p style="font-size: 18px; color: #333; line-height: 1.6;">
                    Hey babe! This is a test email from your Tesphase Girlfriend Bot! 
                    If you're receiving this, everything is working perfectly! 💚
                </p>
                <div style="text-align: center; margin-top: 30px;">
                    <p style="color: #2E8B57; font-weight: bold;">Your solar energy startup reminder system is ready! ⚡</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        success = self.send_email_reminder(subject, message)
        if success:
            print("✅ Test email sent successfully!")
        else:
            print("❌ Test email failed. Check your configuration.")

def main():
    """Main function to run the bot."""
    print("🌞 Welcome to Tesphase Girlfriend Bot! 🌞")
    print("Your automated solar energy startup reminder system")
    print("=" * 50)
    
    bot = TesphaseGirlfriendBot()
    
    # Check if this is a test run
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        print("Running test mode...")
        bot.test_email()
        return
    
    print("Starting Tesphase Girlfriend Bot...")
    print("The bot will send you morning reminders and create daily videos about Tesphase!")
    print("Press Ctrl+C to stop the bot")
    
    try:
        bot.run_scheduler()
    except KeyboardInterrupt:
        print("\n👋 Tesphase Girlfriend Bot stopped. Goodbye!")

if __name__ == "__main__":
    main() 