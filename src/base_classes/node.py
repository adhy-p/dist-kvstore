from abc import ABC
from base_classes.application import Application


class Node(ABC):
  """
  A node is a single computation unit in distributed systems.
  A node has an address, and it holds an application.
  """
  def __init__(self, id: int, app: Application):
    self.id = id
    self.app = app
