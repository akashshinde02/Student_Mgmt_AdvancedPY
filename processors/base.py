"""Abstract base class for log processors"""
from abc import ABC, abstractmethod

class LogProcessor(ABC):
    @abstractmethod
    def process_line(self, line: str):
        pass

    @abstractmethod
    def summary(self) -> dict:
        pass
