import logging

from rich.logging import RichHandler
from rich.highlighter import NullHighlighter
from rich.console import Console
from rich.theme import Theme
from rich.style import Style

theme = Theme(
    {
        "logging.time": "white",
        "logging.message": "white",

        "instabot.prefix": Style(
            color="#FFFFFF",
            bgcolor="#BB00FF",
            bold=True,
        ),
    }
)

console = Console(color_system="truecolor", theme=theme)

class InstaBotFormatter(logging.Formatter):
    def __init__(
        self,
        prefix: str = "INSTABOT INFO"
    ):
        super().__init__()
        self.prefix = prefix

    def format(self, record):
        return (
            f"[instabot.prefix] {self.prefix} [/instabot.prefix] | "
            f"{record.getMessage()}"
        )

rich_handler = RichHandler(
    highlighter=NullHighlighter(),
    omit_repeated_times=False,
    markup=True,
    console=console,
    show_time=True,
    show_level=False,
    show_path=False
)

rich_handler.setFormatter(
    InstaBotFormatter(
        prefix="INSTABOT INFO"
    )
)


def create_logger():
    logger = logging.getLogger("instagram.api")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        logger.addHandler(rich_handler)

    return logger


logger = create_logger()