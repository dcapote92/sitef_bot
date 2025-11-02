import asyncio
from textwrap import dedent
from pyrogram import Client, filters, idle
from pyrogram.types import Message
from pyrogram.enums import ParseMode
from os import getenv
from errors import errors


# Need to create an app on my.telegram.org in order to receive API_ID and API_HASH 
API_ID = getenv('ES_API_ID') 
API_HASH = getenv('ES_API_HASH')

# Get your token on both father
BOT_TOKEN = getenv('ES_TOKEN') # process_assistant

# this is justo set a session name ( can be anything)
SESSION_NAME = "bot_session" 


# =========================================================
# Get pyrogram client started
# =========================================================
app = Client( 
    SESSION_NAME,
    api_id=int(API_ID),
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    parse_mode=ParseMode.MARKDOWN
)




@app.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
 
    await message.reply_text(
        dedent(f'''
        Bem-vindo! 
        Esse nosso bot da T.I chegou para facilitar a nossa vida!
        Para começar digite o código do erro que aparece na tela do PDV.'''
        ),
    )

@app.on_message(filters.text)
async def on_sitef_error(client, message):
    if message.text in errors:
        error_description, to_do, allow_retry = errors[message.text]
        
        answer = dedent(f'''
Código 🛑 : {message.text}

Descrição 🔎 :
{error_description}

Ação 🔧 :
{to_do}

{'Permite Retentativa: 👍' if allow_retry else 'Permite Retentativa: 👎'}
'''
        )

        await message.reply_text(
            answer,
        )


if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    
    async def main_pyrogram():
        print("Bot sendo inicializado...")
        await app.start()
        print("Bot rodando. Pressione Ctrl+C para parar.")
        await idle()
        await app.stop()
        print("Bot parou.")

    try:
        loop.run_until_complete(main_pyrogram())
    except KeyboardInterrupt:
        print("\nBot interrompido pelo usuário.")
    except Exception as e:
        print(f"Ocorreu um erro fatal: {e}")

