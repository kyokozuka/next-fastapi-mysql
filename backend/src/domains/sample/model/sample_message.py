from dataclasses import dataclass


@dataclass(frozen=True)
class SampleMessage:
    value: str
