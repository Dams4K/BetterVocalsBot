import json
import typing

class _References:
    BOT_PATH: str = "datas/bot.json"
    # BETA_GUILDS_PATH: str = "datas/beta_guilds.json"

    BOT_ID: int
    BOT_TOKEN: str
    BOT_PREFIX: str
    VERSION: str
    VERSION_TYPE: str
    AUTHORS_ID: typing.List[int]
    COGS_FOLDER: str

    BETA_GUILDS: typing.List[int]

    def __init__(self) -> None:
        with open(self.BOT_PATH, "r") as f:
            data = json.load(f)
            
            self.BOT_ID = data["id"]
            self.BOT_TOKEN = data["token"]
            self.BOT_PREFIX = data["default_prefix"]
            self.VERSION = data["version"]
            self.VERSION_TYPE = data["version_type"]
            self.AUTHORS_ID = data["authors_id"]
            self.COGS_FOLDER = data["cogs_folder"]

References: _References = _References()