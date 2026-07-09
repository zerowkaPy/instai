from typing import TYPE_CHECKING

from .content import Content

if TYPE_CHECKING:
    from ..bot import InstaBot
    
class Message(Content):
    bot: InstaBot
    time: int
    id: int
    user_id: int
    my_id: int
    timestamp: int
    mid: str
    text: str | None
    is_echo: bool | None

    def __init__(
        self,
        *,
        bot: InstaBot,
        time: int,
        id: int,
        user_id: int,
        my_id: int,
        timestamp: int,
        mid: str,
        text: str | None = None,
        is_echo: bool | None = None):
        
        self.bot = bot
        self.time = time
        self.id = id
        self.user_id = user_id
        self.my_id = my_id
        self.timestamp = timestamp
        self.mid = mid
        self.text = text
        self.is_echo = is_echo

    def __str__(self):
        return "Message"
    
    def __repr__(self):
        return f"Message(text={self.text}, user_id={self.user_id}, is_echo={self.is_echo})"
