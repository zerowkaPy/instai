from typing import Any

class MessagingT:
    sender_id: int
    recipient_id: int
    timestamp: int
    message: dict[str, Any] | None
    postback: dict[str, Any] | None

    def __init__(
        self,
        *,
        sender_id: int,
        recipient_id: int,
        timestamp: int,
        message: dict[str, Any] | None = None,
        postback: dict[str, Any] | None = None):

        self.sender_id = sender_id
        self.recipient_id = recipient_id
        self.timestamp = timestamp
        self.message = message
        self.postback = postback