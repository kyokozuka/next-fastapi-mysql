from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class UpdatedAt:
    value: datetime
