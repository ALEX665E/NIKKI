from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "4110592"))
API_HASH = getenv("API_HASH", "aa7c849566922168031b95212860ede0")
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_NAME = getenv("BOT_NAME","🦋͜͡⍣𝐆𝐉𝟓𝟏𝟔✨𝐌𝐔𝐒𝐈𝐂♪➺")
")
BOT_USERNAME = getenv("BOT_USERNAME", "GJ516_vc_player")
OWNER_USERNAME = getenv("OWNER_USERNAME", "export_gabbar")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "ADVENTURE_FAMILYS")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://telegra.ph/file/db8765da6945e3c9333e6.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/db8765da6945e3c9333e6.jpg")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5505750225").split()))
