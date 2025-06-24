import boto3
import os
from datetime import datetime
from dotenv import load_dotenv
import logging

load_dotenv()
AWS_ACCESS_KEY= os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
AWS_REGION = os.getenv("AWS_REGION")
START_HOUR = int(os.getenv("START_HOUR", 9))
STOP_HOUR = int(os.getenv("STOP_HOUR"))
TAG_KEY = os.getenv("TAG_KEY", "AutoSchedule")
TAG_VALUE = os.getenv("TAG_VALUE", "Yes")

ec2= boto3.resource(
    "ec2",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)

current_hour=datetime.now().hour

filters = [
    { "Name" : f"tag:{TAG_KEY}", "Values" : [TAG_VALUE]},
    { "Name" : "instance-state-name", "Values" : ["running", "stopped"]}
]

instances=ec2.instances.filter(Filters=filters)

for instance in instances:
    instance_id=instance.id
    state=instance.state["Name"]

    try :
        if current_hour == START_HOUR and state == "stopped" :
            instance.start()
            with open("logs.txt", "a") as log:
                log.write(f"{datetime.now()} Instance Started : {instance_id}")
            print(f"Instance started : {instance_id}")

        elif current_hour == STOP_HOUR and state == "running" :
                instance.stop()
                with open ("logs.txt", "a") as log:
                    log.write(f"{datetime.now()} Instance Stopped : {instance_id}")
                print(f"Instance Stopped : {instance_id}")

        else:
             with open ("logs.txt", "a") as log:
                    log.write(f"{datetime.now()} No action for Instance : {instance_id}")

    except Exception as e:
        logging.error(f"❌ Failed to handle instance {instance_id}: {str(e)}")
        print(f"❌ Failed to handle instance {instance_id}: {str(e)}")

