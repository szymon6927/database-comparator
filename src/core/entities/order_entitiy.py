import datetime
import uuid
from dataclasses import dataclass
from typing import Union

from src.core.entities.base_entity import BaseEntity


@dataclass
class Order(BaseEntity):
    id: uuid.UUID
    amount: Union[float, None]
    created_at: Union[datetime.datetime, None]
    updated_at: Union[datetime.datetime, None]
