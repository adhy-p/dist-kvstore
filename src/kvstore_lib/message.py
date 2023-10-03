from attrs import frozen
from typing import Any


@frozen
class Message:
    """
    Message class represents a message that is passed from a node to the other
    """
    src: int
    dst: int
    msg: Any
