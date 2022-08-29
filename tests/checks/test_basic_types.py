from datetime import date, datetime

import pytest
from rcheck import (
    InvalidRuntype,
    assert_bool,
    assert_callable,
    assert_date,
    assert_datetime,
    assert_float,
    assert_instance,
    assert_int,
    assert_number,
    assert_opt_bool,
    assert_opt_callable,
    assert_opt_date,
    assert_opt_datetime,
    assert_opt_float,
    assert_opt_instance,
    assert_opt_int,
    assert_opt_number,
    assert_opt_str,
    assert_str,
    is_bool,
    is_callable,
    is_date,
    is_datetime,
    is_float,
    is_instance,
    is_int,
    is_number,
    is_opt_bool,
    is_opt_callable,
    is_opt_date,
    is_opt_datetime,
    is_opt_float,
    is_opt_instance,
    is_opt_int,
    is_opt_number,
    is_opt_str,
    is_str,
)


class TestBool:
    @pytest.mark.parametrize(
        "val,expected",
        [
            (True, True),
            (False, True),
            (10, False),
            (0, False),
            ("not bool", False),
            (None, False),
        ],
    )
    def test_is_bool(self, val, expected):
        assert is_bool(val) == expected

    @pytest.mark.parametrize(
        "val,expected",
        [
            (True, True),
            (False, True),
            (10, False),
            (0, False),
            ("not bool", False),
            (None, True),
        ],
    )
    def test_is_opt_bool(self, val, expected):
        assert is_opt_bool(val) == expected

    @pytest.mark.parametrize(
        "val,name,raises",
        [
            (True, "my_bool", False),
            (False, "my_bool", False),
            (10, "my_bool", True),
            (0, "my_bool", True),
            ("not bool", "my_bool", True),
            (None, "my_bool", True),
        ],
    )
    def test_assert_bool(self, val, name, raises):
        if raises:
            with pytest.raises(InvalidRuntype) as e:
                assert_bool(val, name)
        else:
            assert_bool(val, name)

    @pytest.mark.parametrize(
        "val,name,raises",
        [
            (True, "my_bool", False),
            (False, "my_bool", False),
            (10, "my_bool", True),
            (0, "my_bool", True),
            ("not bool", "my_bool", True),
            (None, "my_bool", False),
        ],
    )
    def test_assert_opt_bool(self, val, name, raises):
        if raises:
            with pytest.raises(InvalidRuntype) as e:
                assert_opt_bool(val, name)
        else:
            assert_opt_bool(val, name)


class TestStr:
    @pytest.mark.parametrize(
        "val,expected",
        [
            (True, False),
            (10, False),
            ("is str", True),
            (None, False),
        ],
    )
    def test_is_str(self, val, expected):
        assert is_str(val) == expected

    @pytest.mark.parametrize(
        "val,expected",
        [
            (True, False),
            (10, False),
            ("is str", True),
            (None, True),
        ],
    )
    def test_is_opt_str(self, val, expected):
        assert is_opt_str(val) == expected

    @pytest.mark.parametrize(
        "val,name,raises",
        [
            (True, "my str", True),
            (10, "my str", True),
            ("not bool", "my str", False),
            (None, "my str", True),
        ],
    )
    def test_assert_str(self, val, name, raises):
        if raises:
            with pytest.raises(InvalidRuntype) as e:
                assert_str(val, name)
        else:
            assert_str(val, name)

    @pytest.mark.parametrize(
        "val,name,raises",
        [
            (True, "my str", True),
            (10, "my str", True),
            ("not bool", "my str", False),
            (None, "my str", False),
        ],
    )
    def test_assert_opt_str(self, val, name, raises):
        if raises:
            with pytest.raises(InvalidRuntype) as e:
                assert_opt_str(val, name)
        else:
            assert_opt_str(val, name)


class TestInt:
    @pytest.mark.parametrize(
        "val,expected",
        [
            (True, False),
            (10, True),
            ("is str", False),
            (None, False),
        ],
    )
    def test_is_int(self, val, expected):
        assert is_int(val) == expected

    @pytest.mark.parametrize(
        "val,expected",
        [
            (True, False),
            (10, True),
            ("is str", False),
            (None, True),
        ],
    )
    def test_is_opt_int(self, val, expected):
        assert is_opt_int(val) == expected

    @pytest.mark.parametrize(
        "val,name,raises",
        [
            (True, "my int", True),
            (10, "my int", False),
            ("not bool", "my int", True),
            (None, "my int", True),
        ],
    )
    def test_assert_int(self, val, name, raises):
        if raises:
            with pytest.raises(InvalidRuntype) as e:
                assert_int(val, name)
        else:
            assert_int(val, name)

    @pytest.mark.parametrize(
        "val,name,raises",
        [
            (True, "my int", True),
            (10, "my int", False),
            ("not bool", "my int", True),
            (None, "my int", False),
        ],
    )
    def test_assert_opt_int(self, val, name, raises):
        if raises:
            with pytest.raises(InvalidRuntype) as e:
                assert_opt_int(val, name)
        else:
            assert_opt_int(val, name)


