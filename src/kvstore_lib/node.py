from abc import ABC
from kvstore_lib.application import Application


class Node(ABC):
  """
  A node is a single computation unit in distributed systems.
  A node has an address, and it holds an application.
  """
  def __init__(self, id: int, app: Application | None):
    self.id = id
    self.app = app
