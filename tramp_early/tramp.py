# -*- coding: utf-8 -*-

# /////////////////////
# // クラス化する場合 //
# /////////////////////

import random


class Tramp():
    def __init__(self):
        """1~13で初期化する"""
        self.__cards = list(range(1, 14))

    def shuffle(self):
        """シャッフルする"""
        self.__cards = random.sample(self.__cards, len(self.__cards))

    def draw(self) -> int:
        """最初の1枚を引く"""
        return self.__cards[0]
