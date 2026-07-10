from typing import TYPE_CHECKING

from ..http_client import client
from ..logging import logger

if TYPE_CHECKING:
    from ..bot import Instai

async def send_message_(text: str, bot: Instai, user_id: int):
    if user_id == bot.my_id:
        return
    headers = {
        "Authorization" : f"Bearer {bot.token}",
        "Content-Type" : "application/json"
    }
    content = {
    "recipient": {
        "id": user_id},
    "message" : {
        "text" : text
    }
    }
    response = await client.post(f"https://graph.instagram.com/v25.0/{bot.my_id}/messages",
                    json=content, headers=headers)
    if response.is_error:
        if response.is_error:
            logger.error(f"Error in send_message {response.json()}")