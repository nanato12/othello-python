class InvalidRangeError(Exception):
    """範囲外が指定された時のException"""


class AlreadyPutError(Exception):
    """既に石が置いてある時のException"""


class NoEffectPointError(Exception):
    """置いても変わる石がない時のException"""


class ImpossibleReverseError(Exception):
    """反転できない時のException"""
