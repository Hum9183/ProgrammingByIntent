# -*- coding: utf-8 -*-

# ///////////////////
# // 関数化する場合 //
# ///////////////////

# 仕様変更:
# 引く枚数を指定出来るようにする
# 山札の下からも引けるようにする

import random


def draw(num_of_draws: int, from_the_top: bool) -> int:
    # NOTE: 仕様変更に伴う抽象度の変更はない
    trumps = __init()
    shuffled = __shuffle(trumps)
    drawn_tramps = __draw(shuffled, num_of_draws, from_the_top)
    return drawn_tramps


def __init() -> list[int]:
    """1~13のトランプを用意する"""
    return list(range(1, 14))


def __shuffle(tramps: list[int]) -> list[int]:
    """シャッフルする"""
    shuffled = random.sample(tramps, len(tramps))
    return shuffled


def __draw(tramps: list[int],
           num_of_draws: int,
           from_the_top: bool) -> list[int]:
    """トランプを引く"""
    if from_the_top:
        drawn_tramps = tramps[:num_of_draws]
    else:
        drawn_tramps = tramps[-num_of_draws:]
        drawn_tramps.reverse()

    return drawn_tramps
