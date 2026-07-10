from typing import Callable
import inspect
from inspect import Parameter

from .types.dependencies import DEPENDENCIES, DependenciesT
from .types.content_type import ContentType
from .fsm.fsmcontext import FSMContext

class Injector:

    @classmethod
    def _is_p_or_k(cls, param: Parameter):
        return param.kind == Parameter.POSITIONAL_OR_KEYWORD
    
    def _resolve_dp(
        self,
        content: ContentType,
        fsmcontext: FSMContext,
        param: Parameter,
        kwargs: dict):

        dp_value = None
        
        if param.annotation is FSMContext:
            dp_value = fsmcontext
        else:
            dp_value = content
        dp_name = param.name
        kwargs[dp_name] = dp_value

    def resolve(
        self,
        func: Callable,
        content: ContentType,
        fsmcontext: FSMContext):

        sig = inspect.signature(func)
        kwargs: dict[str, DependenciesT] = dict()
        for param in sig.parameters.values():

            if (
            param.annotation in DEPENDENCIES
            and self._is_p_or_k(param)
            ):
                self._resolve_dp(
                    content,
                    fsmcontext,
                    param,
                    kwargs)
        return kwargs