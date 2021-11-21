from typing import List
from termcolor import cprint
from user import User
from store import Store


class Robot:
    csv_file_path = "/home/python/app/src/store/data.csv"

    def __init__(self):
        self.user = User()
        self.store = Store(csv_file_path=self.csv_file_path)

    def ask_name(self):
        # 名前を取得
        cprint("こんにちは！私はRobokoです。あなたの名前はなんですか？", "green")
        while True:
            name = input()
            if name:
                self.user.name = name
                break
            cprint("名前を入力してください。", "red")

    def ask_restlan(self):
        # レストラン名を取得
        restlan_name = None
        cprint(f"{self.user.name}さん。どこのレストランが好きですか？", "green")
        while True:
            restlan_name = input().capitalize()
            if restlan_name:
                self.user.favorite_restlan = restlan_name
                self.store.increament(self.user)
                break
            cprint("レストラン名を入力してください。", "red")

    def get_recomend_restlan(self) -> List:
        restlan_list = self.store.read_rows()
        sorted_list = sorted(restlan_list, key=lambda x: x["Count"])
        if len(sorted_list) > 0:
            return sorted_list
        return []
