from typing import TYPE_CHECKING

from ..http_client import client
from ..types.card import Card
from ..logging import logger

if TYPE_CHECKING:
    from ..bot import Instai

async def send_cards_(cards: list[Card], bot: Instai, user_id: int):
    if user_id == bot.my_id:
        return
    headers = {
        "Authorization" : f"Bearer {bot.token}",
        "Content-Type" : "application/json"
    }
    content = {
    "recipient": {
        "id": user_id},
    "message":{
        "attachment":{
            "type":"template",
            "payload":{
                "template_type":"generic",
                "elements":[card._to_json() for card in cards]
      }
    }
  }
}
    url = f"https://graph.instagram.com/v20.0/{bot.my_id}/messages"
    response = await client.post(
            url=url,
            json=content,
            headers=headers)
    if response.is_error:
        if response.is_error:
            logger.error(f"Error in send_cards {response.json()}")
