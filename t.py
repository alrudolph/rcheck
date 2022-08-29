from datetime import datetime

from rcheck import assert_list, check, is_datetime


@check
def add(a, b):
    return a + b


@check()
def mult(a, b):
    return a * b


# @check(
#     ins={
#         "n": {
#             "Input is positive": lambda x: x >= 0,
#             "Input is an int": is_int,
#         }
#     },
#     # pre_check = {
#     #     "gods are in your favor": lambda x: x.n > 0
#     # },
#     out={
#         "Factorial is greater than 1": lambda x: x >= 1,
#         "Factorial is integer": is_int,
#     },
#     post_check={"out bigger than in": lambda ins, out: ins.n <= out},
# )
# def factorial(n):
#     out = 1

#     for i in range(1, n + 1):
#         out *= i

#     return out


# print(factorial(n=5))

# assert_bool(5, "test_var")

assert_list([1, 2, 3, 2], of=int, name="my test opt")


@check(
    ins={
        "start_date": is_datetime,
        "middle_date": is_datetime,
    },
    pre_check={
        "Middle date comes after start date": lambda ins: ins.start_date
        < ins.middle_date
    },
)
def get_next_date(start_date, middle_date):
    return middle_date + (middle_date - start_date)


get_next_date(datetime(2022, 2, 1), datetime(2022, 1, 1))
