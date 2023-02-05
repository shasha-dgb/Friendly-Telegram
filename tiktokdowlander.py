__version__ = (1, 1, 0)

# 🔒 Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html


# meta developer: ✨ Remaked by @yumakamods
# scope: hikka_only
# scope: hikka_min 1.3.0

from .. import loader, utils
from asyncio import sleep 

class TikDownBotMod(loader.Module):
    """Upload video via TikTok link «Optimized»"""
    
    strings = {
        "name": "💾 TikTok Dowlander",
        "wilson_pls_wait": "🕒 <code>Wait...</code>",
        "wilson_pls_enter_a_link": "🍁 <b>Please provide a link for the TikTok video</b>",
        "wilson_done": "✅ <b>Done!</b>",
        }
    
    strings_ru = {
        "wilson_pls_wait": "🕒 <b>Пожалуйста подождите...</b>",
        "wilson_pls_enter_a_link": "🍁 <b>Пожалуйста, дайте ссылку на видео TikTok</b>",
        "wilson_done": "✅ <b>Готов!",
        }
    
    strings_uz = {
        "wilson_pls_wait": "🕒 <b>Iltimos, kuting...</b>",
        "wilson_pls_enter_a_link": "🍁 <b>Iltimos, TikTok uchun havolani ko'rsating</b>",
        "wilson_done": "✅ <b>Tayyor!",
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
        await message.delete()
