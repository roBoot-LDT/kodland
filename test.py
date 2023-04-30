import time
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from discord.ext import commands
import discord
profile1 = 'Light_coloured'
player1 = 'Cucumber'
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command('networth')
async def on_ctx(ctx):
    global player, profile
    driver = webdriver.Chrome(ChromeDriverManager().install())
    url = f"https://spillager.live/skyblock/networth/{player1}/{profile1}" #Light_coloured #Cucumber 
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, features="lxml")
    main = soup.find(class_='overview_element_value mt-2')
    await ctx.send(main.text)
@bot.command('player')
async def on_ctx(ctx):
    global player1
    player1 = ctx.author
    await ctx.send('yes')
@bot.command('profile')
async def on_ctx(ctx):
    global profile1
    profile1 = ctx.author
    await ctx.send('yes')
    

bot.run('')
