from typing import List, Sequence, Dict

from .typedef import ELEM, LIST_PY, NUM, NUM_LIST_RS, LIST_RS


class BooleanList:
    # Arrange the following methods in alphabetical order.

    def __init__(self, vec: Sequence[bool]) -> None: ...
    def all(self) -> bool: ...
    def and_(self, other: BooleanList) -> BooleanList: ...
    def any(self) -> bool: ...
    def append(self, elem: ELEM): ...
    def as_float(self) -> FloatList: ...
    def as_int(self) -> IntegerList: ...
    def as_str(self) -> StringList: ...
    def copy(self) -> BooleanList: ...
    def counter(self) -> Dict[bool, int]: ...
    @staticmethod
    def cycle(obj: Sequence[bool], size: int) -> BooleanList: ...
    def equal_scala(self, elem: ELEM) -> BooleanList: ...
    def filter(self, condition: BooleanList) -> BooleanList: ...
    def get(self, index: int) -> bool: ...
    def not_(self) -> BooleanList: ...
    def not_equal_scala(self, elem: ELEM) -> BooleanList: ...
    def or_(self, other: BooleanList) -> BooleanList: ...
    def pop(self): ...
    @staticmethod
    def repeat(elem: bool, size: int) -> BooleanList: ...
    def replace(self, old: ELEM, new: ELEM) -> BooleanList: ...
    def set(self, index: int, elem: ELEM): ...
    def size(self) -> int: ...
    def sort(self, ascending: bool) -> BooleanList: ...
    def sum(self) -> int: ...
    def to_list(self) -> List[bool]: ...
    def union_all(self, other: LIST_RS) -> LIST_RS: ...
    def unique(self) -> BooleanList: ...


class FloatList:
    #  Arrange the following methods in alphabetical order.

    def __init__(self, vec: Sequence[float]) -> None: ...
    def add(self, other: NUM_LIST_RS) -> FloatList: ...
    def add_scala(self, elem: NUM) -> FloatList: ...
    def append(self, elem: ELEM) -> None: ...
    def argmax(self) -> int: ...
    def argmin(self) -> int: ...
    def as_bool(self) -> BooleanList: ...
    def as_int(self) -> IntegerList: ...
    def as_str(self) -> StringList: ...
    def copy(self) -> FloatList: ...
    @staticmethod
    def cycle(obj: Sequence[float], size: int) -> FloatList: ...
    def div(self, other: NUM_LIST_RS) -> FloatList: ...
    def div_scala(self, elem: float) -> FloatList: ...
    def equal_scala(self, elem: NUM) -> BooleanList: ...
    def filter(self, condition: BooleanList) -> FloatList: ...
    def get(self, index: int) -> float: ...
    def greater_than_or_equal_scala(self, elem: NUM) -> BooleanList: ...
    def greater_than_scala(self, elem: NUM) -> BooleanList: ...
    def less_than_or_equal_scala(self, elem: NUM) -> BooleanList: ...
    def less_than_scala(self, elem: NUM) -> BooleanList: ...
    def max(self) -> float: ...
    def min(self) -> float: ...
    def mul(self, other: NUM_LIST_RS) -> FloatList: ...
    def mul_scala(self, elem: NUM) -> FloatList: ...
    def not_equal_scala(self, elem: NUM) -> BooleanList: ...
    def pop(self) -> None: ...
    def pow_scala(self, elem: int) -> FloatList: ...
    @staticmethod
    def repeat(elem: float, size: int) -> FloatList: ...
    def replace(self, old: ELEM, new: ELEM) -> FloatList: ...
    def set(self, index: int, elem: ELEM) -> None: ...
    def size(self) -> int: ...
    def sort(self, ascending: bool) -> FloatList: ...
    def sub(self, other: NUM_LIST_RS) -> FloatList: ...
    def sub_scala(self, elem: NUM) -> FloatList: ...
    def sum(self) -> float: ...
    def to_list(self) -> List[float]: ...
    def union_all(self, other: LIST_RS) -> LIST_RS: ...
    def unique(self) -> FloatList: ...


