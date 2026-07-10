from typing import TYPE_CHECKING

from ..http_client import client
from ..logging import logger
from ..types.button import Button

if TYPE_CHECKING:
    from ..bot import Instai

async def send_buttons_(text: str, buttons: list[Button], bot: Instai, user_id: int):
    if len(buttons) > 3:
        return logger.error(
            "Failed to send buttons: Instagram allows a maximum of 3 buttons per message. "
            f"Received {len(buttons)} buttons.")
    if user_id == bot.my_id:
        return logger.error("You can't send any messages to self")
    
    headers = {
        "Authorization" : f"Bearer {bot.token}",
        "Content-Type" : "application/json"
    }
    content = {
        "recipient":{"id":user_id},
        "message":{
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"button",
                    "text":text,
                    "buttons":[button._to_json() for button in buttons]
                        }
                }
            }
        }
    response = await client.post(f"https://graph.instagram.com/v25.0/{bot.my_id}/messages",
                    json=content, headers=headers)
    if response.is_error:
        if response.is_error:
            logger.error(f"Error in send_buttons {response.json()}")