from typing import Protocol

class ButtonBase(Protocol):
    def _to_json(self) -> dict:...