from ..fsm.fsmcontext import FSMContext
from ..types.bot_status import OPEN, CLOSED

import inspect
from typing import Callable, Any


async def anylize_func(
    func: Callable[..., Any],
    fsm: FSMContext):

    sig = inspect.signature(func)
    status = await fsm._get_bot_status()
    flag = False
    for param in sig.parameters.values():
        if param.name == "lock":
            if param.default is True and status != CLOSED:
                flag = True
                await fsm._lock_bot()

        if param.name == "unlock":
            if param.default is True and status != OPEN:
                flag = True
                await fsm._unlock_bot()
    if status == OPEN:
        return True
    
    if not flag:
        return False
    else:
        return True
