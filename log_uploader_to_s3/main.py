import boto3
import os
from datetime import datetime
from dotenv import load_dotenv
import logging

load_dotenv()
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
AWS_REGION = os.getenv("AWS_REGION")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
SOURCE_LOG_FOLDER = os.getenv("SOURCE_LOG_FOLDER")
S3_BASE_FOLDER = os.getenv("S3_BASE_FOLDER")

logging.basicConfig(
    filename= "upload_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

today=datetime.now().strftime("%Y-%m-%d")

try :
    s3 = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name=AWS_REGION
    )

except Exception as e:
    logging.error(f"❌ Failed to connect to S3: {str(e)}")
    exit(1)

try:
    files = [
        f for f in os.listdir(SOURCE_LOG_FOLDER) if f.endswith((".log", ".txt"))
        and os.path.isfile(os.path.join(SOURCE_LOG_FOLDER, f))
    ]
except FileNotFoundError:
    logging.error(f"❌ Source log folder '{SOURCE_LOG_FOLDER}' not found.")
    exit(1)

if not files:
    logging.info("⏸ No log files found to upload.")
    print("⏸ No log files found.")
    exit()

for file_name in files:
    local_path=os.path.join(SOURCE_LOG_FOLDER, file_name)
    s3_key=f"{S3_BASE_FOLDER}/{today}/{file_name}"

    try:
        s3.upload_file(local_path, S3_BUCKET_NAME, s3_key)
        logging.info(f"✅ Uploaded: {file_name} → s3://{S3_BUCKET_NAME}/{s3_key}")
        print(f"✅ Uploaded: {file_name}")
    except Exception as e:
        logging.error(f"❌ Failed to upload {file_name}: {str(e)}")
        print(f"❌ Failed: {file_name} - {str(e)}")