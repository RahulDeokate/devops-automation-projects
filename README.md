# 🚀 DevOps Automation Projects    Auther - Rahul Deokate

This repository contains 5 real-world DevOps automation projects using Python, Git, GitHub, AWS, Jira, and Jenkins. These mini-projects demonstrate automation, scripting, and integration skills required for DevOps roles, all organized and documented for practical learning and showcasing on GitHub.

---

## 📁 Projects Overview

| No. | Project Name             | Description |
|-----|--------------------------|-------------|
| 1️⃣  | **Jira Issue Creator**     | Automates Jira issue creation via REST API using Python |
| 2️⃣  | **EC2 Scheduler**          | Starts and stops AWS EC2 instances based on tags and time |
| 3️⃣  | **GitHub Repo Analyzer**   | Extracts details of any GitHub public repository using GitHub API |
| 4️⃣  | **Jenkins Monitor**        | Monitors Jenkins build job status using Jenkins REST API |
| 5️⃣  | **Log Uploader to S3**     | Uploads system/server logs to an AWS S3 bucket for backup |

---

## 🧰 Tools & Technologies Used

- **Languages**: Python, Shell Scripting
- **Cloud**: AWS (EC2, S3, IAM)
- **CI/CD**: Jenkins
- **Project Management**: Jira
- **Version Control**: Git & GitHub
- **Libraries**: `requests`, `boto3`, `python-dotenv`

---

## 🔧 Folder Structure

devops-automation-projects/
├── jira_issue_creator/
│ ├── main.py
│ ├── .env
│ ├── README.md
│ ├── requirements.txt
│ ├── .gitignore
├── ec2_scheduler/
│ └── ...
├── github_repo_analyzer/
│ └── ...
├── jenkins_monitor/
│ └── ...
├── log_uploader/
│ └── ...
└── README.md (this file)

Each project folder contains:

- `main.py` – main automation script  
- `.env` – environment variables (excluded in `.gitignore`)  
- `README.md` – individual project documentation  
- `requirements.txt` – Python dependencies  
- `.gitignore` – to secure sensitive data  

---

## 🚀 How to Use This Repository

Step 1: Clone the repo
```bash
git clone https://github.com/RahulDeokate/devops-automation-projects.git
cd devops-automation-projects

Step 2: Navigate to Any Project
bash
Copy
Edit
cd jira_issue_creator

Step 3: Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Step 4: Add Your .env File
Each project needs its own .env file. Refer to the individual README.md inside the folder for required keys.

Step 5: Run the Script
bash
Copy
Edit
python main.py