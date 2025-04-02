import tweepy
import pandas as pd
from datetime import datetime
import time

def run_twitter_etl():
    # Twitter API v2 Bearer Token
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAJ9k0QEAAAAAQoJkp20yMjhL6EE3KexwiKQTYss%3DBBPWjS9JIZ0eY3itrrNQtxUj5n8wQT3zb6YU1khS4ZqIYGixwb"  
    
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
    df.to_csv("refined_tweets.csv", index=False)
    
    print("✅ Tweets fetched successfully!")

# Run the function
run_twitter_etl()
