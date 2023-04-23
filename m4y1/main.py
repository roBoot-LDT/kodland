import os
import requests
import discord
from discord.ext import commands
from random import randint, choice
intents = discord.Intents.all()
client = discord.Client(intents=intents)
API_URL = 'https://7015.deeppavlov.ai/model'
bot = commands.Bot(command_prefix='$', intents=intents)

def request_sentiment(message):
    data = {'x': [message]}
    res = requests.post(API_URL, json=data).json()
    santiment = res[0][0]
    return santiment


@client.event
async def on_message(message):
    if message.author == client.user:
        return
@bot.command('stats')
async def send(ctx):
    d = {}
    with open('sentiment.txt', 'r', encoding='utf-8') as f:
        data = f.read()
        lines = data.split('\n')[:-1]
        for line in lines:
            author = line.split(' ')[0]
            sentiment = line.split(' ')[-1]
            if author in d:
                d[author][sentiment] += 1
            else:
                d[author] = {}
                d[author]['positive'] = 0
                d[author]['neutral'] = 0
                d[author]['negative'] = 0
        for author in d:
            for sentiment in d[author]:
                await ctx.send(author, sentiment, d[author][sentiment])
                # print(author, sentiment, d[author][sentiment])
    sentiment = request_sentiment(ctx.content)
    with open('sentiment.txt', 'a', encoding='utf-8') as f:
        f.write(f'{ctx.author} {ctx.content} {sentiment}\n')
client.run("MTAyMDk0NTcwMDgxNDU5NDA0OA.Ge9NUF.7zET8xJ6QzLc2-rY-ROoVodfwMelYxgjwc9MTA")
bot.run("MTAyMDk0NTcwMDgxNDU5NDA0OA.Ge9NUF.7zET8xJ6QzLc2-rY-ROoVodfwMelYxgjwc9MTA")
