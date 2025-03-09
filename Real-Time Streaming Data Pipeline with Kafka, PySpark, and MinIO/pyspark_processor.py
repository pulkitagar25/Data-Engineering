from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("KafkaToMinIO") \
    .config("spark.hadoop.fs.s3a.endpoint", "http://127.0.0.1:9000") \
    .config("spark.hadoop.fs.s3a.access.key", "fL5CShmE7V1uQ2LcSazD") \
    .config("spark.hadoop.fs.s3a.secret.key", "NPKOii7HyccNCgURB6kuL6Dzb0iyHbGUzLzg5LYf") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .getOrCreate()

print("✅ Spark Session Initialized Successfully")

# Read Data from MinIO
df = spark.read.json("s3a://kafka-data/input/")

# Show Data
df.show()

# Stop Spark
spark.stop()