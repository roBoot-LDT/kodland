import discord
from discord.ext import commands
from botSettings import TOKEN
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx, asjkfjd = 5): 
    await ctx.send(f'Привет! Я бот {bot.user}!' * asjkfjd)

@bot.command()          
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run(TOKEN)
