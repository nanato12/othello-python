from dataclasses import dataclass
from enum import IntEnum, auto
from typing import List, Tuple

from othello.errors import ImpossibleReverseError, InvalidRangeError


class COLOR(IntEnum):
    NONE = 0
    WHITE = auto()
    BLACK = auto()

    @property
    def icon(self) -> str:
        return [" ", "○", "●"][self.value]


@dataclass
class Stone:
    x: int
    y: int
    color: COLOR = COLOR.NONE

    def __post_init__(self) -> None:
        if not (0 <= self.x < 8 and 0 <= self.y < 8):
            raise InvalidRangeError("その範囲には置けねえんだよなぁ")

    def reverse(self) -> None:
        if self.color == COLOR.NONE:
            raise ImpossibleReverseError("石がないのに反転できないぜ")
        self.color = COLOR.BLACK if self.color == COLOR.WHITE else COLOR.BLACK

    @property
    def effect_points(self) -> List[List[Tuple[int, int]]]:
        """該当する石から見た影響する全範囲"""
        # 上
        up_points = [(self.x, y) for y in range(8) if y < self.y]
        up_points.reverse()
        # 下
        down_points = [(self.x, y) for y in range(8) if y > self.y]
        # 左
        left_points = [(x, self.y) for x in range(8) if x < self.x]
        left_points.reverse()
        # 右
        right_points = [(x, self.y) for x in range(8) if x > self.x]
        # 左上
        left_up_points = [
            (x, y)
            for x, y in zip(
                reversed(range(0, self.x)), reversed(range(0, self.y))
            )
        ]
        # 右下
        left_down_points = [
            (x, y) for x, y in zip(range(self.x + 1, 8), range(self.y + 1, 8))
        ]
        # 右上
        right_up_points = [
            (x, y)
            for x, y in zip(range(self.x + 1, 8), reversed(range(0, self.y)))
        ]
        # 左下
        right_down_points = [
            (x, y)
            for x, y in zip(reversed(range(0, self.x)), range(self.y + 1, 8))
        ]
        return [
            up_points,
            down_points,
            right_points,
            left_points,
            left_up_points,
            left_down_points,
            right_up_points,
            right_down_points,
        ]

    def __str__(self) -> str:
        return self.color.icon

    __repr__ = __str__
