import boto3

# ─── CONFIG ───────────────────────────────────────────
INSTANCE_ID = "i-0ae01d48abb983779"    # Replace with your EC2 Instance ID
ACTION       = "stop"               # Change to "stop" to stop the instance
FILE_PATH    = "/Users/damian/Desktop/airplane1.jpg"   # Local file to upload
BUCKET_NAME  = "damo-amazons3demo-bucket-123"     # Replace with your S3 bucket name
S3_KEY       = "uploaded/airplane1.jpg"  # Path inside the bucket
# ──────────────────────────────────────────────────────

ec2 = boto3.client("ec2", region_name="us-east-1")
s3  = boto3.client("s3", region_name="us-east-1")

# 1. List all S3 buckets
print("\n📦 S3 Buckets in your account:")
response = s3.list_buckets()
for bucket in response["Buckets"]:
    print(f"  - {bucket['Name']}")

# 2. Start or Stop EC2 instance
print(f"\n⚙️  {ACTION.capitalize()}ing EC2 instance: {INSTANCE_ID}")
if ACTION == "start":
    ec2.start_instances(InstanceIds=[INSTANCE_ID])
    print("  ✅ Start command sent.")
elif ACTION == "stop":
    ec2.stop_instances(InstanceIds=[INSTANCE_ID])
    print("  ✅ Stop command sent.")
else:
    print("  ⚠️  Invalid ACTION. Use 'start' or 'stop'.")

# 3. Upload a file to S3
print(f"\n⬆️  Uploading '{FILE_PATH}' to s3://{BUCKET_NAME}/{S3_KEY}")
s3.upload_file(FILE_PATH, BUCKET_NAME, S3_KEY)
print("  ✅ Upload complete.")


