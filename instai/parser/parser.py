from typing import Any, TYPE_CHECKING

from ..types.content_type import ContentType
from ..types.message import Message
from ..types.webhook import WebhookT
from ..types.messaging import MessagingT
from ..types.callback import Callback

class WebhookParser:
    if TYPE_CHECKING:
        from ..bot import Instai
        bot: Instai

    @classmethod
    def _resolve_postback(
        cls,
        *,
        bot: Instai,
        postback: dict[str, Any],
        webhook: WebhookT,
        messaging: MessagingT):

        mid = postback["mid"]
        title = postback.get("title")
        payload = postback.get("payload")
        is_echo = postback.get("is_echo")

        return Callback(
            bot=bot,
            time=webhook.time,
            id=webhook.id,
            user_id=messaging.sender_id,
            my_id=messaging.recipient_id,
            timestamp=messaging.timestamp,
            mid=mid,
            text=title,
            payload=payload,
            is_echo=is_echo)

    @classmethod
    def _resolve_message(
        cls,
        *,
        bot: Instai,
        message: dict[str, Any],
        webhook: WebhookT,
        messaging: MessagingT) -> Message:

        mid = message["mid"]
        text = message.get("text")
        is_echo = message.get("is_echo")
        
        return Message(
            bot=bot,
            time=webhook.time,
            id=webhook.id,
            user_id=messaging.sender_id,
            my_id=messaging.recipient_id,
            timestamp=messaging.timestamp,
            mid=mid,
            text=text,
            is_echo=is_echo)
    
    @classmethod
    def _resolve_messaging(cls, messaging: dict[str, Any]) -> MessagingT:
        sender_id = messaging["sender"]["id"]
        recipient_id = messaging["recipient"]["id"]
        timestamp = messaging["timestamp"]
        message = messaging.get("message")
        postback = messaging.get("postback") 

        parsed_messaging = MessagingT(
            sender_id=sender_id,
            recipient_id=recipient_id,
            timestamp=timestamp)
        if message:
            parsed_messaging.message = message
        elif postback:
            parsed_messaging.postback = postback
        return parsed_messaging

    
    @classmethod 
    def _resolve_webhook(cls, request: dict[str, Any]) -> WebhookT | None:
        entry: dict[str, Any] = request["entry"][0]
        id = entry["id"]
        time = entry["time"]

        if entry.get("messaging"):
            messaging = entry["messaging"][0]
            return WebhookT(
                entry=entry,
                id=id,
                time=time,
                messaging=messaging)
    
    @classmethod
    def resolve(cls, bot: Instai, request: dict[str, Any]) -> ContentType | None:
        webhook = cls._resolve_webhook(request)
        if webhook:
            if webhook.messaging:
                messaging = cls._resolve_messaging(webhook.messaging)
                if messaging.message:
                    message = cls._resolve_message(
                        bot=bot,
                        message=messaging.message,
                        webhook=webhook,
                        messaging=messaging)
                    return message
                elif messaging.postback:
                    callback = cls._resolve_postback(
                        bot=bot,
                        postback=messaging.postback,
                        webhook=webhook,
                        messaging=messaging)
                    return callback
            return None
        else:
            return None
