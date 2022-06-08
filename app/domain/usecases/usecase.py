from abc import ABC, abstractmethod
from typing import Any, Optional


class Usecase(ABC):
    @abstractmethod
    def execute(self, *args: Optional[Any]):
        raise NotImplementedError('This contract method must be implemented')