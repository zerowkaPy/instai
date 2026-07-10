from typing import Any

class WebhookT:
    entry: dict[str, Any]
    time: int
    id: int
    messaging: dict[str, Any] | None

    def __init__(
        self,
        *,
        entry: dict[str, Any],
        time: int,
        id: int,
        messaging: dict[str, Any] | None = None):

        self.entry = entry
        self.time = time
        self.id = id
        self.messaging = messaging