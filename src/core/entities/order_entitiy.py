import datetime
from dataclasses import dataclass
from typing import Union

from src.core.entities.base_entity import BaseEntity


@dataclass
class Order(BaseEntity):
    amount: Union[float, None]
    updated_at: Union[datetime.datetime, None]
