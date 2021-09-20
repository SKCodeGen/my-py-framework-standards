from abc import ABC, abstractmethod
from typing import Optional, Union
from pathlib import Path

import attr
import yaml


class BaseClient(ABC):
    def __init__(self, name: str, email: Optional[str]):
        self.name = name
        self.email = email

    @property
    @abstractmethod
    def parent(self) -> str:
        return "MoM"

    @abstractmethod
    def get_client_class_per_day(self):
        pass

    def read_and_print_interests(self, file_path: Union[str, Path]) -> dict:

        interests_dict = {}
        with open(file_path, 'r') as f:
            interests_dict = yaml.safe_load(f)
        return interests_dict


