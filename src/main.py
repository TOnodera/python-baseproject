import csv
from os import path, read, write
import pathlib
from termcolor import cprint

from modules import utils

# データ保管場所
csv_file_path = "/home/python/app/src/store/data.csv"
# CSVフィールド名
fieldnames = ["Name", "Count"]
# 一番人気のあるお店の名前
most_popular_restlan = None
# 一番人気のあるお店のカウント
most_popular_restlan_count = 0

# 名前を取得
cprint("こんにちは！私はRobokoです。あなたの名前はなんですか？", "green")
while True:
    name = input()
    if name:
        break
    cprint("名前を入力してください。", "red")

# レストラン名を取得
cprint(f"{name}さん。どこのレストランが好きですか？", "green")
while True:
    restlan_name = input()
    if restlan_name:
        break
    cprint("レストラン名を入力してください。", "red")


# ファイルが存在する場合は読み込む

# CSVファイルが存在する場合はファイルを読み込んでデータを取得する
if pathlib.Path.exists(csv_file_path):
    with open(csv_file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file, fieldnames=fieldnames)
        for row in reader:
            if count := int(row.get("Count")) > most_popular_restlan_count:
                most_popular_restlan = row.get("Name")
                most_popular_restlan_count = count

# CSVファイルへの書き込み
with open(csv_file_path, "a+") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    # 空の場合はヘッダー追加
    if utils.fils_is_empty(csv_file_path):
        writer.writeheader()
    writer.writerow({"Name"})

cprint(f"{name}さん。ありがとうございました。")
cprint("良い一日を！さようなら。")
