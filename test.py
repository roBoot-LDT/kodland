import discord
import requests

client = discord.Client()

TOKEN = 'ТОКЕН'
API_URL = 'https://7015.deeppavlov.ai/model'


def request_sentiment(message):
    data = {'x': [message]}
    res = requests.post(API_URL, json=data).json()
    santiment = res[0][0]
    return santiment


@client.event
async def on_message(message):
    # В случае, если автором сообщения является бот,
    # мы не отвечаем. Иначе бот будет разговаривать сам с собой
    if message.author == client.user:
        return

    setiment = request_sentiment(message.content)
    await message.channel.send(setiment)

client.run(TOKEN)
