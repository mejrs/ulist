from lib2to3.pgen2.token import OP
from typing import List, Sequence, Dict, Set, Optional

from .typedef import ELEM, LIST_PY, NUM, NUM_LIST_RS, LIST_RS, ELEM_OPT


class BooleanList:
    # Arrange the following methods in alphabetical order.

    def __init__(self, vec: Sequence[bool], hset: Set[int]) -> None: ...
    def all(self) -> bool: ...
    def and_(self, other: BooleanList) -> BooleanList: ...
    def any(self) -> bool: ...
    def append(self, elem: ELEM_OPT) -> None: ...
    def as_float32(self) -> FloatList32: ...
    def as_float64(self) -> FloatList64: ...
    def as_int32(self) -> IntegerList32: ...
    def as_int64(self) -> IntegerList64: ...
    def as_str(self) -> StringList: ...
    def copy(self) -> BooleanList: ...
    def counter(self) -> Dict[bool, int]: ...
    @staticmethod
    def cycle(obj: Sequence[bool], size: int) -> BooleanList: ...
    def equal_scala(self, elem: ELEM) -> BooleanList: ...
    def filter(self, condition: BooleanList) -> BooleanList: ...
    def get(self, index: int) -> Optional[bool]: ...
    def get_by_indexes(self, indexes: IndexList) -> BooleanList: ...
    def not_(self) -> BooleanList: ...
    def not_equal_scala(self, elem: ELEM) -> BooleanList: ...
    def or_(self, other: BooleanList) -> BooleanList: ...
    def pop(self): ...
    @staticmethod
    def repeat(elem: Optional[bool], size: int) -> BooleanList: ...
    def replace(self, old: ELEM_OPT, new: ELEM_OPT) -> BooleanList: ...
    def set(self, index: int, elem: ELEM_OPT) -> None: ...
    def size(self) -> int: ...
    def sort(self, ascending: bool) -> None: ...
    def sum(self) -> int: ...
    def to_index(self) -> IndexList: ...
    def to_list(self) -> List[Optional[bool]]: ...
    def union_all(self, other: LIST_RS) -> LIST_RS: ...
    def unique(self) -> BooleanList: ...


class FloatList32:
    #  Arrange the following methods in alphabetical order.

    def __init__(self, vec: Sequence[float], hset: Set[int]) -> None: ...
    def add(self, other: NUM_LIST_RS) -> FloatList32: ...
    def add_scala(self, elem: NUM) -> FloatList32: ...
    def append(self, elem: ELEM_OPT) -> None: ...
    def argmax(self) -> int: ...
    def argmin(self) -> int: ...
    def as_bool(self) -> BooleanList: ...
    def as_float64(self) -> FloatList64: ...
    def as_int32(self) -> IntegerList32: ...
    def as_int64(self) -> IntegerList64: ...
    def as_str(self) -> StringList: ...
    def copy(self) -> FloatList32: ...
    @staticmethod
    def cycle(obj: Sequence[float], size: int) -> FloatList32: ...
    def div(self, other: NUM_LIST_RS) -> FloatList32: ...
    def div_scala(self, elem: float) -> FloatList32: ...
    def equal_scala(self, elem: NUM) -> BooleanList: ...
    def filter(self, condition: BooleanList) -> FloatList32: ...
    def get(self, index: int) -> Optional[float]: ...
    def get_by_indexes(self, indexes: IndexList) -> FloatList32: ...
    def greater_than_or_equal_scala(self, elem: NUM) -> BooleanList: ...
    def greater_than_scala(self, elem: NUM) -> BooleanList: ...
    def less_than_or_equal_scala(self, elem: NUM) -> BooleanList: ...
    def less_than_scala(self, elem: NUM) -> BooleanList: ...
    def max(self) -> float: ...
    def min(self) -> float: ...
    def mul(self, other: NUM_LIST_RS) -> FloatList32: ...
    def mul_scala(self, elem: NUM) -> FloatList32: ...
    def not_equal_scala(self, elem: NUM) -> BooleanList: ...
    def pop(self) -> None: ...
    def pow_scala(self, elem: int) -> FloatList32: ...
    @staticmethod
    def repeat(elem: Optional[float], size: int) -> FloatList32: ...
    def replace(self, old: ELEM_OPT, new: ELEM_OPT) -> FloatList32: ...
    def set(self, index: int, elem: ELEM_OPT) -> None: ...
    def size(self) -> int: ...
    def sort(self, ascending: bool) -> None: ...
    def sub(self, other: NUM_LIST_RS) -> FloatList32: ...
    def sub_scala(self, elem: NUM) -> FloatList32: ...
    def sum(self) -> float: ...
    def to_list(self) -> List[Optional[float]]: ...
    def union_all(self, other: LIST_RS) -> LIST_RS: ...
    def unique(self) -> FloatList32: ...


