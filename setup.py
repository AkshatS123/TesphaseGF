#!/usr/bin/env python3
"""
Setup script for Tesphase Girlfriend Bot
Helps with initial configuration and installation
"""

import os
import sys
import subprocess
import shutil

def install_requirements():
    """Install required packages."""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Packages installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing packages: {e}")
        return False

def create_config_file():
    """Create configuration file from template."""
    if os.path.exists('config.env'):
        print("⚠️  config.env already exists. Skipping...")
        return True
    
    print("⚙️  Creating configuration file...")
    try:
        shutil.copy('config.env.example', 'config.env')
        print("✅ Configuration file created!")
        print("📝 Please edit config.env with your email settings")
        return True
    except FileNotFoundError:
        print("❌ config.env.example not found!")
        return False

def create_directories():
    """Create necessary directories."""
    directories = ['videos', 'images', 'audio', 'logs']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    print("📁 Directories created successfully!")

def main():
    """Main setup function."""
    print("🌞 Tesphase Girlfriend Bot Setup 🌞")
    print("=" * 40)
    
    # Create directories
    create_directories()
    
    # Install requirements
    if not install_requirements():
        print("❌ Setup failed during package installation")
        return
    
    # Create config file
    if not create_config_file():
        print("❌ Setup failed during configuration")
        return
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Edit config.env with your email settings")
    print("2. Generate a Gmail App Password (not regular password)")
    print("3. Run: python tesphase_girlfriend_bot.py test")
    print("4. If test passes, run: python tesphase_girlfriend_bot.py")
    print("\n💡 The bot will send you morning reminders at 8:00 AM and evening summaries at 6:00 PM")

if __name__ == "__main__":
    main() 