from typing import Protocol, TYPE_CHECKING

from ..methods.send_message import send_message_
from ..methods.send_cards import send_cards_
from .card import Card
from ..logging import logger
from .button import Button
from ..methods.send_buttons import send_buttons_

if TYPE_CHECKING:
    from ..bot import InstaBot

class Content(Protocol):
    bot: InstaBot
    time: int
    id: int
    user_id: int
    my_id: int
    timestamp: int
    is_echo: bool | None

    async def send_message(self, text: str):
        if self.is_echo:
            return
        await send_message_(text, self.bot, self.user_id)

    async def send_cards(self, cards: list[Card]):
        if len(cards) > 10:
            return logger.error(f"Maximum available length of cards is 3, but {len(cards)} was given")
        await send_cards_(cards, self.bot, self.user_id)

    async def send_buttons(self, text: str, buttons: list[Button]):
        await send_buttons_(text, buttons, self.bot, self.user_id)
