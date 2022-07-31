from datetime import datetime
import csv
from get_searched_tweets import *
import PySimpleGUI as sg

def write_csv_search_tweets(tweets):
    dt_now = datetime.now()
    date = f"{dt_now}"
    with open("./search_tweets.csv", mode="w", encoding="Shift-JIS", newline="\n") as f:
        writer = csv.DictWriter(f, ["Date", "tweet_No", "id", "tweet"])
        writer.writeheader()
        for index, tweet in enumerate(tweets[0]):
            writer.writerow({"Date": dt_now, "tweet_No": index, "id": tweet["id"], "tweet": tweet["text"]})

def create_msg(tweets):
    msg = ""
    for tweet in tweets[0]:
        msg += f"{tweet}\n"
    return msg

def execute(client, values, window):
    value1 = values["input1"]
    value2 = values["input2"]
    value3 = values["input3"]
    tweets = search_tweets(client, [value1, value2], value3)
    msg = create_msg(tweets)
    window["text1"].update(msg)

def main():
    title = "2つの検索単語を入力すると、それを含むツイートを指定数表示するアプリ"
    label1, value1 = "検索単語1", "シャドバ"
    label2, value2 = "検索単語2", "連勝"
    label3, value3 = "表示ツイート数", "10"

    layout = [[sg.Text(label1, size=(14,1)), sg.Input(value1, key="input1")],
              [sg.Text(label2, size=(14,1)), sg.Input(value2, key="input2")],
              [sg.Text(label3, size=(14,1)), sg.Input(value3, key="input3")],
              [sg.Button("実行", size=(20,1), pad=(5,15), bind_return_key=True)],
              [sg.Multiline(key="text1", size=(120,40))]]

    client = create_client()
    
    window = sg.Window(title, layout, font=(None, 14))
    while True:
        event, values = window.read()
        if event == None:
            break
        if event == "実行":
            execute(client, values, window)
    window.close()
    write_csv_search_tweets(tweets)

if __name__ == "__main__":
    main()
