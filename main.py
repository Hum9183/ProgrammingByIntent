# -*- coding: utf-8 -*-

# NOTE: 意図によるプログラミングの習作

# References:
# https://zenn.dev/dove/articles/2f0ec6786dba10
# https://zenn.dev/miya_tech/articles/4450f9b74f6852
# https://y-ahiru.hatenadiary.jp/entry/2021/12/19/000000

from tramp_early import tramp_straight, tramp_functions
from tramp_custom import tramp_straight_custom, tramp_functions_custom

from tramp_early.tramp import Tramp
from tramp_custom.tramp_custom import TrampCustom

if __name__ == '__main__':
    ### ベタ書きと関数化 ###

    # 初期型
    print(tramp_straight.draw())
    print(tramp_functions.draw())

    # 仕様変更
    print(tramp_straight_custom.draw(3, True))
    print(tramp_functions_custom.draw(3, True))

    # ======================

    ### 番外編(クラス) ###
    # 初期型
    tramp = Tramp()
    tramp.shuffle()
    print(tramp.draw())

    # 仕様変更
    tramp = TrampCustom()
    tramp.shuffle()
    print(tramp.draw(3, True))
