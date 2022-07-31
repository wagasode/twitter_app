import tweepy
import json

#----------
#指定された検索単語を含むツイートを検索する。
#検索範囲は直近1週間。
#----------

# twitter_api_clientを作成する
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

# 与えられた検索単語を含むツイートを検索
# 検索上限数を指定
def search_tweets(client, words, tweet_max):
    tweet_list = client.search_recent_tweets(query=words, max_results=tweet_max)
    return tweet_list
