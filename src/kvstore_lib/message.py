from attrs import define


@define
class Message:
  """
  Message class represents a message that is passed from a node to the other
  for requests, message attr contains:
  - command: str = GET | PUT | APPEND
  - key: str
  - [optional] value: str

  for replies, message attr contains:
  - ret_msg: str
  """
  message: dict[str, str]
  seq_num: int
