from typing import Any

from .button import Button
from .action import Action
from ..logging import logger

class Card:
    title: str
    image_url: str | None
    subtitle: str | None
    action: Action | None
    buttons: list[Button] | None

    def __init__(
        self,
        *,
        title: str,
        image_url: str | None = None,
        subtitle: str | None = None,
        action: Action | None = None,
        buttons: list[Button] | None = None):

        if (
        not subtitle
        and not action
        and not buttons):
            return logger.error("Card must have at least one of: subtitle, default_action, or buttons")
            
        if buttons and len(buttons) > 3:
            return logger.error(f"Max len of buttons per one card is 3, but {len(buttons)} was given")
        
        self.title = title
        self.image_url = image_url
        self.subtitle = subtitle
        self.action = action
        self.buttons = buttons

    def _to_json(self):
        base: dict[str, Any] =  {"title" : self.title}
        if self.image_url:
            base.update({"image_url" : self.image_url})
        if self.subtitle:
            base.update({"subtitle" : self.subtitle})
        if self.action:
            base.update({"default_action" : self.action._to_json()})
        if self.buttons:
            base.update({
                "buttons" : [button._to_json() for button in self.buttons]
            })
        return base