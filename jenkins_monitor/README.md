# 🛠️ Jenkins Job Monitor

## 📖 Description
A simple Python script to monitor the status of Jenkins jobs using the Jenkins REST API.

## 🎯 Objective
To get the real-time build status of a Jenkins job and optionally log it for analysis or alerts.

## 🧰 Tools & Technologies
- Python
- Jenkins REST API
- `requests` and `dotenv`

## 🛠️ Features
- Fetch last build status of any Jenkins job
- Use `.env` for secure credentials
- Logs job status to `logs.txt`
- Easy to extend with alerting or Slack notifications

## 📁 Project Structure

jenkins_monitor/
├── main.py
├── .env
├── README.md
├── requirements.txt
├── .gitignore
└── logs.txt