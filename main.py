import telebot
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config import TOKEN, SERVICE_ACCOUNT_FILE, SPREADSHEET_URL
from keep_alive import keep_alive

bot = telebot.TeleBot(TOKEN)

scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, scope)
client = gspread.authorize(creds)
sheet = client.open_by_url(SPREADSHEET_URL).sheet1

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🤖 Swapnil Bot सुरू झाला! आता तू command पाठवू शकतोस ✅")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    sheet.append_row([message.chat.id, message.text])
    bot.reply_to(message, f"📩 तुझं मेसेज Sheet मध्ये add झालं!")

keep_alive()
bot.polling()
