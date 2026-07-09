from typing import Literal, Any

from .button_base import ButtonBase

class LinkButton(ButtonBase):
    button_type: Literal["web_url"] = "web_url"
    url: str
    text: str

    def __init__(
        self,
        *,
        url: str,
        text: str):

        self.url = url
        self.text = text

    def _to_json(self) -> dict[str, Any]:
        return {
            "type" : self.button_type,
            "url" : self.url,
            "title" : self.text
        }