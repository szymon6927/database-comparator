import datetime
import uuid
from dataclasses import dataclass
from typing import Union

from src.core.entities.base_entity import BaseEntity


@dataclass
class Event(BaseEntity):
    id: uuid.UUID
    name: Union[str, None]
    city: Union[str, None]
    date: Union[datetime.datetime, None]
    created_at: Union[datetime.datetime, None]
