from ...types.state_type import StateType
from ...types.bot_status import OPEN, CLOSED
from .base_storage import BaseStorage
from ...utils.storage_keys import (
        get_state_key,
        get_data_key,
        get_status_key
    )


class MemoryStorage(BaseStorage):
    def __init__(self):
        self.state = {}
        self.data = {}
        self.status = {}

    async def set_state(self, key: str, state: StateType = None):
        key = get_state_key(key)
        self.state[key] = state

    async def get_state(self, key: str) -> StateType:
        key = get_state_key(key)
        state = self.state.get(key)
        return state
    
    async def set_data(self, key: str, data: dict):
        key = get_data_key(key)
        self.data[key] = data

    async def get_data(self, key: str) -> dict:
        key = get_data_key(key)
        data = self.data.get(key)
        if data is None:
            return {}
        return data

    async def update_data(self, key: str, data: dict):
        current = await self.get_data(key)
        current.update(data)
        await self.set_data(key, current)

    async def clear(self, key: str):
        state_key = get_state_key(key)
        data_key = get_data_key(key)
        self.state.pop(state_key, None)
        self.data.pop(data_key, None)

    async def lock(self, key: str) -> None:
        key = get_status_key(key)
        self.status[key] = CLOSED

    async def unlock(self, key: str) -> None:
        key = get_status_key(key)
        self.status[key] = OPEN

    async def is_locked(self, key: str) -> bool:
        status = await self.get_bot_status(key)
        if status == OPEN:
            return False
        return True
        
    async def get_bot_status(self, key: str):
        key = get_status_key(key)
        status = self.status.get(key, OPEN)
        return status