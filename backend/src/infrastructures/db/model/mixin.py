from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from sqlalchemy.ext.declarative import declared_attr
from datetime import datetime


class TimestampMixin:
    @declared_attr
    def created_at(cls) -> Mapped[datetime]:
        return mapped_column(
            Timestamp, nullable=False, server_default=text("current_timestamp")
        )

    @declared_attr
    def updated_at(cls) -> Mapped[datetime]:
        return mapped_column(
            Timestamp,
            nullable=False,
            server_default=text("current_timestamp on update current_timestamp"),
        )
