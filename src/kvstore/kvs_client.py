from kvstore_lib.node import Node


class KVSClient(Node):
  def __init__(self, id: int):
    super().__init__(id, None)

  def send_command(self, command: str, key: str, value: str | None = None):
    pass
