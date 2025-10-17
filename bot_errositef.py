# developed by @dcapote92

from telebot import TeleBot as tbot
from erros import erros

bot = tbot('8453280249:AAHoPzyFxUZinr-Qf9FwBeuUClsOUPf6AOk')

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
    '''for e in erros.keys():
        if message.text == e:
            bot.reply_to(message,erros[e])'''
    if message.text in erros:
        descricao_erro, acao_erro, permite_retentativa = erros[message.text]
        retentativa_status = options['retentativa_sim'] if permite_retentativa else options['retentativa_nao']
        final_message = f'Código: {message.text}{options['descricao']}{descricao_erro}{options['acao']}{acao_erro}{retentativa_status}'
        bot.reply_to(message, final_message)

bot.infinity_polling()
