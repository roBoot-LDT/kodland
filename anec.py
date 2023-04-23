import pickle
from discord.ext import commands
from random import choice

bot = commands.Bot(command_prefix='$')

with open('anecs.pickle', 'rb') as f:
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


bot.run('ТОКЕН')
