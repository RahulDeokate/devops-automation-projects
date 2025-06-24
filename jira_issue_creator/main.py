import os
import requests
from dotenv import load_dotenv
from datetime import datetime

#load imvironment veriables from .env file
load_dotenv()
JIRA_EMAIL=os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN=os.getenv("JIRA_API_TOKEN")
JIRA_PROJECT_KEY=os.getenv("PROJECT_KEY")
JIRA_URL=os.getenv("JIRA_URL") + "/rest/api/3/issue"

#setting headers and basic authentication
auth = (JIRA_EMAIL, JIRA_API_TOKEN)
headers= {
    "Accept" : "application/json",
    "Content-Type" : "application/json"
}

#prepare issue content
summery="This is auto generated icket"
description = {
    "type": "doc",
    "version": 1,
    "content": [
        {
            "type": "paragraph",
            "content": [
                {
                    "type": "text",
                    "text": "This ticket was created using Jira REST API and Python."
                }
            ]
        }
    ]
}

issue_data = {
    "fields" : {
        "project" : { "key" : JIRA_PROJECT_KEY},
        "summary" : summery,
        "description" : description,
        "issuetype" : { "name" : "Bug"} 
    }
}

#send post requeat to jira
responce=requests.post(JIRA_URL, json=issue_data, headers=headers, auth=auth)

#handle responce
if responce.status_code == 201 :
    issue_key=responce.json().get("key")
    with open("logs.txt", "a") as log :
        log.write(f"{datetime.now()} : Jira ticket created successfuly {issue_key}\n")
    print(f"Ticket created successfuly : {issue_key}")
    
else:
    print(f" Failed to create ticket : {responce.status_code}")
    print(responce.text)
    with open("logs.txt", "a") as log :
        log.write(f"{datetime.now()} : failed to generate ticket {responce.status_code}\n")
        log.write(responce.text + "\n")
    

