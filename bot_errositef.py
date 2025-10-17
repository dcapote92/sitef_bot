# developed by @dcapote92

from telebot import TeleBot as tbot
from os import getenv
from errors import errors

token = getenv('BOT_TOKEN')
bot = tbot(token)

options = {
    'descricao' : '\nDescrição ⚠️:  ',
    'acao' : '\nAção: ',
    'retentativa_sim' : '\nPermite Retentativa: 👍',
    'retentativa_nao' : '\nPermite Retentativa: 👎'
}


@bot.message_handler(commands=['iniciar','start'])
def send_welcome(message):
    bot.reply_to(message, 'Bem-vindo, esse nosso bot da T.I chegou para facilitar a nossa vida!\nPara começar digite o código do erro que aparece na tela do PDV.')

@bot.message_handler(func=lambda message:'00')
def send_message(message):
    if message.text in errors:
        error_description, to_do, allow_retry = errors[message.text]
        retry_status = options['retentativa_sim'] if allow_retry else options['retentativa_nao']
        final_message = f'Código: {message.text}{options['descricao']}{error_description}{options['acao']}{to_do}{retry_status}'
        bot.reply_to(message, final_message)

bot.infinity_polling()
