# AWS Automation with Python & Boto3

A Python script that automates common AWS tasks using the Boto3 SDK — no manual console interaction required.

## 📋 What it Does
- Lists all S3 buckets in an AWS account
- Starts or stops an EC2 instance
- Uploads a file to an S3 bucket

## 🛠️ Technologies Used
- Python 3
- AWS Boto3 SDK
- Amazon S3
- Amazon EC2
- AWS CLI

## ⚙️ How to Run

### 1. Install dependencies
pip install boto3

### 2. Configure AWS credentials
aws configure

### 3. Update the config values in the script
INSTANCE_ID = "your-ec2-instance-id"
ACTION       = "start" or "stop"
FILE_PATH    = "path/to/your/file"
BUCKET_NAME  = "your-s3-bucket-name"

### 4. Run the script
python aws_script.py

## 💡 Skills Demonstrated
- Cloud infrastructure automation
- AWS SDK (Boto3)
- Python scripting
- EC2 and S3 management
- CLI proficiency
