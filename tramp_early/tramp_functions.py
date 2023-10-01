# -*- coding: utf-8 -*-

# ///////////////////
# // 関数化する場合 //
# ///////////////////

# 「どのようにやるのか」ではなく「何をやるのか」
# Good:
# ・関数名に「何をやるのか」が書いてあるため意図を把握しやすい

import random


def draw() -> int:
    trumps = __init()
    shuffled = __shuffle(trumps)
    first_one = __draw_first_one(shuffled)
    return first_one


def __init() -> list[int]:
    """1~13のトランプを用意する"""
    return list(range(1, 14))


def __shuffle(tramps: list[int]) -> list[int]:
    """シャッフルする"""
    shuffled = random.sample(tramps, len(tramps))
    return shuffled


def __draw_first_one(tramps: list[int]) -> int:
    """最初の1枚を引く"""
    first_one = tramps[0]
    return first_one
