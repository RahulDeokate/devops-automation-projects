# ⚙️ EC2 Scheduler

## 📖 Description
This script allows you to **start or stop EC2 instances** on AWS using Python. It's useful for reducing AWS costs by automating instance management during non-working hours.

## 🎯 Objective
Automate the starting and stopping of EC2 instances using a Python script and environment configuration.

## 🧰 Tools & Technologies
- Python
- Boto3 (AWS SDK for Python)
- AWS EC2
- `dotenv` for secure credentials
- Git & GitHub

## 🛠️ Features
- Start EC2 instances with one command
- Stop EC2 instances with another
- Logs each action with timestamp
- Uses `.env` for secure credentials

## 📁 Project Structure

ec2_scheduler/
├── main.py
├── .env
├── README.md
├── requirements.txt
├── .gitignore
└── logs.txt