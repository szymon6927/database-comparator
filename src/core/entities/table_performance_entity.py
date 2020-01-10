from dataclasses import dataclass


@dataclass
class TablePerformance:
    table_name: str
    insert_time: float
    get_by_id_time: float
    get_all_time: float
