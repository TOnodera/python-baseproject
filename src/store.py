import pathlib
import csv
from typing import List
from user import User


class Store:
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path
        self.fieldnames = ["Name", "Count"]
        self.create_store()

    def create_store(self):
        """
        ファイルが存在しない場合はヘッダー行が書かれたCSVファイルを新規作成。
        """
        # ファイルが存在しない場合はファイルを作成する
        if not pathlib.Path(self.csv_file_path).exists():
            with open(self.csv_file_path, "w") as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
                writer.writeheader()

    def read_rows(self) -> List:
        """
        CSVファイルのデータ行を全て読み込んでリストを返す。
        """
        # CSVファイルが存在する場合はファイルを読み込んでデータを取得する
        csv_file_list = []
        with open(self.csv_file_path, "r") as csv_file:
            reader = csv.DictReader(csv_file, fieldnames=self.fieldnames)
            for index, row in enumerate(reader):
                if index == 0:
                    continue
                csv_file_list.append(row)
        return csv_file_list

    def increament(self, user: User):
        """
        レストラン名がCSVに存在する場合はCountを+1して保存。
        Params:
            restaurant_name: レストラン名

        """
        # CSVのデータをリストに読み込む
        rows = self.read_rows()
        if any(user.favorite_restaurant == row["Name"] for row in rows):
            self.update_row(user.favorite_restaurant)
        else:
            self.create_row(user.favorite_restaurant)

    def create_row(self, restaurant_name: str):
        with open(self.csv_file_path, "a") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
            writer.writerow({"Name": restaurant_name.capitalize(), "Count": 1})

    def update_row(self, restaurant_name: str):
        all_rows = []
        with open(self.csv_file_path, "r") as csv_file:
            reader = csv.DictReader(csv_file, fieldnames=self.fieldnames)
            for row in reader:
                all_rows.append(row)
        with open(self.csv_file_path, "w") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
            for row in all_rows:
                if restaurant_name.capitalize() == row["Name"]:
                    row.update({"Count": int(row["Count"]) + 1})
                writer.writerow(row)
