from abc import ABC
from typing import Any

from ...types.state_type import StateType

class BaseStorage(ABC):
    async def set_state(self, key: str, state: StateType = None) -> None:
        ...

    async def get_state(self, key: str) -> StateType:
        ...
    
    async def set_data(self, key: str, data: dict) -> None:
        ...

    async def get_data(self, key: str) -> dict[str, Any]:
        ...

    async def update_data(self, key: str, data: dict) -> None:
        ...

    async def clear(self, key: str) -> None:
        ...

    async def lock(self, key: str) -> None:
        ...

    async def unlock(self, key: str) -> None:
        ...
    
    async def is_locked(self, key: str) -> bool:
        ...