class TestFloat:
    @pytest.mark.parametrize(
        "val,expected",
        [
            (True, False),
            (10.0, True),
            (10, False),
            ("is str", False),
            (None, False),
        ],
    )
    def test_is_float(self, val, expected):
        assert is_float(val) == expected

    @pytest.mark.parametrize(
        "val,expected",
        [
            (True, False),
            (10.0, True),
            (10, False),
            ("is str", False),
            (None, True),
        ],
    )
    def test_is_opt_float(self, val, expected):
        assert is_opt_float(val) == expected

    @pytest.mark.parametrize(
        "val,name,raises",
        [
            (True, "my float", True),
            (10.0, "my float", False),
            (10, "my float", True),
            ("not bool", "my float", True),
            (None, "my float", True),
        ],
    )
    def test_assert_float(self, val, name, raises):
        if raises:
            with pytest.raises(InvalidRuntype) as e:
                assert_float(val, name)
        else:
            assert_float(val, name)

    @pytest.mark.parametrize(
        "val,name,raises",
        [
            (True, "my float", True),
            (10.0, "my float", False),
            (10, "my float", True),
            ("not bool", "my float", True),
            (None, "my float", False),
        ],
    )
    def test_assert_opt_float(self, val, name, raises):
        if raises:
            with pytest.raises(InvalidRuntype) as e:
                assert_opt_float(val, name)
        else:
            assert_opt_float(val, name)


class TestNumber:
    @pytest.mark.parametrize(
        "val,expected",
        [
            (True, False),
            (10.0, True),
            (10, True),
            ("is str", False),
            (None, False),
        ],
    )
    def test_is_number(self, val, expected):
        assert is_number(val) == expected

    @pytest.mark.parametrize(
        "val,expected",
        [
            (True, False),
            (10.0, True),
            (10, True),
            ("is str", False),
            (None, True),
        ],
    )
    def test_is_opt_number(self, val, expected):
        assert is_opt_number(val) == expected

    @pytest.mark.parametrize(
        "val,name,raises",
        [
            (True, "my number", True),
            (10.0, "my number", False),
            (1, "my number", False),
            ("not bool", "my number", True),
            (None, "my number", True),
        ],
    )
    def test_assert_number(self, val, name, raises):
        if raises:
            with pytest.raises(InvalidRuntype) as e:
                assert_number(val, name)
        else:
            assert_number(val, name)

    @pytest.mark.parametrize(
        "val,name,raises",
        [
            (True, "my number", True),
            (10.0, "my number", False),
            (1, "my number", False),
            ("not bool", "my number", True),
            (None, "my number", False),
        ],
    )
    def test_assert_opt_number(self, val, name, raises):
        if raises:
            with pytest.raises(InvalidRuntype) as e:
                assert_opt_number(val, name)
        else:
            assert_opt_number(val, name)


class TestClass:
    @pytest.mark.parametrize(
        "val,cls,expected",
        [
            (True, int, False),
            (10.0, float, True),
            (10, (int, float), True),
            (None, str, False),
        ],
    )
    def test_is_instance(self, val, cls, expected):
        assert is_instance(val, cls) == expected

    @pytest.mark.parametrize(
        "val,cls,expected",
        [
            (True, int, False),
            (10.0, float, True),
            (10, (int, float), True),
            (None, str, True),
        ],
    )
    def test_is_opt_instance(self, val, cls, expected):
        assert is_opt_instance(val, cls) == expected

    @pytest.mark.parametrize(
        "val,cls,name,raises",
        [
            (True, int, "my instance", True),
            (10.0, float, "my instance", False),
            (1, (int, float), "my instance", False),
            ("not bool", bool, "my instance", True),
            (None, str, "my instance", True),
        ],
    )
    def test_assert_instance(self, val, cls, name, raises):
        if raises:
            with pytest.raises(InvalidRuntype) as e:
                assert_instance(val, cls, name)
        else:
            assert_instance(val, cls, name)

    @pytest.mark.parametrize(
        "val,cls,name,raises",
        [
            (True, int, "my instance", True),
            (10.0, float, "my instance", False),
            (1, (int, float), "my instance", False),
            ("not bool", bool, "my instance", True),
            (None, str, "my instance", False),
        ],
    )
    def test_assert_opt_instance(self, val, cls, name, raises):
        if raises:
            with pytest.raises(InvalidRuntype) as e:
                assert_opt_instance(val, cls, name)
        else:
            assert_opt_instance(val, cls, name)


