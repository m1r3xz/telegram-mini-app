import os
from telegram import Update, WebAppInfo, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Replace with your bot token from BotFather
BOT_TOKEN = "7335268852:AAGCp5SUMHt4jlK2Qu_MSXR3mOqUqKAP2vY"

# Replace with your ngrok URL
WEBAPP_URL = "https://3c9a-185-107-56-72.ngrok-free.app/index.html"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message with a button that opens the web app."""
    button = KeyboardButton(
        text="Open Counter App",
        web_app=WebAppInfo(url=WEBAPP_URL)
    )
    keyboard = ReplyKeyboardMarkup([[button]], resize_keyboard=True)
    await update.message.reply_text(
        "Welcome! Click the button below to open the Counter App:",
        reply_markup=keyboard
    )

async def app(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message with a button that opens the web app."""
    button = KeyboardButton(
        text="Open Counter App",
        web_app=WebAppInfo(url=WEBAPP_URL)
    )
    keyboard = ReplyKeyboardMarkup([[button]], resize_keyboard=True)
    await update.message.reply_text(
        "Click the button below to open the Counter App:",
        reply_markup=keyboard
    )

def main():
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("app", app))

    # Run the bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
