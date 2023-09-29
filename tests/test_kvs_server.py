from kvstore_lib.message import Message
from kvstore.kvs_server import KVSServer

messages = [
  Message(src=0, dst=1, msg={'cmd_type': 'PUT', 'key': 'hello', 'value': 'world'}, seq_num=1),
  Message(src=0, dst=1, msg={'cmd_type': 'GET', 'key': 'hello'}, seq_num=1),
  Message(src=0, dst=1, msg={'cmd_type': 'GET', 'key': 'nokey'}, seq_num=1),
  Message(src=0, dst=1, msg={'cmd_type': 'APPEND', 'key': 'hello', 'value': 'ofpython'}, seq_num=1),
  Message(src=0, dst=1, msg={'cmd_type': 'APPEND', 'key': 'newkey', 'value': 'newval'}, seq_num=1),
  Message(src=0, dst=1, msg={'cmd_type': 'GET'}, seq_num=1),
  Message(src=0, dst=1, msg={'cmd_type': 'PUT'}, seq_num=1),
  Message(src=0, dst=1, msg={'cmd_type': 'APPEND'}, seq_num=1),
  Message(src=0, dst=1, msg={'cmd_type': 'GET', 'key': 'with_value', 'value': '1234'}, seq_num=1),
  Message(src=0, dst=1, msg={'cmd_type': 'PUT', 'key': 'without_value'}, seq_num=1),
  Message(src=0, dst=1, msg={'cmd_type': 'APPEND', 'key': 'without_value'}, seq_num=1),
  Message(src=0, dst=1, msg={'cmd_type': 'NEW_CMD', 'key': 'hello', 'value': 'world'}, seq_num=1),
]

expected = [
  Message(src=1, dst=0, msg={'ret_msg': 'PutOK'}, seq_num=0),
  Message(src=1, dst=0, msg={'ret_msg': 'world'}, seq_num=0),
  Message(src=1, dst=0, msg={'ret_msg': 'KeyNotFound'}, seq_num=0),
  Message(src=1, dst=0, msg={'ret_msg': 'worldofpython'}, seq_num=0),
  Message(src=1, dst=0, msg={'ret_msg': 'newval'}, seq_num=0),
  Message(src=1, dst=0, msg={'ret_msg': 'Error: Key must be specified'}, seq_num=0),
  Message(src=1, dst=0, msg={'ret_msg': 'Error: Key/Value must be specified'}, seq_num=0),
  Message(src=1, dst=0, msg={'ret_msg': 'Error: Key/Value must be specified'}, seq_num=0),
  Message(src=1, dst=0, msg={'ret_msg': 'KeyNotFound'}, seq_num=0),
  Message(src=1, dst=0, msg={'ret_msg': 'Error: Key/Value must be specified'}, seq_num=0),
  Message(src=1, dst=0, msg={'ret_msg': 'Error: Key/Value must be specified'}, seq_num=0),
  Message(src=1, dst=0, msg={'ret_msg': 'Error: Unknown command'}, seq_num=0),
]


def test_kvs_server():
  s = KVSServer(1)
  for m, exp in zip(messages, expected):
    assert (s.handle_command(m) == exp)
