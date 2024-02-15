import os


class Mody(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 26983509)

    API_HASH = os.environ.get("API_HASH", "ab5d4207ca2212869822f58afee6be9e")
    
    USER_NAME = os.environ.get("USER_NAME", "")
    
    SESSION = os.environ.get("SESSION", "")

    BOT_USER = os.environ.get("BOT_USER", "")

    VIA_USER = os.environ.get("VIA_USER", "")

    MENTION = os.environ.get("MENTION", "")
