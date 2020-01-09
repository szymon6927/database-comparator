import datetime
import uuid
from dataclasses import dataclass
from typing import Union

from src.core.entities.base_entity import BaseEntity


@dataclass
class Customer(BaseEntity):
    id: uuid.UUID
    name: Union[str, None]
    age: Union[int, None]
    company_name: Union[str, None]
    created_at: Union[datetime.datetime, None]
