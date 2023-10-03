from attrs import frozen
from kvstore_lib.application import Application


@frozen
class Node:
    """
    A node is a single computation unit in distributed systems.
    A node has an address, and it holds an application.
    """
    address: int
    app: Application
