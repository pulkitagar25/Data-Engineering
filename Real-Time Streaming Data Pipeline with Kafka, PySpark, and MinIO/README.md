# Real-Time Streaming Data Pipeline with Kafka, PySpark, and MinIO

## Overview
This project implements a **real-time data pipeline** using **Apache Kafka**, **PySpark Streaming**, and **MinIO (S3-compatible storage)**. The pipeline efficiently ingests, processes, and stores large-scale streaming data with **high scalability and low latency**.

## Architecture
1. **Kafka** – Handles real-time data ingestion with high throughput.
2. **PySpark Streaming** – Processes incoming data using micro-batch processing.
3. **MinIO** – Stores partitioned data for efficient retrieval and analytics.

## Features
- **Scalable Data Ingestion**: Kafka ensures real-time message streaming with fault tolerance.
- **Efficient Data Processing**: PySpark Streaming processes data in **5-minute intervals**.
- **Optimized Storage**: MinIO enables **partitioned storage** for fast retrieval.
- **Low Latency**: Reduces processing time, ensuring near real-time analytics.

## Setup Instructions
### Prerequisites
- Apache Kafka
- PySpark
- MinIO (or AWS S3)
- Python 3.x

### Installation
1. **Start Kafka Broker**
   ```sh
   kafka-server-start.sh config/server.properties
   ```
2. **Create Kafka Topic**
   ```sh
   kafka-topics.sh --create --topic real-time-data --bootstrap-server localhost:9092
   ```
3. **Run PySpark Streaming Job**
   ```sh
   spark-submit streaming_pipeline.py
   ```
4. **Store Data in MinIO**
   ```sh
   mc alias set myminio http://localhost:9000 ACCESS_KEY SECRET_KEY
   mc cp /processed_data myminio/bucket-name/
   ```

## Future Enhancements
- Implement **schema validation** for incoming data.
- Optimize **Kafka consumer offsets** for better fault tolerance.
- Enable **real-time analytics dashboard integration**.

## Contact
For queries or contributions, reach out at [agar.pulkit25@gmail.com](mailto:agar.pulkit25@gmail.com).
