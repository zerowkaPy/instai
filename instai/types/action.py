from typing import Literal

class Action:
    action_type: Literal["web_url"] = "web_url"
    url: str

    def __init__(self, url: str):
        self.url = url
    
    def _to_json(self):
        return {
            "type" : self.action_type,
            "url" : self.url
        }