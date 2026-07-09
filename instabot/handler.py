from typing import Callable, Any
import inspect

from .filters import FilterObj
from .injector import Injector
from .types.content_type import ContentType
from .fsm.fsmcontext import FSMContext

injector = Injector()

class HandlerObject:
    def __init__(self, callback: Callable, *filters: FilterObj):
        self.callback = callback
        self.filters = filters
    
    async def execute_filters(
        self,
        content: ContentType,
        fsmcontext: FSMContext) -> bool:

        for filter in self.filters:
            kwargs = injector.resolve(
                filter,
                content,
                fsmcontext)
            result = filter(**kwargs)
            if inspect.isawaitable(result):
                result = await result
            if not result:
                return False
        return True
    
    async def execute(
        self,
        content: ContentType,
        fsmcontext: FSMContext) -> Any:

        kwargs = injector.resolve(
            self.callback,
            content,
            fsmcontext)
        coro = self.callback(**kwargs)
        return await coro