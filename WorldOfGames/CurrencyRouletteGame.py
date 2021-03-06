from abc import ABC
import requests
import random


class CurrencyRouletteGame(ABC):

    def __init__(self, difficulty):
        self.difficulty = difficulty
        super().__init__()

    def play(self):
        total_usd = random.randint(1, 100)
        total_ils = total_usd * self.convert_usd_to_ils()
        interval_min, interval_max = self.get_money_interval(total_ils, self.difficulty)
        print(f"{total_ils} {interval_min} {interval_max}")
        usr_input = self.get_guess_from_user(total_usd)
        if interval_min <= usr_input <= interval_max:
            print("You Won!")
        else:
            print("You Lose!")

    @staticmethod
    def convert_usd_to_ils():
        url = 'https://free.currconv.com/api/v7/convert?q=USD_ILS&compact=ultra&apiKey=745a7a1c61a087e2ed35'
        res = r = requests.get(url)
        if res.status_code == 200:
            return res.json()['USD_ILS']
        return 0

    @staticmethod
    def get_money_interval(total_ils, difficulty):
        interval = (total_ils - (5 - difficulty), total_ils + (5 - difficulty))
        return interval

    @staticmethod
    def get_guess_from_user(total_in_usd):
        usr_input = int(input(f"try to convert {total_in_usd} USD to ILS"))
        return usr_input
