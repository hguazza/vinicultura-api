from abc import ABC, abstractmethod
from typing import Any, List

from pydantic import BaseModel


class BaseExtraction(ABC):
    """
    Base class for all extraction classes.
    """

    def __init__(self) -> None:
        pass

    @abstractmethod
    def extract(self, year: int) -> BaseModel:
        pass
    
    @abstractmethod
    def normalize(self, data: List[dict[str, str]], *args: Any) -> List[dict[str, str]]:
        """
        Normalize the data extracted from the source.
        """
        pass