import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
JENKINS_URL = os.getenv("JENKINS_URL")
JENKINS_USERNAME = os.getenv("JENKINS_USERNAME")
JENKINS_API_TOKEN = os.getenv("JENKINS_API_TOKEN")
JOB_NAME = os.getenv("JOB_NAME")

api_url = f"{JENKINS_URL}/job/{JOB_NAME}/lastBuild/api/json"

try:
    response = requests.get(api_url, auth=(JENKINS_USERNAME, JENKINS_API_TOKEN))

    if response.status_code == 200:
        data = response.json()
        build_result = data.get("result", "UNKNOWN")
        build_url = data.get("url", "N/A")
        duration_ms = data.get("duration", 0)
        duration_min = round(duration_ms / 60000, 2)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

        log_message = (
            f"[{timestamp}] 🛠️ Build Status: {build_result} | "
            f"Duration: {duration_min} min | URL: {build_url}"
        )

        # Print and log
        print(log_message)
        with open("logs.txt", "a", encoding="utf-8") as log:
            log.write(log_message + "\n")

    else:
        print(f"❌ Failed to fetch job status: {response.status_code}")
        with open("logs.txt", "a", encoding="utf-8") as log:
            log.write(f"[{datetime.now()}] ❌ Failed to fetch job status: {response.status_code}\n")
            log.write(response.text + "\n")

except requests.exceptions.RequestException as e:
    print(f"❗ Error connecting to Jenkins: {e}")
    with open("logs.txt", "a", encoding="utf-8") as log:
        log.write(f"[{datetime.now()}] ❗ Connection error: {str(e)}\n")