from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os

BOT_TOKEN = os.environ.get("8579949777:AAGtbaNwQW8CRp8RIcZfLsb7zjFEb0mI25w")

MOVIES = {
    "avatar": "https://drive.google.com/uc?export=download&id=FILE_ID_1",
    "titanic": "https://drive.google.com/uc?export=download&id=FILE_ID_2"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎬 Movie Download Bot\n\nMovie name লিখুন"
    )

async def search_movie(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.message.text.lower()
    if name in MOVIES:
        await update.message.reply_text(f"⬇ Download:\n{MOVIES[name]}")
    else:
        await update.message.reply_text("❌ Movie পাওয়া যায়নি")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_movie))

app.run_polling()
