import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("REPO_NAME")

url = f"https://api.github.com/repos/{REPO_NAME}"

headers = {
    "Autorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json" 
}

responce = requests.get(url,headers=headers)

if responce.status_code==200:
    data=responce.json()

    full_name = data.get("full_name")
    stars = data.get("stargazers_count")
    forks = data.get("forks_count")
    issues = data.get("open_issues_count")
    updated = data.get("updated_at")
    license_data = data.get("license")
    license = license_data["name"] if license_data else "N/A"
    repo_url = data.get("html_url")

    # Format output
    report = f"""
    📊 GitHub Repo Report - {full_name}
    ---------------------------------------
    ⭐ Stars         : {stars}
    🍴 Forks         : {forks}
    🐞 Open Issues   : {issues}
    🕐 Last Updated  : {updated}
    ✅ License       : {license}
    🔗 URL           : {repo_url}
    📝 Generated At  : {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    """
    with open ("report.txt", "w", encoding="utf-8") as file:
        file.write(report.strip())
        print("✅ Report generated successfully: report.txt")

else:
    print(f"Failed to fetch the repositery : {responce.status_code}")
    print(f"{responce.text}")