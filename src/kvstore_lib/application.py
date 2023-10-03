from abc import ABC, abstractmethod
from kvstore_lib.command import Command


class Application(ABC):
    @abstractmethod
    def execute(self, command: Command):
        ...
