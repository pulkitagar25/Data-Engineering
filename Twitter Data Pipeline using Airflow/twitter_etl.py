import tweepy
import pandas as pd
from datetime import datetime
import time
import boto3

def run_twitter_etl():
    # Twitter API v2 Bearer Token
    bearer_token = "YOUR_BEARER_TOKEN"  
    
    # Authenticate using tweepy Client
    client = tweepy.Client(bearer_token=bearer_token)
    
    # Elon Musk's Twitter user ID
    user_id = "44196397"  # Elon Musk's user ID
    
    # Fetch only 5 tweets to conserve API quota
    tweets = client.get_users_tweets(
        id=user_id, 
        max_results=5,  # Reduced from 100 to 5
        tweet_fields=["created_at", "public_metrics"]
    )
    
    tweet_list = []
    if tweets.data:
        for tweet in tweets.data:
            refined_tweet = {
                "user": "elonmusk",
                "text": tweet.text,
                "favorite_count": tweet.public_metrics["like_count"],
                "retweet_count": tweet.public_metrics["retweet_count"],
                "created_at": tweet.created_at
            }
            tweet_list.append(refined_tweet)
    
    # Convert to DataFrame and save to CSV
    df = pd.DataFrame(tweet_list)
    csv_file = "refined_tweets.csv"
    df.to_csv(csv_file, index=False)
    
    # Upload CSV to S3
    s3 = boto3.client("s3", aws_access_key_id="YOUR_AWS_ACCESS_KEY", aws_secret_access_key="YOUR_AWS_SECRET_KEY")
    s3.upload_file(csv_file, "your-s3-bucket-name", "refined_tweets.csv")

# Run the function
run_twitter_etl()
