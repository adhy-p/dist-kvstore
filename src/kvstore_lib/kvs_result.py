from attrs import frozen
from kvstore_lib.result import Result


@frozen
class KVSResult(Result):
    res: str
