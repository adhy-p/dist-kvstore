from base_classes.node import Node
from base_classes.message import Message
from kvstore.kvs_app import KVStore


class KVSServer(Node):
  def __init__(self, id: int):
    super().__init__(id, KVStore())
    self.app: KVStore
    self.COMMANDS = {
      'GET',
      'PUT',
      'APPEND',
    }

  def handle_command(self, m: Message) -> Message:
    if not m:
      return Message({'ret_msg': 'Error: Empty message'}, 0)

    msg: dict[str, str] = m.message
    # seq_num: int = m.seq_num
    if msg.get('command', None) not in self.COMMANDS:
      return Message({'ret_msg': 'Error: Unknown command'}, 0)

    cmd: str = msg['command']
    key: str | None = msg.get('key')
    value: str | None = msg.get('value', None)
    ret: str = ""
    if cmd == 'GET':
      if not key:
        return Message({'ret_msg': 'Error: Key must be specified'}, 0)
      ret = self.app.get(key)
    elif cmd == 'PUT':
      if not key or not value:
        return Message({'ret_msg': 'Error: Key/Value must be specified'}, 0)
      ret = self.app.put(key, value)
    elif cmd == 'APPEND':
      if not key or not value:
        return Message({'ret_msg': 'Error: Key/Value must be specified'}, 0)
      ret = self.app.append(key, value)
    return Message({'ret_msg': ret}, 0)
