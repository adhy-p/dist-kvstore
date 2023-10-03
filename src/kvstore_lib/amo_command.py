from attrs import frozen
from kvstore_lib.command import Command


@frozen
class AMOCommand(Command):
    """
    AMOCommand is command sent to application that implements at most once semantics.
    """
    src: int
    dst: int
    cmd: Command
    seq_num: int
