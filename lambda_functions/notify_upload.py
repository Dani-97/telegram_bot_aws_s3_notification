import configparser
import json
import requests
import telebot

def send_message(message):
    config = configparser.ConfigParser()
    config.read('config.cfg')

    TOKEN = config['BOT']['token']
    CHAT_ID = config['BOT']['chat_id']

    bot = telebot.TeleBot(TOKEN, parse_mode='HTML')
    bot.send_message(CHAT_ID, message)

def lambda_handler(event, context):
    uploaded_file_name = str(event['Records'][0]['s3']['object']['key'])
    bucket_name = str(event['Records'][0]['s3']['bucket']['name'])
    message = f'The file <b>{uploaded_file_name}</b> has been uploaded to the bucket <b>{bucket_name}</b>'
    send_message(message)
