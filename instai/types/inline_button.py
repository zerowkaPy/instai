from typing import Literal, Any

from .button_base import ButtonBase

class InlineButton(ButtonBase):
    button_type: Literal["postback"] = "postback"

    def __init__(
        self,
        *,
        text: str,
        payload: str):

        self.text = text
        self.payload = payload
    
    def _to_json(self) -> dict[str, Any]:
        return {
            "type" : self.button_type,
            "title" : self.text,
            "payload" : self.payload
        }