from typing import Union

from .message import Message
from ..fsm import FSMContext
from .callback import Callback


DependenciesT = Union[Message | Callback]

DEPENDENCIES = (
    FSMContext,
    Message,
    Callback
)
