# -*- coding: utf-8 -*-

# //////////////////////////
# // 処理をベタ書きする場合 //
# //////////////////////////

# 仕様変更:
# 引く枚数を指定出来るようにする
# 山札の下からも引けるようにする

# Bad:
# 仕様変更によって抽象度がかなりバラバラになってしまった...

import random


def draw(num_of_draws: int, from_the_top: bool) -> int:
    # 1~13のトランプを用意する
    trumps = list(range(1, 14))

    # シャッフルする
    shuffled = random.sample(trumps, len(trumps))

    # 引く
    if from_the_top:
        drawn_tramps = shuffled[:num_of_draws]
    else:
        drawn_tramps = shuffled[-num_of_draws:]
        drawn_tramps.reverse()

    return drawn_tramps