class FloatList64:
    #  Arrange the following methods in alphabetical order.

    def __init__(self, vec: Sequence[float], hset: Set[int]) -> None: ...
    def add(self, other: NUM_LIST_RS) -> FloatList64: ...
    def add_scala(self, elem: NUM) -> FloatList64: ...
    def append(self, elem: ELEM_OPT) -> None: ...
    def argmax(self) -> int: ...
    def argmin(self) -> int: ...
    def as_bool(self) -> BooleanList: ...
    def as_float32(self) -> FloatList32: ...
    def as_int32(self) -> IntegerList32: ...
    def as_int64(self) -> IntegerList64: ...
    def as_str(self) -> StringList: ...
    def copy(self) -> FloatList64: ...
    @staticmethod
    def cycle(obj: Sequence[float], size: int) -> FloatList64: ...
    def div(self, other: NUM_LIST_RS) -> FloatList64: ...
    def div_scala(self, elem: float) -> FloatList64: ...
    def equal_scala(self, elem: NUM) -> BooleanList: ...
    def filter(self, condition: BooleanList) -> FloatList64: ...
    def get(self, index: int) -> Optional[float]: ...
    def get_by_indexes(self, indexes: IndexList) -> FloatList64: ...
    def greater_than_or_equal_scala(self, elem: NUM) -> BooleanList: ...
    def greater_than_scala(self, elem: NUM) -> BooleanList: ...
    def less_than_or_equal_scala(self, elem: NUM) -> BooleanList: ...
    def less_than_scala(self, elem: NUM) -> BooleanList: ...
    def max(self) -> float: ...
    def min(self) -> float: ...
    def mul(self, other: NUM_LIST_RS) -> FloatList64: ...
    def mul_scala(self, elem: NUM) -> FloatList64: ...
    def not_equal_scala(self, elem: NUM) -> BooleanList: ...
    def pop(self) -> None: ...
    def pow_scala(self, elem: int) -> FloatList64: ...
    @staticmethod
    def repeat(elem: Optional[float], size: int) -> FloatList64: ...
    def replace(self, old: ELEM_OPT, new: ELEM_OPT) -> FloatList64: ...
    def set(self, index: int, elem: ELEM_OPT) -> None: ...
    def size(self) -> int: ...
    def sort(self, ascending: bool) -> None: ...
    def sub(self, other: NUM_LIST_RS) -> FloatList64: ...
    def sub_scala(self, elem: NUM) -> FloatList64: ...
    def sum(self) -> float: ...
    def to_list(self) -> List[Optional[float]]: ...
    def union_all(self, other: LIST_RS) -> LIST_RS: ...
    def unique(self) -> FloatList64: ...


