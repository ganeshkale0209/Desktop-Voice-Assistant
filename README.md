# Desktop-Voice-Assistant
Project Description
A Python-based desktop voice assistant that can recognize speech commands, perform web searches, retrieve weather updates, open applications, and respond to queries using Wikipedia, Wolfram Alpha, and other APIs. This assistant also features a GUI-based login system.

Features
Speech recognition and voice response
Web searches (Google, YouTube, Wikipedia, Stack Overflow)
Weather information retrieval
Time announcements
News updates from Times of India
Personal greeting based on the time of day
Ability to take photos using the webcam
Basic system commands (log off, sign out)

Prerequisites
Before running this project, ensure you have the following installed:
Python 3.x
PyCharm (for easy development and execution)

Installation Steps

Step 1: Install Python
Download and install Python from python.org.
Make sure to check "Add Python to PATH" during installation.

Step 2: Install PyCharm
Download and install PyCharm from JetBrains.
Open PyCharm and create a new Python project.

Step 3: Clone the Repository

    git clone https://github.com/yourusername/Desktop-Voice-Assistant.git
    cd Desktop-Voice-Assistant

Step 4: Install Required Python Packages
Run the following command to install dependencies:

    pip install -r requirements.txt
    If requirements.txt is not available, manually install the required packages:
    pip install speechrecognition pyttsx3 wikipedia webbrowser requests ecapture wolframalpha tkinter

Step 5: Run the Assistant

    python assistant.py

Usage Instructions

Run the script and enter the login credentials:
    Username: admin
    Password: admin123
Speak commands like:
    "Open YouTube"
    "Search Wikipedia for Python programming"
    "Tell me the time"
    "What's the weather like in Mumbai?"
    "Take a photo"
Say "Goodbye" or "Stop" to exit the assistant.

Customization
    Modify the wishMe() function for a personalized greeting.
    Change login credentials in the login_window() function.
    Update API keys for weather and Wolfram Alpha queries.

Troubleshooting
    If speech recognition fails, check your microphone permissions.
    If API requests fail, verify your internet connection and API keys.
