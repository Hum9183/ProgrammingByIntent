# -*- coding: utf-8 -*-

# //////////////////////////
# // 処理をベタ書きする場合 //
# //////////////////////////

# Good:
# ・短い処理の場合、簡潔でわかりやすい
# Bad:
# ・コメントが無いと意図が分かりづらい

import random


def draw() -> int:
    # 1~13のトランプを用意する
    trumps = list(range(1, 14))

    # シャッフルする
    shuffled = random.sample(trumps, len(trumps))

    # 最初の1枚を引く
    first_one = shuffled[0]
    return first_one
