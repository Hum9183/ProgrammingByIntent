# -*- coding: utf-8 -*-

# /////////////////////
# // クラス化する場合 //
# /////////////////////

# 仕様変更:
# 引く枚数を指定出来るようにする
# 山札の下からも引けるようにする

import random


class TrampCustom():
    def __init__(self):
        """1~13で初期化する"""
        self.__cards = list(range(1, 14))

    def shuffle(self):
        """シャッフルする"""
        self.__cards = random.sample(self.__cards, len(self.__cards))

    def draw(self, num_of_draws: int, from_the_top: bool) -> list[int]:
        """トランプを引く"""
        cards = self.__cards

        if from_the_top:
            drawn_cards = cards[:num_of_draws]
        else:
            drawn_cards = cards[-num_of_draws:]
            drawn_cards.reverse()

        return drawn_cards
