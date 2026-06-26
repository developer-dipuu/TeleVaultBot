#---------- © sᴛᴀʟᴋᴇʀ@hehe_stalker
#---------- ᴘʀᴏJᴇᴄᴛ - ᴛᴇʟᴇɢʀᴀᴍ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛ sᴇʟʟɪɴɢ ʙᴏᴛ
#-------------------------------------------------------
import os
from dotenv import load_dotenv

load_dotenv()

def _getenv(name: str, default: str | None = None, required: bool = False) -> str:
    val = os.getenv(name, default)
    if required and (val is None or val == ""):
        raise RuntimeError(f"Missing required env var: {name}")
    return val
    
MUST_JOIN_CHANNEL = "-1003972430511"
BOT_TOKEN = _getenv("BOT_TOKEN", "8846137972:AAGYolSduNzMPEmEmZtkdl6L-4kvBkq-4ic")
ADMIN_IDS = [int(i) for i in _getenv("ADMIN_IDS", "740397179", required=True).replace(" ", "").split(",") if i]
API_ID = "32660355"
API_HASH = "c01207b248ac94963597c2158d72d613"

DATABASE_URL = _getenv("DATABASE_URL")
MONGO_URI = "mongodb+srv://TeleVault:TeleVault@televault.6kr2f9n.mongodb.net"


DEFAULT_CURRENCY = _getenv("DEFAULT_CURRENCY", "₹")
MIN_BALANCE_REQUIRED = float(_getenv("MIN_BALANCE_REQUIRED", "0"))
