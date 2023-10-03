from attrs import frozen
from kvstore_lib.command import Command


@frozen
class KVSCommand(Command):
    cmd_type: str
    key: str
    value: str | None = None
