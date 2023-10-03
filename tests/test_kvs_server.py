from kvstore_lib.message import Message
from kvstore_lib.amo_command import AMOCommand
from kvstore_lib.kvs_command import KVSCommand
from kvstore_lib.amo_result import AMOResult
from kvstore_lib.kvs_result import KVSResult
from kvstore.kvs_server import KVSServer

messages = [
  Message(0, 1, AMOCommand(src=0, dst=1, cmd=KVSCommand('PUT', 'hello', 'world'), seq_num=1)),
  Message(0, 1, AMOCommand(src=0, dst=1, cmd=KVSCommand('GET', 'hello'), seq_num=1)),
  Message(0, 1, AMOCommand(src=0, dst=1, cmd=KVSCommand('GET', 'nokey'), seq_num=1)),
  Message(0, 1, AMOCommand(src=0, dst=1, cmd=KVSCommand('APPEND', 'hello', 'ofpython'), seq_num=1)),
  Message(0, 1, AMOCommand(src=0, dst=1, cmd=KVSCommand('APPEND', 'newkey', 'newval'), seq_num=1)),
  Message(0, 1, AMOCommand(src=0, dst=1, cmd=KVSCommand('GET', 'with_value', '1234'), seq_num=1)),
  Message(0, 1, AMOCommand(src=0, dst=1, cmd=KVSCommand('PUT', 'without_value'), seq_num=1)),
  Message(0, 1, AMOCommand(src=0, dst=1, cmd=KVSCommand('APPEND', 'without_value'), seq_num=1)),
  Message(0, 1, AMOCommand(src=0, dst=1, cmd=KVSCommand('NEW_CMD', 'hello', 'world'), seq_num=1)),
  # at most once
  Message(0, 1, AMOCommand(src=0, dst=1, cmd=KVSCommand('APPEND', 'once', 'once'), seq_num=1)),
  Message(0, 1, AMOCommand(src=0, dst=1, cmd=KVSCommand('APPEND', 'once', 'once'), seq_num=1)),
  Message(0, 1, AMOCommand(src=0, dst=1, cmd=KVSCommand('APPEND', 'once', 'once'), seq_num=1)),
  Message(0, 1, AMOCommand(src=0, dst=1, cmd=KVSCommand('APPEND', 'once', 'more'), seq_num=2)),
]

expected = [
  Message(1, 0, AMOResult(src=1, dst=0, res=KVSResult('PutOK'), seq_num=2)),
  Message(1, 0, AMOResult(src=1, dst=0, res=KVSResult('world'), seq_num=2)),
  Message(1, 0, AMOResult(src=1, dst=0, res=KVSResult('KeyNotFound'), seq_num=2)),
  Message(1, 0, AMOResult(src=1, dst=0, res=KVSResult('worldofpython'), seq_num=2)),
  Message(1, 0, AMOResult(src=1, dst=0, res=KVSResult('newval'), seq_num=2)),
  Message(1, 0, AMOResult(src=1, dst=0, res=KVSResult('KeyNotFound'), seq_num=2)),
  Message(1, 0, AMOResult(src=1, dst=0, res=KVSResult('Error: Key/Value must be specified'),
                          seq_num=2)),
  Message(1, 0, AMOResult(src=1, dst=0, res=KVSResult('Error: Key/Value must be specified'),
                          seq_num=2)),
  Message(1, 0, AMOResult(src=1, dst=0, res=KVSResult('Error: Unknown command'), seq_num=2)),
  # at most once
  Message(1, 0, AMOResult(src=1, dst=0, res=KVSResult('once'), seq_num=2)),
  Message(1, 0, AMOResult(src=1, dst=0, res=KVSResult('once'), seq_num=2)),
  Message(1, 0, AMOResult(src=1, dst=0, res=KVSResult('once'), seq_num=2)),
  Message(1, 0, AMOResult(src=1, dst=0, res=KVSResult('oncemore'), seq_num=3)),
]


def test_kvs_server():
  s = KVSServer(1)
  for m, exp in zip(messages, expected):
    assert (s.handle_command(m) == exp)
