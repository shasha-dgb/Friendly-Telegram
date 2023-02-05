__version__ = (1, 1, 0)

# 🔒 Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html


# meta developer: ✨ Remaked by @yumakamods
# scope: hikka_only
# scope: hikka_min 1.3.0

from .. import loader, utils
from asyncio import sleep 

class TikDownBotMod(loader.Module):
    """Install videos for tiktok with link"""
    
    strings = {
        "name": "TikTok Dowlander",
        "yumaka_pls_wait": "🕒 <code>Wait...</code>",
        "yumaka_pls_enter_a_link": "🍁 <b>Please provide a link for the TikTok video</b>",
        "yumaka_done": "✅ <b>Done!</b>",
        }
    
    strings_ru = {
        "yumaka_pls_wait": "🕒 <code>Пожалуйста подождите...</code>",
        "yumaka_pls_enter_a_link": "🍁 <b>Пожалуйста, дайте ссылку на видео TikTok</b>",
        "yumaka_done": "✅ <b>Готовo!",
        }
    
    strings_uz = {
        "yumaka_pls_wait": "🕒 <b>Iltimos, kuting...</b>",
        "yumaka_pls_enter_a_link": "🍁 <b>Iltimos, TikTok uchun havolani ko'rsating</b>",
        "yumaka_done": "✅ <b>Tayyor!",
        }

    async def tiktokcmd(self, message):
        """> [Link] just enter the link for the video"""
        reply = await message.get_reply_message() 
        await utils.answer(message, self.strings("yumaka_pls_wait", message))
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings("yumaka_pls_enter_a_link", message))
            return
        r = await message.client.inline_query('tikdobot', args)
        await message.client.send_file(message.to_id, r[1].result.content.url, caption=f"{self.strings('yumaka_done')} | <code>{args}</code>", reply_to=reply.id if reply else None)
        
