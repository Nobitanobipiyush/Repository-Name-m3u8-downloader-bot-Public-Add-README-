import os
from telegram.ext import Updater,CommandHandler
from downloader import download_m3u8_to_mp4

TOKEN=os.getenv("TELEGRAM_TOKEN")

def start(update,context):
    update.message.reply_text("Send /download <m3u8 link>")

def download(update,context):
    url=context.args[0]
    update.message.reply_text("Downloading...")
    file=download_m3u8_to_mp4(url)
    update.message.reply_document(open(file,"rb"))

updater=Updater(TOKEN,use_context=True)
dp=updater.dispatcher

dp.add_handler(CommandHandler("start",start))
dp.add_handler(CommandHandler("download",download))

updater.start_polling()
updater.idle()
