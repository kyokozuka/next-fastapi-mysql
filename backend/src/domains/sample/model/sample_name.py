from dataclasses import dataclass


@dataclass(frozen=True)
class SampleName:
    value: str

    def __post_init__(self) -> None:
        if not self.value:
            raise ValueError("Sample name cannot be empty")
        if len(self.value) < 1:
            raise ValueError("Sample name must be at least 1 character long")
        if len(self.value) > 255:
            raise ValueError("Sample name is too long")
