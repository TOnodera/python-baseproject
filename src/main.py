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


# ファイルが存在しない場合はファイルを作成する
if not pathlib.Path.exists(csv_file_path):
    with open(csv_file_path, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

# CSVファイルが存在する場合はファイルを読み込んでデータを取得する
with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file, fieldnames=fieldnames)


cprint(f"{name}さん。ありがとうございました。")
cprint("良い一日を！さようなら。")
