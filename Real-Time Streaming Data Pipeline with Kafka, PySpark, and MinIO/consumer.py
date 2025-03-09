from kafka import KafkaConsumer
import json
import boto3
import pandas as pd
import io

import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

# Kafka Consumer
consumer = KafkaConsumer(
    'datastream',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# MinIO Configuration
MINIO_ENDPOINT = "http://127.0.0.1:9000"
MINIO_ACCESS_KEY = " "
MINIO_SECRET_KEY = ""
BUCKET_NAME = "streaming-bucket"

# Initialize MinIO Client
s3_client = boto3.client(
    's3',
    endpoint_url=MINIO_ENDPOINT,
    aws_access_key_id=MINIO_ACCESS_KEY,
    aws_secret_access_key=MINIO_SECRET_KEY
)

# List to store messages before writing to Parquet
batch_data = []
batch_size = 10  # Adjust batch size as needed

# Process Messages from Kafka
for message in consumer:
    data = message.value  # Extract data
    print(f'Consumed: {data}')
    
    batch_data.append(data)

    # Write to MinIO after collecting batch_size records
    if len(batch_data) >= batch_size:
        df = pd.DataFrame(batch_data)  # Convert to DataFrame
        
        # Convert DataFrame to Parquet in memory
        parquet_buffer = io.BytesIO()
        df.to_parquet(parquet_buffer, engine="pyarrow")  # Or use engine="fastparquet"

        # Upload to MinIO
        file_name = f"parquet/data_{message.offset}.parquet"
        s3_client.put_object(
            Bucket=BUCKET_NAME,
            Key=file_name,
            Body=parquet_buffer.getvalue()
        )

        print(f'✅ Data uploaded to MinIO: {file_name}')
        
        batch_data.clear()  # Clear the batch for the next cycle
