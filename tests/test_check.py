from collections.abc import Mapping, Sequence
from typing import Any, Optional, Type, Union

import pytest

from rcheck import Check


@pytest.fixture
def r_check():
    return Check(suppress_and_record=False)


@pytest.mark.parametrize(
    "primitive_value,primitive_type",
    [
        ("my_str", str),
        (10, int),
        (1.4, float),
        (True, bool),
        (bytes("hello", encoding="utf-8"), bytes),
    ],
)
def test_generic_isinstance_primitive_success(
    primitive_value: Any, primitive_type: Type[Any], r_check: Check
):
    assert r_check._generic_isinstance(primitive_value, primitive_type)[0] # type: ignore


@pytest.mark.parametrize(
    "primitive_value,primitive_type",
    [
        ("my_str", int),
        (10, float),
        (1.4, bool),
        (True, bytes),
        (bytes("hello", encoding="utf-8"), str),
    ],
)
def test_generic_isinstance_primitive_failures(
    primitive_value: Any, primitive_type: Type[Any], r_check: Check
):
    assert not r_check._generic_isinstance(primitive_value, primitive_type)[0] # type: ignore


@pytest.mark.parametrize(
    "type_",
    [
        (Optional[int]),
        (Union[int, None]),
        (Union[None, int]),
        (Union[str, None, int]),
    ],
)
def test_generic_isinstance_optional_none_success(type_: Type[Any], r_check: Check):
    assert r_check._generic_isinstance(None, type_)[0] # type: ignore


@pytest.mark.parametrize(
    "value,type_",
    [
        (1, Optional[int]),
        (2, Union[int, None]),
        (3, Union[None, int]),
        ("hello", Union[str, None, int]),
        (4, Union[str, None, int]),
        ([[12]], Union[Sequence[Sequence[int]], Mapping[Sequence[int], Sequence[str]]]),
        ({1: ["hello"]}, Union[Sequence[Sequence[int]], Mapping[int, Sequence[str]]]),
        ([1, 2, "three", "four"], Sequence[Union[int, str]]),
    ],
)
def test_generic_isinstance_optional_value_success(
    value: Any, type_: Type[Any], r_check: Check
):
    assert r_check._generic_isinstance(value, type_)[0] # type: ignore