class TestCallable:
    @pytest.mark.parametrize(
        "val,expected",
        [
            (True, False),
            (lambda x: x, True),
            ("is str", False),
            (None, False),
        ],
    )
    def test_is_callable(self, val, expected):
        assert is_callable(val) == expected

    @pytest.mark.parametrize(
        "val,expected",
        [
            (True, False),
            (lambda x: x, True),
            ("is str", False),
            (None, True),
        ],
    )
    def test_is_opt_callable(self, val, expected):
        assert is_opt_callable(val) == expected

    @pytest.mark.parametrize(
        "val,name,raises",
        [
            (True, "my callable", True),
            (lambda x: x, "my callable", False),
            ("not bool", "my callable", True),
            (None, "my callable", True),
        ],
    )
    def test_assert_callable(self, val, name, raises):
        if raises:
            with pytest.raises(InvalidRuntype) as e:
                assert_callable(val, name)
        else:
            assert_callable(val, name)

    @pytest.mark.parametrize(
        "val,name,raises",
        [
            (True, "my callable", True),
            (lambda x: x, "my callable", False),
            ("not bool", "my callable", True),
            (None, "my callable", False),
        ],
    )
    def test_assert_opt_callable(self, val, name, raises):
        if raises:
            with pytest.raises(InvalidRuntype) as e:
                assert_opt_callable(val, name)
        else:
            assert_opt_callable(val, name)


class TestDate:
    # not that datetimes are a subclass of dates
    @pytest.mark.parametrize(
        "val,expected",
        [
            (True, False),
            (None, False),
            ("is str", False),
            (date(2022, 1, 1), True),
            (datetime(2022, 1, 1), True),
        ],
    )
    def test_is_date(self, val, expected):
        assert is_date(val) == expected

    @pytest.mark.parametrize(
        "val,expected",
        [
            (True, False),
            (None, True),
            ("is str", False),
            (date(2022, 1, 1), True),
            (datetime(2022, 1, 1), True),
        ],
    )
    def test_is_opt_date(self, val, expected):
        assert is_opt_date(val) == expected

    @pytest.mark.parametrize(
        "val,name,raises",
        [
            (True, "my date", True),
            (None, "my date", True),
            ("not bool", "my date", True),
            (date(2022, 1, 1), "my date", False),
            (datetime(2022, 1, 1, 5), "my date", False),
        ],
    )
    def test_assert_date(self, val, name, raises):
        if raises:
            with pytest.raises(InvalidRuntype) as e:
                assert_date(val, name)
        else:
            assert_date(val, name)

    @pytest.mark.parametrize(
        "val,name,raises",
        [
            (True, "my date", True),
            (None, "my date", False),
            ("not bool", "my date", True),
            (date(2022, 1, 1), "my date", False),
            (datetime(2022, 1, 1, 5), "my date", False),
        ],
    )
    def test_assert_opt_date(self, val, name, raises):
        if raises:
            with pytest.raises(InvalidRuntype) as e:
                assert_opt_date(val, name)
        else:
            assert_opt_date(val, name)


class TestDatetime:
    @pytest.mark.parametrize(
        "val,expected",
        [
            (True, False),
            (None, False),
            ("is str", False),
            (date(2022, 1, 1), False),
            (datetime(2022, 1, 1), True),
        ],
    )
    def test_is_datetime(self, val, expected):
        assert is_datetime(val) == expected

    @pytest.mark.parametrize(
        "val,expected",
        [
            (True, False),
            (None, True),
            ("is str", False),
            (date(2022, 1, 1), False),
            (datetime(2022, 1, 1), True),
        ],
    )
    def test_is_opt_datetime(self, val, expected):
        assert is_opt_datetime(val) == expected

    @pytest.mark.parametrize(
        "val,name,raises",
        [
            (True, "my date", True),
            (None, "my date", True),
            ("not bool", "my date", True),
            (date(2022, 1, 1), "my date", True),
            (datetime(2022, 1, 1, 5), "my date", False),
        ],
    )
    def test_assert_datetime(self, val, name, raises):
        if raises:
            with pytest.raises(InvalidRuntype) as e:
                assert_datetime(val, name)
        else:
            assert_datetime(val, name)

    @pytest.mark.parametrize(
        "val,name,raises",
        [
            (True, "my date", True),
            (None, "my date", False),
            ("not bool", "my date", True),
            (date(2022, 1, 1), "my date", True),
            (datetime(2022, 1, 1, 5), "my date", False),
        ],
    )
    def test_assert_opt_datetime(self, val, name, raises):
        if raises:
            with pytest.raises(InvalidRuntype) as e:
                assert_opt_datetime(val, name)
        else:
            assert_opt_datetime(val, name)
