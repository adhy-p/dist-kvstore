from kvstore_lib.node import Node
from kvstore_lib.message import Message
from kvstore.kvs_app import KVStore
from typing import Any


class KVSServer(Node):
    def __init__(self, address: int):
        super().__init__(address, KVStore())
        self.app: KVStore

    def handle_command(self, command: Message) -> Message:
        sender: int = command.src
        receiver: int = command.dst
        app_cmd: dict[Any, Any] = command.msg
        if receiver == self.address:
            try:
                ret = self.app.execute(app_cmd)
                return Message(self.address, sender, {'ret_msg': ret}, 0)
            except Exception as e:
                return Message(self.address, sender, {'ret_msg': str(e)}, 0)
        return Message(self.address, sender, {'ret_msg': 'Wrong Address'}, 0)
