import imp
from tokenize import Token
from flask import Flask, request
import telegram
from telebot.config import bot_token,bot_user_name,URL

global bot
global TOKEN 
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

#start the flask app
app = Flask(__name__)



if __name__== '__main__':
    app.run(threaded=True)