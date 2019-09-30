import telebot
import sqlite3
from sqlite3 import Error
import os.path
import requests
import sys

API_TOKEN = "YOURTOKEN" # HERE IS YOUR TOKEN
bot = telebot.TeleBot(API_TOKEN) # connect bot to your token

def create_or_open_db(db_file): # def function
    db_is_new = not os.path.exists(db_file) # check does db exists
    conn = sqlite3.connect(db_file)         # connect or create db
    if db_is_new:
        print('Creating schema')
        sql = '''create table if not exists AUDIO(
        UID INTEGER,
        AUDIOS TEXT);''' # make prepare query 
        conn.execute(sql) # shortcut for conn.cursor().execute(sql)
    else:
        print('Schema exists')
    return conn

conn = create_or_open_db('audio.db') # open or create db
conn = sqlite3.connect('audio.db') # connect to db
c = conn.cursor()

@bot.message_handler(content_types=['voice']) # handle all voice message
def handle_docs_audio(message):
    if message.chat.type == 'group': # check type message, ignore all message that isn't groupmessage
            conn = create_or_open_db('audio.db') # open or create db
            conn = sqlite3.connect('audio.db') # connect to db
            c = conn.cursor()
            raw = message.voice.file_id # get voice file id
            uid = message.from_user.id # get id of user 
            path = raw+".ogg" # for voice file
            file_info = bot.get_file(raw) # get file from id
            downloaded_file = bot.download_file(file_info.file_path) # download file
            with open(path,'wb') as new_file: # save file
                new_file.write(downloaded_file)  
            realpath = os.path.realpath(path) # get current path for saved voice file
            c.execute("INSERT INTO AUDIO (UID, AUDIOS) VALUES (?,?)", (uid, realpath)) # insert user id and path to voice file into db 
            conn.commit()
bot.polling() # make bot running