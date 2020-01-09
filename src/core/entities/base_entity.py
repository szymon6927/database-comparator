import datetime
import uuid
from dataclasses import dataclass
from typing import Union


@dataclass
class BaseEntity:
    id: uuid.UUID
    created_at: Union[datetime.datetime, None]
