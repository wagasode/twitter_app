import json
import tweepy
from datetime import datetime
import csv

def create_client():
    with open("./secret_twitter_keys.json", encoding="UTF-8") as f:
        twitter_keys = json.load(f)

    api_key = twitter_keys["API_Key"]
    api_key_secret = twitter_keys["API_Key_Secret"]
    access_token = twitter_keys["Access_Token"]
    access_token_secret = twitter_keys["Access_Token_Secret"]
    baerer_token = twitter_keys["Baerer_Token"]
    client = tweepy.Client(baerer_token, consumer_key=api_key, consumer_secret=api_key_secret, access_token=access_token, access_token_secret=access_token_secret, wait_on_rate_limit=True)

    return client 

def search_tweets(client, words, tweet_max):
    tweet_list = client.search_recent_tweets(query=words, max_results=tweet_max)
    return tweet_list

def write_csv_user_id(user_id):
    dt_now = datetime.now()
    date = f"{dt_now}"
    with open("./user_id.csv", mode="a", encoding="UTF-8") as f:
        writer = csv.DictWriter(f, ["Date", "user_id"])
        writer.writeheader()
        writer.writerow({"Date": f"{dt_now}", "user_id": f"{user_id}"})

def write_csv_search_tweets(tweets):
    dt_now = datetime.now()
    date = f"{dt_now}"
    with open("./search_tweets.csv", mode="a", encoding="UTF-8") as f:
        writer = csv.DictWriter(f, ["Date", "tweets"])
        writer.writeheader()
        writer.writerow({"Date": f"{dt_now}", "tweets": f"{tweets}"})


def main():
    username = "origin_seeker"
    search_word_list = ["シャドバ", "連勝"]
    search_tweet_max = 10

    client = create_client()
    user = client.get_user(username=username, user_fields="description,protected,location,name,username,public_metrics,profile_image_url,verified") 
    user_id = user.data.get("id")
    write_csv_user_id(user_id)
    
    tweets = search_tweets(client, search_word_list, search_tweet_max)
    write_csv_search_tweets(tweets)

if __name__ == "__main__":
    main()
