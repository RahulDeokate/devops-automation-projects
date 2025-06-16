# ☁️ Log Uploader to S3

## 📖 Description
A Python script to automatically upload system/server log files to an AWS S3 bucket for storage and future analysis.

## 🎯 Objective
Automate the process of backing up logs to the cloud using AWS SDK.

## 🧰 Tools & Technologies
- Python
- AWS S3 + IAM
- `boto3`, `dotenv`
- Git & GitHub

## 🛠️ Features
- Upload local logs to AWS S3
- Use `.env` for secure credential management
- Append results to log file
- Can be scheduled with cron for automation

## 📁 Project Structure

log_uploader/
├── main.py
├── .env
├── README.md
├── requirements.txt
├── .gitignore
└── upload_logs.log
