from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import MUST_JOIN_CHANNEL

# Private channel details
PRIVATE_CHANNEL_ID =  -1003972430511
PRIVATE_CHANNEL_LINK = "https://t.me/+qBOMK-vel0thNWZl"
PRIVATE_CHANNEL_ID2 =  -1003972430511

BOTUSER = "TeleVaultSvsBot"
# Welcome text with HTML formatting
WELCOME_TEXT = ("<b>Access Restricted</b>\n\n<b><u>You must join our channel to use this bot.
</u></b>\n\n 1.<u><i>Tap Join Channel</i></u>\n2.<u></i>Tap I've Joined to verify</i></u>")



async def check_join(client, message: types.Message):
    """
    Check if the user has joined both required channels.
    If not, send the join message and return False.
    """
    try:
        # Public channel check
        member1 = await client.get_chat_member(PRIVATE_CHANNEL_ID2, message.from_user.id)

        # Private channel check
        member2 = await client.get_chat_member(PRIVATE_CHANNEL_ID, message.from_user.id)

        if (member1.status in ["left", "kicked"]) or (member2.status in ["left", "kicked"]):
            await send_join_message(message)
            return False

        return True
    except Exception:
        await send_join_message(message)
        return False


async def send_join_message(message: types.Message):
    """
    Send a message asking the user to join the required channels,
    with inline buttons for both channels in one row and Verify below.
    """
    kb = InlineKeyboardBuilder()

    # First row: both channels
    kb.row(
        types.InlineKeyboardButton(text="📢 𝖴𝗉𝖽𝖺𝗍𝖾𝗌", url=f"https://t.me/+qBOMK-vel0thNWZl"),
        types.InlineKeyboardButton(text="💌 𝖲𝗎𝗉𝗉𝗈𝗋𝗍 ", url=PRIVATE_CHANNEL_LINK)
    )
    kb.row(
         types.InlineKeyboardButton(text="Verify Join ☑️", callback_data="back_main")
    )
        

    

    await message.answer(
        WELCOME_TEXT,
        reply_markup=kb.as_markup(),
        parse_mode="HTML"
    )
