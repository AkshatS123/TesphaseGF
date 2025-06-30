# 🌞 Tesphase Girlfriend Bot 🌞

Your automated solar energy startup reminder system that acts as a supportive "girlfriend" to keep you motivated and on track with your Tesphase solar energy startup!

## ✨ Features

- **🌅 Morning Motivation**: Daily email reminders at 8:00 AM to start your day focused on Tesphase
- **📹 Daily Video Summaries**: Automated video creation with motivational content about your solar energy startup
- **🌅 Evening Check-ins**: Evening summaries at 6:00 PM with video attachments
- **💚 Personalized Messages**: Supportive, girlfriend-style messages to keep you motivated
- **📊 Progress Tracking**: Tracks your startup journey and milestones
- **🎵 Text-to-Speech**: Narrated videos with motivational content

## 🚀 Quick Start

### 1. Setup

```bash
# Clone or download the project
# Navigate to the project directory
cd TesphaseGF

# Run the setup script
python setup.py
```

### 2. Configure Email

1. Edit `config.env` with your email settings:
```env
EMAIL_SENDER=your-email@gmail.com
EMAIL_PASSWORD=your-app-password
EMAIL_RECIPIENT=your-email@gmail.com
STARTUP_NAME=Tesphase
STARTUP_DESCRIPTION=Solar Energy Startup
```

2. **Important**: Generate a Gmail App Password:
   - Go to Google Account Settings
   - Security → 2-Step Verification → App passwords
   - Generate a new app password for "Mail"
   - Use this password (not your regular Gmail password)

### 3. Test the Bot

```bash
# Test email functionality
python tesphase_girlfriend_bot.py test
```

### 4. Run the Bot

```bash
# Start the automated reminder system
python tesphase_girlfriend_bot.py
```

## 📅 Schedule

The bot runs on the following schedule:

- **8:00 AM**: Morning motivation email with Tesphase focus areas
- **2:00 PM**: Mid-day reminder to stay on track
- **6:00 PM**: Evening summary with daily video attachment

## 🎬 Video Features

The bot creates personalized videos that include:

- **Solar-themed backgrounds** with green gradients
- **Motivational text overlays** about Tesphase
- **Text-to-speech narration** with supportive messages
- **Daily focus areas** for your solar energy startup
- **Professional styling** with startup branding

## 📁 Project Structure

```
TesphaseGF/
├── tesphase_girlfriend_bot.py    # Main bot application
├── setup.py                      # Setup and installation script
├── requirements.txt              # Python dependencies
├── config.env.example           # Configuration template
├── config.env                   # Your configuration (create this)
├── README.md                    # This file
├── videos/                      # Generated video files
├── images/                      # Image assets
├── audio/                       # Audio files
└── logs/                        # Log files
```

## 🔧 Customization

### Modify Messages

Edit the `morning_messages` and `reminder_messages` lists in `tesphase_girlfriend_bot.py` to customize the supportive messages.

### Change Schedule

Modify the `run_scheduler()` method to change when reminders are sent:

```python
# Example: Change morning reminder to 7:30 AM
schedule.every().day.at("07:30").do(self.create_morning_reminder)
```

### Customize Video Content

Edit the `generate_video_script()` method to change video content and focus areas.

## 🛠️ Troubleshooting

### Email Issues

- **"Authentication failed"**: Make sure you're using an App Password, not your regular Gmail password
- **"SMTP error"**: Check your internet connection and Gmail settings
- **"Configuration incomplete"**: Verify all fields in `config.env` are filled

### Video Issues

- **"OpenCV error"**: Install OpenCV: `pip install opencv-python`
- **"MoviePy error"**: Install MoviePy: `pip install moviepy`
- **"Text-to-speech error"**: Install pyttsx3: `pip install pyttsx3`

### General Issues

- **"Module not found"**: Run `pip install -r requirements.txt`
- **"Permission denied"**: Make sure you have write permissions in the project directory

## 🌟 Tesphase Focus Areas

The bot reminds you about these key areas for your solar energy startup:

- 🔋 **Solar Panel Efficiency Research**
- 💡 **Renewable Energy Innovation**
- 🌍 **Environmental Impact Analysis**
- 📊 **Market Research & Competitor Analysis**
- 🤝 **Partnership Development**
- 💰 **Funding Strategy & Investor Outreach**

## 💚 Motivation

Remember why you started Tesphase:
- **Make the world greener** one solar panel at a time
- **Innovate renewable energy** solutions
- **Create sustainable impact** for future generations
- **Build something meaningful** that helps the planet

## 📞 Support

If you need help with your Tesphase startup or the bot:

1. Check the logs in the `logs/` directory
2. Review the configuration in `config.env`
3. Test individual components with the test mode

## 🎯 Success Tips

- **Consistency**: Let the bot remind you daily to work on Tesphase
- **Focus**: Use the suggested focus areas to stay organized
- **Progress**: Track your milestones and celebrate small wins
- **Persistence**: Every great solar energy company started with determination

---

**Remember**: Your passion for solar energy is what makes you special. Don't let that fire go out! 💚⚡

*Built with love for your Tesphase solar energy startup journey* 🌞 