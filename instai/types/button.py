from typing import Union

from .link_button import LinkButton
from .inline_button import InlineButton

Button = Union[LinkButton, InlineButton]