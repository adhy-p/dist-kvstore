from attrs import frozen
from kvstore_lib.result import Result


@frozen
class AMOResult(Result):
    """
    AMOResult is result sent by application that implements at most once semantics.
    """
    src: int
    dst: int
    res: Result
    seq_num: int
