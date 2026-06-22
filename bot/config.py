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
ADMIN_IDS = [int(i) for i in _getenv("ADMIN_IDS", "8619127196", required=True).replace(" ", "").split(",") if i]
API_ID = "37313295"
API_HASH = "1f050e79d114ec31c85dc54a4d9b8cb7"

DATABASE_URL = _getenv("DATABASE_URL")
MONGO_URI = "mongodb+srv://TeleVault:TeleVault@televault.6kr2f9n.mongodb.net"


DEFAULT_CURRENCY = _getenv("DEFAULT_CURRENCY", "₹")
MIN_BALANCE_REQUIRED = float(_getenv("MIN_BALANCE_REQUIRED", "0"))
