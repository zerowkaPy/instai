from typing import Protocol, Any

from .types.message import Message
from .types.state_type import StateType
from .fsm.fsmcontext import FSMContext
from .types.callback import Callback

class FilterObj(Protocol):
    def __call__(self, *args: Any, **kwargs: Any) -> bool | Any: ...

class TextFilter(FilterObj):
    def __init__(self, text: str):
        self.text = text

    def __call__(self, msg: Message):
        return  msg.text == self.text
    
    def __repr__(self):
        return f"TextFilter({self.text})"
    
class StateFilter(FilterObj):
    def __init__(
        self,
        state: StateType):

        self.state = state

    async def __call__(self, fsm: FSMContext):
        state = await fsm.get_state()
        return self.state == state
    
class CallbackFilter(FilterObj):
    def __init__(self, payload: str):
        self.payload = payload

    def __call__(self, callback: Callback):
        return self.payload == callback.payload



    

    