class IntegerList32:
    #  Arrange the following methods in alphabetical order.

    def __init__(self, vec: Sequence[int], hset: Set[int]) -> None: ...
    def add(self, other: NUM_LIST_RS) -> IntegerList32: ...
    def add_scala(self, elem: NUM) -> IntegerList32: ...
    def append(self, elem: ELEM_OPT) -> None: ...
    def argmax(self) -> int: ...
    def argmin(self) -> int: ...
    def as_bool(self) -> BooleanList: ...
    def as_float32(self) -> FloatList32: ...
    def as_float64(self) -> FloatList64: ...
    def as_int64(self) -> IntegerList64: ...
    def as_str(self) -> StringList: ...
    def copy(self) -> IntegerList32: ...
    def counter(self) -> Dict[int, int]: ...
    @staticmethod
    def cycle(obj: Sequence[int], size: int) -> IntegerList32: ...
    def div(self, other: NUM_LIST_RS) -> FloatList32: ...
    def div_scala(self, elem: float) -> FloatList32: ...
    def equal_scala(self, elem: NUM) -> BooleanList: ...
    def filter(self, condition: BooleanList) -> IntegerList32: ...
    def get(self, index: int) -> Optional[int]: ...
    def get_by_indexes(self, indexes: IndexList) -> IntegerList32: ...
    def greater_than_or_equal_scala(self, elem: NUM) -> BooleanList: ...
    def greater_than_scala(self, elem: NUM) -> BooleanList: ...
    def less_than_or_equal_scala(self, elem: NUM) -> BooleanList: ...
    def less_than_scala(self, elem: NUM) -> BooleanList: ...
    def max(self) -> int: ...
    def min(self) -> int: ...
    def mul(self, other: NUM_LIST_RS) -> IntegerList32: ...
    def mul_scala(self, elem: NUM) -> IntegerList32: ...
    def not_equal_scala(self, elem: NUM) -> BooleanList: ...
    def pop(self) -> None: ...
    def pow_scala(self, elem: int) -> IntegerList32: ...
    def set(self, index: int, elem: ELEM_OPT) -> None: ...
    @staticmethod
    def repeat(elem: Optional[int], size: int) -> IntegerList32: ...
    def replace(self, old: ELEM_OPT, new: ELEM_OPT) -> IntegerList32: ...
    def size(self) -> int: ...
    def sort(self, ascending: bool) -> None: ...
    def sub(self, other: NUM_LIST_RS) -> IntegerList32: ...
    def sub_scala(self, elem: NUM) -> IntegerList32: ...
    def sum(self) -> int: ...
    def to_list(self) -> List[Optional[int]]: ...
    def union_all(self, other: LIST_RS) -> LIST_RS: ...
    def unique(self) -> IntegerList32: ...


class IntegerList64:
    #  Arrange the following methods in alphabetical order.

    def __init__(self, vec: Sequence[int], hset: Set[int]) -> None: ...
    def add(self, other: NUM_LIST_RS) -> IntegerList64: ...
    def add_scala(self, elem: NUM) -> IntegerList64: ...
    def append(self, elem: ELEM_OPT) -> None: ...
    def argmax(self) -> int: ...
    def argmin(self) -> int: ...
    def as_bool(self) -> BooleanList: ...
    def as_float32(self) -> FloatList32: ...
    def as_float64(self) -> FloatList64: ...
    def as_int32(self) -> IntegerList32: ...
    def as_str(self) -> StringList: ...
    def copy(self) -> IntegerList64: ...
    def counter(self) -> Dict[int, int]: ...
    @staticmethod
    def cycle(obj: Sequence[int], size: int) -> IntegerList64: ...
    def div(self, other: NUM_LIST_RS) -> FloatList64: ...
    def div_scala(self, elem: float) -> FloatList64: ...
    def equal_scala(self, elem: NUM) -> BooleanList: ...
    def filter(self, condition: BooleanList) -> IntegerList64: ...
    def get(self, index: int) -> Optional[int]: ...
    def get_by_indexes(self, indexes: IndexList) -> IntegerList64: ...
    def greater_than_or_equal_scala(self, elem: NUM) -> BooleanList: ...
    def greater_than_scala(self, elem: NUM) -> BooleanList: ...
    def less_than_or_equal_scala(self, elem: NUM) -> BooleanList: ...
    def less_than_scala(self, elem: NUM) -> BooleanList: ...
    def max(self) -> int: ...
    def min(self) -> int: ...
    def mul(self, other: NUM_LIST_RS) -> IntegerList64: ...
    def mul_scala(self, elem: NUM) -> IntegerList64: ...
    def not_equal_scala(self, elem: NUM) -> BooleanList: ...
    def pop(self) -> None: ...
    def pow_scala(self, elem: int) -> IntegerList64: ...
    def set(self, index: int, elem: ELEM_OPT) -> None: ...
    @staticmethod
    def repeat(elem: Optional[int], size: int) -> IntegerList64: ...
    def replace(self, old: ELEM_OPT, new: ELEM_OPT) -> IntegerList64: ...
    def size(self) -> int: ...
    def sort(self, ascending: bool) -> None: ...
    def sub(self, other: NUM_LIST_RS) -> IntegerList64: ...
    def sub_scala(self, elem: NUM) -> IntegerList64: ...
    def sum(self) -> int: ...
    def to_list(self) -> List[Optional[int]]: ...
    def union_all(self, other: LIST_RS) -> LIST_RS: ...
    def unique(self) -> IntegerList64: ...


