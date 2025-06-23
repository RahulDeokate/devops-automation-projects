import os
from dotenv import load_dotenv
import requests

load_dotenv()

auth = (os.getenv("JIRA_EMAIL"), os.getenv("JIRA_API_TOKEN"))
url = os.getenv("JIRA_URL") + "/rest/api/3/myself"

res = requests.get(url, auth=auth)
print(res.status_code)
print(res.json())