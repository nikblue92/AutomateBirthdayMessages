# AutomateBirthdayMessages 🎂📱

A personal automation script that sends birthday SMS messages to family members — so I never forget to make someone's day special.

## 💡 Why I Built This

I'm forgetful with dates, especially birthdays. This project automates the process of sending thoughtful birthday messages, so I stay connected with the people I care about — automatically.

## 🚀 Features

- 📆 Tracks birthdays using a local data file (JSON or CSV)
- 🕐 Sends messages automatically on the correct day
- ✉️ Integrates with Twilio API for sending SMS
- 🔒 Keeps phone numbers and API keys secure via environment variables
- 📄 Logs sent messages to prevent duplicates

## 🔧 Technologies Used

- Python 3
- Twilio (for SMS sending)
- `schedule` or `cron` (for task scheduling)
- JSON or SQLite (for birthday data storage)

## 🛠 How to Use

1. Clone the repo:
   ```bash
   git clone https://github.com/nikblue92/AutomateBirthdayMessages.git
   cd AutomateBirthdayMessages
pip install flask
python main.py