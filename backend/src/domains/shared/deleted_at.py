from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class DeletedAt:
    value: datetime | None
