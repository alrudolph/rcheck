from _typeshed import Incomplete
from rcheck.check import Check as Check
from types import TracebackType
from typing import Optional, Type

class CheckAll:
    check: Incomplete
    def __init__(self, *, check_instance: Check) -> None: ...
    def __enter__(self) -> Check: ...
    def __exit__(self, exc_type: Optional[Type[Exception]], exc_value: Optional[Exception], exc_tb: Optional[TracebackType]): ...

def check_all(): ...
