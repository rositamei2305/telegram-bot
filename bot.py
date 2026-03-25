from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes

TOKEN = "8669248066:AAHASeirCyS7px8uabDIUrg-lYhusoDzlJY"

AUTO_MESSAGE = """Hiện tại kênh tele của Mây 𝐜𝐢̉ 𝐭𝐢𝐞̂́𝐩 𝐧𝐡𝐚̣̂𝐧 𝐭𝐡𝐨̂𝐧𝐠 𝐭𝐢𝐧 𝐥𝐚̀𝐦 𝐦𝐢𝐱𝐬𝐞𝐭 𝐭𝐡𝐞𝐨 𝐲𝐞̂𝐮 𝐜𝐚̂̀𝐮, mọi liên hệ không nhằm mục đích giao dịch đặt nhạc sẽ chưa thể 
phản hồi ngay bây giờ.
Nếu có nhu cầu đặt mixset style 𝐇𝐨𝐮𝐬 / 𝐕𝐁𝐚𝐬𝐬 / 𝐂𝐥𝐮𝐛 / 𝐓𝐞𝐜𝐡 𝐇𝐨𝐮𝐬𝐞 / 𝐌𝐞𝐥𝐨𝐝𝐢𝐜 𝐓𝐞𝐜𝐡𝐧𝐨 Mây sẽ tư vấn cụ thể hơn nha😚
Xin lỗi vì sự bất tiện và cám ơn vì đã quan tâm🥳
_________________________________

Contacts For You: Hà Ngọc Mây (Rosita Mei)
🎶 SoundCloud: https://soundcloud.com/rositamei2305
📥 Facebook: www.facebook.com/rositamei2305/
🎬 Tiktok: www.tiktok.com/@rosita.mei2305
🤳 Telegram: t.me/rositamei03
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(AUTO_MESSAGE)

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(AUTO_MESSAGE)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

app.run_polling()
