# Twitter Airflow Data Engineering Project

This project extracts tweets from Elon Musk's Twitter account using Twitter API v2, processes them, and stores the data in an Amazon S3 bucket. The process is automated using Apache Airflow.

## Overview

The project is designed to fetch recent tweets, extract relevant metadata, and store the data for further analysis. It integrates with AWS S3 for storage and uses Airflow for scheduling.

## Features

- Fetches recent tweets from Twitter API v2.
- Extracts tweet metadata including text, likes, retweets, and timestamps.
- Saves the extracted data as a CSV file.
- Uploads the CSV file to an Amazon S3 bucket.
- Automates the ETL process using Apache Airflow.

## Components

- **Twitter API v2**: Used to fetch tweets.
- **Tweepy**: Python library to interact with the Twitter API.
- **Pandas**: Used for data transformation and storage.
- **Amazon S3**: Cloud storage for storing extracted data.
- **Apache Airflow**: Used for scheduling and automating the ETL process.

## Workflow

1. Authenticate with the Twitter API using API credentials.
2. Fetch the latest tweets from Elon Musk's Twitter account.
3. Extract relevant data such as tweet text, likes, retweets, and timestamps.
4. Store the extracted data in a CSV file.
5. Upload the CSV file to an Amazon S3 bucket.
6. Use Apache Airflow to schedule and automate the ETL pipeline.

## Usage

- The script runs on an EC2 instance and extracts tweets at scheduled intervals.
- Apache Airflow ensures the process runs automatically as per the defined schedule.
- The extracted tweets can be used for sentiment analysis, trend tracking, or other data analytics tasks.

## Author

Pulkit Agarwal
