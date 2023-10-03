from kvstore_lib.node import Node
from kvstore_lib.message import Message
from kvstore.kvs_app import KVStore
from kvstore_lib.amo_command import AMOCommand
from kvstore_lib.amo_application import AMOApp
from kvstore_lib.kvs_result import KVSResult
from kvstore_lib.amo_result import AMOResult
from kvstore_lib.kvs_exception import KVSException


class KVSServer(Node):
    def __init__(self, address: int):
        super().__init__(address, AMOApp(KVStore()))

    def handle_command(self, msg: Message) -> Message:
        amo_cmd: AMOCommand = msg.msg
        receiver: int = amo_cmd.dst
        if receiver == self.address:
            try:
                res: AMOResult = self.app.execute(amo_cmd)
                return Message(msg.dst, msg.src, res)
            except KVSException as e:
                return Message(msg.dst, msg.src, KVSResult((str(e))))
        return Message(msg.dst, msg.src, KVSResult(""))
