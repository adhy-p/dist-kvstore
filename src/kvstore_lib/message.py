from attrs import define
from typing import Any


@define
class Message:
    """
    Message class represents a message that is passed from a node to the other
    """
    src: int
    dst: int
    msg: dict[Any, Any]
    seq_num: int
