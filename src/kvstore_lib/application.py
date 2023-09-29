from abc import ABC, abstractmethod
from typing import Any


class Application(ABC):
    @abstractmethod
    def execute(self, command: Any):
        ...
