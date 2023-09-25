from kvstore_lib.message import Message
from kvstore.kvs_server import KVSServer

messages = [
  Message(message={'command': 'PUT', 'key': 'hello', 'value': 'world'}, seq_num=1),
  Message(message={'command': 'GET', 'key': 'hello'}, seq_num=1),
  Message(message={'command': 'GET', 'key': 'nokey'}, seq_num=1),
  Message(message={'command': 'APPEND', 'key': 'hello', 'value': 'ofpython'}, seq_num=1),
  Message(message={'command': 'APPEND', 'key': 'newkey', 'value': 'newvalue'}, seq_num=1),
  Message(message={'command': 'GET'}, seq_num=1),
  Message(message={'command': 'PUT'}, seq_num=1),
  Message(message={'command': 'APPEND'}, seq_num=1),
  Message(message={'command': 'GET', 'key': 'with_value', 'value': '1234'}, seq_num=1),
  Message(message={'command': 'PUT', 'key': 'without_value'}, seq_num=1),
  Message(message={'command': 'APPEND', 'key': 'without_value'}, seq_num=1),
  Message(message={'command': 'NEW_COMMAND', 'key': 'hello', 'value': 'world'}, seq_num=1),
]

expected = [
  Message(message={'ret_msg': 'PutOK'}, seq_num=0),
  Message(message={'ret_msg': 'world'}, seq_num=0),
  Message(message={'ret_msg': 'KeyNotFound'}, seq_num=0),
  Message(message={'ret_msg': 'worldofpython'}, seq_num=0),
  Message(message={'ret_msg': 'newvalue'}, seq_num=0),
  Message(message={'ret_msg': 'Error: Key must be specified'}, seq_num=0),
  Message(message={'ret_msg': 'Error: Key/Value must be specified'}, seq_num=0),
  Message(message={'ret_msg': 'Error: Key/Value must be specified'}, seq_num=0),
  Message(message={'ret_msg': 'KeyNotFound'}, seq_num=0),
  Message(message={'ret_msg': 'Error: Key/Value must be specified'}, seq_num=0),
  Message(message={'ret_msg': 'Error: Key/Value must be specified'}, seq_num=0),
  Message(message={'ret_msg': 'Error: Unknown command'}, seq_num=0),
]


def test_kvs_server():
  s = KVSServer(1)
  for m, exp in zip(messages, expected):
    assert (s.handle_command(m) == exp)
