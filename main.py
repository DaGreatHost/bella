from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio
from config import BOT_TOKEN

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = await update.message.reply_text(
        "🔞 Join here https://t.me/addlist/6Fswvlhfpy40YTFl for more videos and photos.\n\n*Dapat 18+ ka bago sumali!*",
        parse_mode="Markdown"
    )
    await asyncio.sleep(3)
    try:
        await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=msg.message_id)
    except Exception as e:
        print(f"Failed to delete message: {e}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running... 🚀")
    app.run_polling()
