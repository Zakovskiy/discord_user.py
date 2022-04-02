__title__ = "discord_user.py"
__author__ = "Zakovskiy"
__license__ = "MIT"
__copyright__ = "Copyright 2020-2022 Zakovskiy"
__version__ = "1.0.0"

from .discord_user import Client

from requests import get
from json import loads

__newest__ = loads(get("https://pypi.python.org/pypi/discord_user.py/json").text)["info"]["version"]

if __version__ != __newest__:
    exit(f"New version of {__title__} available: {__newest__} (Using {__version__})")