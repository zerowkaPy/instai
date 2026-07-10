import json
import inspect
from typing import Callable, Any

from redis.asyncio import Redis

from ..types.state_type import StateType
from ..utils.redis_storage_keys import user_id_to_key
from ..types.bot_status import OPEN, CLOSED


class FSMContext:
    def __init__(
        self,
        client: Redis,
        user_id: int ):
        
        self.client = client
        self.user_id = user_id
        self.key = user_id_to_key(user_id)

    async def set_state(self, state: StateType = None):
        key = self.key
        if state is None:
            state = "null"
        await self.client.set(key, state, ex=86_400)

    async def get_state(self) -> StateType:
        key = self.key
        state = await self.client.get(key)
        if type(state) is bytes:
            state = state.decode("utf-8")
        if state == "null":
            state = None
        return state
    
    async def set_data(self, data: dict):
        key = f"{self.key}:data"
        await self.client.set(key, json.dumps(data), ex=86_400)

    async def get_data(self) -> dict:
        key = f"{self.key}:data"
        data = await self.client.get(key)
        if data is None:
            return {}
        if isinstance(data, bytes):
            data = data.decode("utf-8")
        return json.loads(data)

    async def update_data(self, data: dict):
        current = await self.get_data()
        if not isinstance(current, dict):
            current = {}
        current.update(data)
        await self.set_data(current)

    async def clear(self):
        key = self.key
        data_key = f"{key}:data"
        await self.client.delete(key)
        await self.client.delete(data_key)

    async def _lock_bot(self):
        key = f"{self.key}:status"
        await self.client.set(key, CLOSED, ex=86_400)

    async def _unlock_bot(self):
        key = f"{self.key}:status"
        await self.client.set(key, OPEN, ex=86_400)
    
    async def _get_bot_status(self):
        key = f"{self.key}:status"
        data = await self.client.get(key)
        if isinstance(data, bytes):
            data = data.decode("utf-8")
        return data
    
    async def _status_permission(self, func: Callable[..., Any]):
        sig = inspect.signature(func)
        status = await self._get_bot_status()
        flag = False
        for param in sig.parameters.values():
            if param.name == "lock":
                if param.default is True and status != CLOSED:
                    flag = True
                    await self._lock_bot()

            if param.name == "unlock":
                if param.default is True and status != OPEN:
                    flag = True
                    await self._unlock_bot()
        if status == OPEN:
            return True
        
        if not flag:
            return False
        else:
            return True
