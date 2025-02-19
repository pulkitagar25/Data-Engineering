import os
from dotenv import load_dotenv
from minio import Minio
from minio.error import S3Error

load_dotenv()

# Load environment variables

access_key = os.getenv("MINIO_ACCESS_KEY")
secret_key = os.getenv("MINIO_SECRET_KEY")

def main():

    client = Minio("192.168.91.197:9000",  
        access_key=access_key,  
        secret_key=secret_key, 
        secure=False # Set to False for local, HTTP connection. True for HTTPS.
    )

    # The file to upload, change this path if needed
    source_file = "steps.txt"

    # The destination bucket and filename on the MinIO server
    bucket_name = "python-test-bucket"
    destination_file = "my-test-file.txt"
    
    # Make the bucket if it doesn't exist.
    found = client.bucket_exists(bucket_name)
    if not found:
        client.make_bucket(bucket_name)
        print("Created bucket", bucket_name)
    else:
        print("Bucket", bucket_name, "already exists")

    # Upload the file, renaming it in the process
    client.fput_object(
        bucket_name, destination_file, source_file,
    )
    print(
        source_file, "successfully uploaded as object",
        destination_file, "to bucket", bucket_name,
    )

if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)