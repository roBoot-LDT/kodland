import discord
from discord.ext import commands
import os, random

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('/home/roboot/kodland/discord/images')) 
    with open(f'{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
bot.run('MTAyMDk0NTcwMDgxNDU5NDA0OA.G5Gjxz.i860sD-wsadO97J29W5J9bDlSn-ucBHY0GFVKo')
