import boto3
import requests
import sys

file_url = sys.argv[1]  

bucket_name = sys.argv[2]  # string
object_name = file_url.split("/")[-1]  # string
expires_in = int(sys.argv[3])  # integer

response = requests.get(file_url)
with open(object_name, "wb") as file:
    file.write(response.content)

s3 = boto3.client("s3")

s3.upload_file(object_name, bucket_name, object_name)

presigned_url = s3.generate_presigned_url(
    "get_object",
    Params={"Bucket": bucket_name, "Key": object_name},
    ExpiresIn=expires_in
)

print("\nPresigned URL (valid for", expires_in, "seconds):")
print(presigned_url)
