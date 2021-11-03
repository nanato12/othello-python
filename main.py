from othello import Borad
from othello.errors import (
    AlreadyPutError,
    ImpossibleReverseError,
    InvalidRangeError,
    NoEffectPointError,
)
from othello.models import Stone

board = Borad()
for color in board.order():
    board.show()
    while True:
        try:
            y, x = input(
                f"[{color.icon}] {color.name} input (x,y) >>> "
            ).split(",")
            board.put_stone(Stone(int(x) - 1, int(y) - 1, color))
            break
        except ValueError:
            print("カンマ区切りの数字で入力してくれないかね？ 入力例はこんな感じ -> 1,1")
        except (
            InvalidRangeError,
            AlreadyPutError,
            NoEffectPointError,
            ImpossibleReverseError,
        ) as e:
            print(e)
        except Exception:
            raise
