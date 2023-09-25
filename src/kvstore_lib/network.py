from kvstore_lib.message import Message
from collections import deque


class Network:
  """
  This class simulates a network connection.
  - Nodes can send messages to the network and read from the network.
  - The messages can be dropped and/or reordered. (TODO)

  The buffer stores a list of tuples (src_addr, Message).
  """

  instances: dict[int, 'Network'] = dict()
  # reliability: float = 1.0
  # can_reorder: bool = False

  # def setup(self, reliability: float=1.0, can_reorder: bool=False):
  #   Network.reliability: float = reliability
  #   Network.can_reorder: bool = can_reorder

  def __init__(self, id: int):
    self.address: int = id
    self.inbox: deque[tuple[int, Message]] = deque()
    Network.instances[id] = self

  def send(self, dest_addr: int, msg: Message):
    """
    Send a message to the specified address
    """
    Network.instances[dest_addr].inbox.append((self.address, msg))

  def recv(self) -> tuple[int, Message]:
    """
    Receive a message from local inbox (blocking operation)
    """
    while not self.inbox:  # busy wait
      pass
    return self.inbox.popleft()
