import csv
from os import path
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
# CSVデータを保持する
csv_file_list = []
# 選択回答の入力(Yes)
answer_yes = ["yes", "y"]
# 選択回答の入力(No)
answer_no = ["no", "n"]


def get_recomend_restlan(restlan_list: list):
    sorted_list = sorted(restlan_list, key=lambda x: x["Count"])
    if len(sorted_list) > 0:
        return sorted_list
    return None


# 名前を取得
cprint("こんにちは！私はRobokoです。あなたの名前はなんですか？", "green")
while True:
    name = input()
    if name:
        break
    cprint("名前を入力してください。", "red")


# ファイルが存在しない場合はファイルを作成する
if not pathlib.Path(csv_file_path).exists():
    with open(csv_file_path, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

# CSVファイルが存在する場合はファイルを読み込んでデータを取得する
with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file, fieldnames=fieldnames)
    for index, row in enumerate(reader):
        if index == 0:
            continue
        csv_file_list.append(row)


# おすすめがあれば表示
recomend_restlan_dict = get_recomend_restlan(csv_file_list)
if recomend_restlan_dict:
    #    while True:
    #        answer = input()
    #        if answer.lower() in answer_yes or answer.lower() in answer_no:
    #            break
    #        else:
    #            cprint("Yes/Noで入力してください。", "red")
    for row in recomend_restlan_dict:
        print(f"おすすめのレストラン{row['Name']}があります。お好きですか？")
        answer = input()
        if answer.lower() in answer_yes:
            break
        elif answer.lower() in answer_no:
            continue
        else:
            cprint("Yes/Noで入力してください。", "red")


# レストラン名を取得
restlan_name = None
cprint(f"{name}さん。どこのレストランが好きですか？", "green")
while True:
    restlan_name = input().capitalize()
    if restlan_name:
        break
    cprint("レストラン名を入力してください。", "red")

# CSVファイルを更新
with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    # レストラン名がリストに既に存在する場合は+1
    for index, row in enumerate(csv_file_list):
        if restlan_name == row["Name"]:
            row.update({"Count": int(row["Count"]) + 1})
        writer.writerow(row)
    # レストラン名がリストに存在しない場合は新規作成
    if not any(restlan_name == row["Name"] for row in csv_file_list):
        writer.writerow({"Name": restlan_name.capitalize(), "Count": 1})


cprint(f"{name}さん。ありがとうございました。")
cprint("良い一日を！さようなら。")
