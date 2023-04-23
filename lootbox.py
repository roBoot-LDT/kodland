import os
import discord
from discord.ext import commands
from random import randint, choice

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)

points = 0
temp_points = 0

@bot.command('show')
async def show(ctx):
    global points
    number = randint(0, 10)
    if number > 7:
        points *= 2
        await ctx.send(f'Набранное кол-во очков {points}')
    else:
        points = 0
        await ctx.send('Все сгорело (( ')


@bot.command('play')
async def play(ctx):
    global points
    if points >= 5:
        points -= 5
        img_name = choice(os.listdir('images'))
        with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
        if 'normal' in img_name:
            await ctx.send('Обычное изображение')   
        if 'rare' in img_name:
            await ctx.send('Редкое изображение')
        if 'unique' in img_name:
            await ctx.send('Очень редкое изображение')
        await ctx.send(file=picture)
        return
    await ctx.send('Не достаточно очков')


@bot.command('dice')
async def dice(ctx):
    global points
    points += randint(1, 4)
    await ctx.send(f'Кол-во очков {points}')


@bot.command('guess_number')
async def guess_number(ctx, guess):
    global points
    guess = int(guess)
    number = randint(0, 10)
    await ctx.send(f'Загаданное число {number}')
    if number == guess:
        points += 10
    else:
        points += 10 - abs(int(number - guess))
    await ctx.send(f'Кол-во очков {points}')


@bot.command('twenty_one')
async def twenty_one(ctx, end=None):
    global temp_points, points
    if end == 'stop':
        if temp_points > 21:
            temp_points = 0
            await ctx.send(f'Ничего в итоге не набрано')
        else:
            points += temp_points
            await ctx.send(f'Кол-во очков {points}')
            temp_points = 0
        return
    temp_points += randint(0, 10)
    await ctx.send(f'Кол-во очков набрано {temp_points}')


bot.run('MTAyMDk0NTcwMDgxNDU5NDA0OA.G1-RVl.scgDJrYE1RCa3eHLZcFQcz_Vkh6x8Qk7t7l4Xg')
