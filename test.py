import pickle
from discord.ext import commands
from random import choice
import discord

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)

with open('/home/roboot/Downloads/anecs.pickle', 'rb') as f:
    anecs = pickle.load(f)


@bot.command('cat')
async def cat(ctx):
    '''По команде $cat возвращает категории списком'''
    await ctx.send('\n'.join(anecs.keys()))


@bot.command('rand')
async def rand(ctx):
    '''По команде $rand возвращает случайный анекдот'''
    cat = choice(list(anecs.keys()))
    anec = choice(anecs[cat])
    await ctx.send(anec)


@bot.command('anek')
async def anek(ctx, cat):
    '''По команде $anek {категория} возвращает случайный анекдот из выбранной категории'''
    anec = choice(anecs[cat])
    await ctx.send(anec)


bot.run('MTAyMDk0NTcwMDgxNDU5NDA0OA.GE7PkA.6bBmB5V_RC2eFDdC-DVwmsVj6sh4SvUy-I-SZQ')
