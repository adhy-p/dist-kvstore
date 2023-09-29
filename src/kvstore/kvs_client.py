from kvstore_lib.node import Node
from kvstore.kvs_app import KVStore


class KVSClient(Node):
    def __init__(self, address: int):
        super().__init__(address, KVStore())

    def send_command(self, command: str, key: str, value: str | None = None):
        pass
