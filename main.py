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

def write_csv_user_id(user_id):
    today = datetime.today().timetuple()
    date = f"{today.tm_year}-{today.tm_mon}-{today.tm_mday}"
    with open("./followers.csv", mode="a", encoding="UTF-8") as f:
        writer = csv.DictWriter(f, ["Date", "user_id"])
        writer.writeheader()
        writer.writerow({"Date": f"{date}", "user_id": f"{user_id}"})

def main():
    username = "origin_seeker"

    client = create_client()
    user = client.get_user(username=username, user_fields="description,protected,location,name,username,public_metrics,profile_image_url,verified") 
    user_id = user.data.get("id")
    write_csv_user_id(user_id)

if __name__ == "__main__":
    main()
