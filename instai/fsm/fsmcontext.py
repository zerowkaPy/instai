from typing import Any

from ..types.state_type import StateType
from .storages.base_storage import BaseStorage

class FSMContext:
    def __init__(
        self,
        storage: BaseStorage,
        user_id: int ):
        
        self.storage = storage
        self.user_id = user_id
        self.key = str(user_id)

    async def set_state(self, state: StateType = None):
        await self.storage.set_state(self.key, state)

    async def get_state(self) -> str | None:
        return await self.storage.get_state(self.key)
    
    async def set_data(self, data: dict) -> None:
        await self.storage.set_data(self.key, data)

    async def get_data(self) -> dict[str, Any]:
        return await self.storage.get_data(self.key)

    async def update_data(self, data: dict) -> None:
        await self.storage.update_data(self.key, data)

    async def clear(self) -> None:
        await self.storage.clear(self.key)

