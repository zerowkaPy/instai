from typing import Any, Callable

from ..bot import InstaBot
from ..parser.parser import WebhookParser
from ..filters import FilterObj
from ..handler import HandlerObject
from ..types.message import Message
from ..types.callback import Callback
from ..types.content_type import ContentType
from ..fsm.fsmcontext import FSMContext
from ..logging import logger

class Dispatcher:

    def __init__(self, bot: InstaBot):
        self.bot = bot
        self.messages_handlers: list[HandlerObject] = []
        self.callback_handlers: list[HandlerObject] = []
        self.parser = WebhookParser()
        self.locked = False

        logger.info("Bot is ready to accept webhooks.")

    def _register_message(self, callback: Callable, *filters: FilterObj):
        handler = HandlerObject(callback, *filters)
        self.messages_handlers.append(
            handler)
        
    def _register_callback(self, callback: Callable, *filters: FilterObj):
        handler = HandlerObject(callback, *filters)
        self.callback_handlers.append(
            handler)

    def message(self, *filters):
        def wrapper(callback: Callable):
            self._register_message(callback, *filters)
            return callback
        return wrapper
    
    def callback(self, *filters):
        def wrapper(callback: Callable):
            self._register_callback(callback, *filters)
            return callback
        return wrapper
    
    async def _process_update(
        self,
        content: ContentType,
        fsmcontext: FSMContext):

        if isinstance(content, Message):
            handlers = self.messages_handlers
        elif isinstance(content, Callback):
            handlers = self.callback_handlers
        else:
            handlers = []
        
        for handler in handlers:
            check_filter = await handler.execute_filters(content, fsmcontext)
            if check_filter:
                if await fsmcontext._status_permission(handler.callback):
                    await handler.execute(content, fsmcontext)
                    return logger.info(f"update {str(content)} id {content.id} is handled user_id={content.user_id} bot_id={self.bot.my_id}")
        return logger.info(f"update {content.id} is not handled user_id={content.user_id} bot_id={self.bot.my_id}")
                

    async def feed_update(self, request: dict[str, Any]):
        parser = self.parser
        content = parser.resolve(self.bot, request)
        if content is None:
            return logger.error("update was not parsed correctly")
        if content.is_echo:
            return logger.info(f"echo update\U0001F634 {content.id} user_id {content.user_id} bot_id {self.bot.my_id}")
        fsmcontext = FSMContext(self.bot.storage.client, content.user_id)
        await self._process_update(content, fsmcontext)