class StringList:
    # Arrange the following methods in alphabetical order.

    def __init__(self, vec: Sequence[str], hset: Set[int]) -> None: ...
    def append(self, elem: ELEM_OPT) -> None: ...
    def as_bool(self) -> BooleanList: ...
    def as_float32(self) -> FloatList32: ...
    def as_float64(self) -> FloatList64: ...
    def as_int32(self) -> IntegerList32: ...
    def as_int64(self) -> IntegerList64: ...
    def contains(self, elem: str) -> BooleanList: ...
    def copy(self) -> StringList: ...
    def counter(self) -> Dict[str, int]: ...
    @staticmethod
    def cycle(obj: Sequence[str], size: int) -> StringList: ...
    def ends_with(self, elem: str) -> BooleanList: ...
    def equal_scala(self, elem: ELEM) -> BooleanList: ...
    def filter(self, condition: BooleanList) -> StringList: ...
    def get(self, index: int) -> Optional[str]: ...
    def get_by_indexes(self, indexes: IndexList) -> StringList: ...
    def not_equal_scala(self, elem: ELEM) -> BooleanList: ...
    def pop(self): ...
    @staticmethod
    def repeat(elem: Optional[str], size: int) -> StringList: ...
    def replace(self, old: ELEM_OPT, new: ELEM_OPT) -> StringList: ...
    def set(self, index: int, elem: ELEM_OPT) -> None: ...
    def size(self) -> int: ...
    def sort(self, ascending: bool) -> None: ...
    def starts_with(self, elem: str) -> BooleanList: ...
    def str_len(self) -> IntegerList64: ...
    def to_list(self) -> List[Optional[str]]: ...
    def union_all(self, other: LIST_RS) -> LIST_RS: ...
    def unique(self) -> StringList: ...


class IndexList:
    # Arrange the following methods in alphabetical order.

    def __init__(self, vec: Sequence[int]) -> None: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def back(self) -> int: ...
    def to_list(self) -> List[int]: ...


def arange32(start: int, stop: int, step: int) -> IntegerList32: ...


def arange64(start: int, stop: int, step: int) -> IntegerList64: ...


def select_bool(
    conditions: List[BooleanList],
    choices: LIST_PY,
    default: bool,
) -> BooleanList: ...


def select_float(
    conditions: List[BooleanList],
    choices: LIST_PY,
    default: float,
) -> FloatList64: ...


def select_int(
    conditions: List[BooleanList],
    choices: LIST_PY,
    default: int,
) -> IntegerList64: ...


def select_string(
    conditions: List[BooleanList],
    choices: LIST_PY,
    default: str,
) -> StringList: ...
