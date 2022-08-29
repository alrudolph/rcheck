# import pytest
# from rcheck import (
#     InvalidRuntype,
#     assert_list,
#     assert_list_of_opt,
#     assert_opt_list,
#     is_list,
#     is_list_of_opt,
#     is_opt_list,
# )


# class TestList:
#     @pytest.mark.parametrize(
#         "val,of,expected",
#         [
#             ([2, 3, 3], int, True),
#             ([2, 3, 3], None, True),
#             ([2, 3, 3, None, 5.0, "string"], None, True),
#             ([True, True, False], int, False),
#             ([1, 0, 1], bool, False),
#         ],
#     )
#     def test_is_list(self, val, of, expected):
#         if of is not None:
#             assert is_list(val, of) == expected
#         else:
#             assert is_list(val) == expected

#     @pytest.mark.parametrize(
#         "val,of,throws_exception",
#         [
#             ([2, 3, 3], int, False),
#             ([2, 3, 3], None, False),
#             ([2, 3, 3, None, 5.0, "string"], None, False),
#             ([True, True, False], int, True),
#             ([1, 0, 1], bool, True),
#         ],
#     )
#     def test_assert_list(self, val, of, throws_exception):
#         if throws_exception:
#             with pytest.raises(InvalidRuntype) as e:
#                 if of is not None:
#                     assert_list(val, name="my list", of=of)
#                 else:
#                     assert_list(val, name="my list")
#         else:
#             if of is not None:
#                 assert_list(val, name="my list", of=of)
#             else:
#                 assert_list(val, name="my list")

#     @pytest.mark.parametrize(
#         "val,of,expected",
#         [
#             ([2, 3, 3], int, True),
#             ([2, None, 3], int, True),
#             ([2, 3, 3, None, 5.0, "string"], str, False),
#             (None, None, False),
#             ([True, True, False], int, False),
#             ([1, 0, 1], bool, False),
#         ],
#     )
#     def test_is_list_of_opt(self, val, of, expected):
#         assert is_list_of_opt(val, of) == expected

#     @pytest.mark.parametrize(
#         "val,of,expected",
#         [
#             ([2, 3, 3], int, True),
#             ([2, None, 3], int, True),
#             ([2, 3, 3, None, 5.0, "string"], str, False),
#             (None, bool, False),
#             ([True, True, False], int, False),
#             ([1, 0, 1], bool, False),
#         ],
#     )
#     def test_assert_list_of_opt(self, val, of, expected):
#         if expected:
#             assert_list_of_opt(val, of, "my opt list")
#         else:
#             with pytest.raises(InvalidRuntype) as e:
#                 assert_list_of_opt(val, of, "my opt list")

#     @pytest.mark.parametrize(
#         "val,of,expected",
#         [
#             ([1, 2, 3], int, True),
#             ([1, 2, 3], None, True),
#             (["str", 1, 5.0], None, True),
#             (["str", 1, 5.0], (str, int, float), True),
#             (1, int, False),
#             (None, int, True),
#             (None, None, True),
#             ((1, 2, 3), int, False),
#             (map(lambda x: x, [1, 2, 3]), int, False),
#         ],
#     )
#     def test_is_opt_list(self, val, of, expected):
#         if of is not None:
#             assert is_opt_list(val, of) == expected
#         else:
#             assert is_opt_list(val) == expected

#     @pytest.mark.parametrize(
#         "val,of,expected",
#         [
#             ([1, 2, 3], int, True),
#             ([1, 2, 3], None, True),
#             (["str", 1, 5.0], None, True),
#             (["str", 1, 5.0], (str, int, float), True),
#             (1, int, False),
#             (None, int, True),
#             (None, None, True),
#             ((1, 2, 3), int, False),
#             (map(lambda x: x, [1, 2, 3]), int, False),
#         ],
#     )
#     def test_assert_opt_list(self, val, of, expected):
#         if expected:
#             if of is not None:
#                 assert_opt_list(val, "my opt list", of=of)
#             else:
#                 assert_opt_list(val, "my opt list")
#         else:
#             with pytest.raises(InvalidRuntype) as e:
#                 if of is not None:
#                     assert_opt_list(val, "my opt list", of=of)
#                 else:
#                     assert_opt_list(val, "my opt list")
