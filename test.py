import discord
import requests

intents = discord.Intents.all()
client = discord.Client(intents=intents)

TOKEN = ''
API_URL = 'https://7015.deeppavlov.ai/model'


def request_sentiment(message):
    data = {'x': [message]}
    res = requests.post(API_URL, json=data).json()
    santiment = res[0][0]
    return santiment


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    setiment = request_sentiment(message.content)
    if setiment == "negative":
        await message.channel.send('Bad')

client.run(TOKEN)