class IntegerList:
    #  Arrange the following methods in alphabetical order.

    def __init__(self, vec: Sequence[int]) -> None: ...
    def add(self, other: NUM_LIST_RS) -> IntegerList: ...
    def add_scala(self, elem: NUM) -> IntegerList: ...
    def append(self, elem: ELEM) -> None: ...
    def argmax(self) -> int: ...
    def argmin(self) -> int: ...
    def as_bool(self) -> BooleanList: ...
    def as_float(self) -> FloatList: ...
    def as_str(self) -> StringList: ...
    def copy(self) -> IntegerList: ...
    def counter(self) -> Dict[int, int]: ...
    @staticmethod
    def cycle(obj: Sequence[int], size: int) -> IntegerList: ...
    def div(self, other: NUM_LIST_RS) -> FloatList: ...
    def div_scala(self, elem: float) -> FloatList: ...
    def equal_scala(self, elem: NUM) -> BooleanList: ...
    def filter(self, condition: BooleanList) -> IntegerList: ...
    def get(self, index: int) -> int: ...
    def greater_than_or_equal_scala(self, elem: NUM) -> BooleanList: ...
    def greater_than_scala(self, elem: NUM) -> BooleanList: ...
    def less_than_or_equal_scala(self, elem: NUM) -> BooleanList: ...
    def less_than_scala(self, elem: NUM) -> BooleanList: ...
    def max(self) -> int: ...
    def min(self) -> int: ...
    def mul(self, other: NUM_LIST_RS) -> IntegerList: ...
    def mul_scala(self, elem: NUM) -> IntegerList: ...
    def not_equal_scala(self, elem: NUM) -> BooleanList: ...
    def pop(self) -> None: ...
    def pow_scala(self, elem: int) -> IntegerList: ...
    def set(self, index: int, elem: ELEM) -> None: ...
    @staticmethod
    def repeat(elem: int, size: int) -> IntegerList: ...
    def replace(self, old: ELEM, new: ELEM) -> IntegerList: ...
    def size(self) -> int: ...
    def sort(self, ascending: bool) -> IntegerList: ...
    def sub(self, other: NUM_LIST_RS) -> IntegerList: ...
    def sub_scala(self, elem: NUM) -> IntegerList: ...
    def sum(self) -> int: ...
    def to_list(self) -> List[int]: ...
    def union_all(self, other: LIST_RS) -> LIST_RS: ...
    def unique(self) -> IntegerList: ...


class StringList:
    # Arrange the following methods in alphabetical order.

    def __init__(self, vec: Sequence[str]) -> None: ...
    def append(self, elem: ELEM): ...
    def as_bool(self) -> BooleanList: ...
    def as_float(self) -> FloatList: ...
    def as_int(self) -> IntegerList: ...
    def contains(self, elem: str) -> BooleanList: ...
    def copy(self) -> StringList: ...
    def counter(self) -> Dict[str, int]: ...
    @staticmethod
    def cycle(obj: Sequence[str], size: int) -> StringList: ...
    def equal_scala(self, elem: ELEM) -> BooleanList: ...
    def filter(self, condition: BooleanList) -> StringList: ...
    def get(self, index: int) -> str: ...
    def not_equal_scala(self, elem: ELEM) -> BooleanList: ...
    def pop(self): ...
    @staticmethod
    def repeat(elem: str, size: int) -> StringList: ...
    def replace(self, old: ELEM, new: ELEM) -> StringList: ...
    def set(self, index: int, elem: ELEM): ...
    def size(self) -> int: ...
    def sort(self, ascending: bool) -> StringList: ...
    def to_list(self) -> List[str]: ...
    def union_all(self, other: LIST_RS) -> LIST_RS: ...
    def unique(self) -> StringList: ...


def arange(start: int, stop: int, step: int) -> IntegerList: ...


def select_bool(
    conditions: List[BooleanList],
    choices: LIST_PY,
    default: bool,
) -> BooleanList: ...


def select_float(
    conditions: List[BooleanList],
    choices: LIST_PY,
    default: float,
) -> FloatList: ...


def select_int(
    conditions: List[BooleanList],
    choices: LIST_PY,
    default: int,
) -> IntegerList: ...


def select_string(
    conditions: List[BooleanList],
    choices: LIST_PY,
    default: str,
) -> IntegerList: ...
