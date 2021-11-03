from copy import deepcopy
from pprint import pprint
from typing import Generator, List

from othello.errors import AlreadyPutError, NoEffectPointError
from othello.models import COLOR, Stone


class Borad:
    __stones = [[Stone(x, y) for x in range(8)] for y in range(8)]

    def __init__(self) -> None:
        init_points = [(3, 3), (3, 4), (4, 4), (4, 3)]
        for point, color in zip(init_points, self.order()):
            x, y = point
            self.__stones[x][y] = Stone(x, y, color)

    def show(self) -> None:
        """現在の盤を表示する関数"""
        stone_lists: List[List] = [list(range(9)), *deepcopy(self.__stones)]
        for i, stone_list in enumerate(stone_lists[1:], start=1):
            stone_list.insert(0, i)
        pprint(stone_lists, compact=True, width=40)

    def get_effect_stones(self, stone: Stone) -> List[Stone]:
        """影響する石を取得する関数"""
        if self.__stones[stone.x][stone.y].color != COLOR.NONE:
            raise AlreadyPutError("おっと、そこにはもう石が置いてあるよ")

        effect_stones = []
        for points in stone.effect_points:
            # 影響範囲の石
            stones = [self.__stones[point[0]][point[1]] for point in points]
            # 影響範囲の石の中に同色がなければ continue
            if stone.color not in [_stone.color for _stone in stones]:
                continue

            for _stone in stones:
                # 石がないか、同色なら影響範囲終了
                if _stone.color in (COLOR.NONE, stone.color):
                    break
                # 影響する石を追加
                effect_stones.append(_stone)
        return effect_stones

    def put_stone(self, stone: Stone) -> None:
        """石を置いて影響する石を反転させる"""
        effect_stones = self.get_effect_stones(stone)
        if not effect_stones:
            raise NoEffectPointError("そこに置いてもどの石も変わらないよ")

        # 石を置く
        self.__stones[stone.x][stone.y] = stone
        # 影響する石を反転
        for _stone in effect_stones:
            _stone.reverse()

    @staticmethod
    def order() -> Generator[COLOR, None, None]:
        while True:
            yield COLOR.BLACK
            yield COLOR.WHITE
