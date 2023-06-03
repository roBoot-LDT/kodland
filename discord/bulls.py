import discord
from botSettings import TOKEN
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
###################################ВЫШЕ НЕ ТРОГАТЬ#######################################################
#########################################################################################################
    if message.author == client.user:
        return
    if message.content.startswith("Экология") or message.content.startswith("Загрязнение") or message.content.startswith("экология") or message.content.startswith("загрязнение"):
        if "Земля" in message.content or "земля" in message.content:
            await message.channel.send('1. Предотвращение загрязнения почвы')
            await message.channel.send('2. Очистка почвы от токсичных веществ')
            await message.channel.send('3. Предотвращение эрозии')
            await message.channel.send("*А вот сайт для универсального решения проблем с экологией:* https://wiki.fenix.help/ekologiya/puti-resheniya-yekologicheskih-problem")
        elif "Воздух" in message.content or "воздух" in message.content:
            await message.channel.send('1.  Перевести фабрики на электро движки.')
            await message.channel.send('2.  чтобы из них не выробатывались отходы и газы.')
            await message.channel.send("*А вот сайт для универсального решения проблем с экологией:* https://wiki.fenix.help/ekologiya/puti-resheniya-yekologicheskih-problem")
        elif "Вода" in message.content or "вода" in message.content:
            await message.channel.send('1. Очистка сточных вод.')
            await message.channel.send('2. Сокращение пластиковых отходов.')
            await message.channel.send('3. Экономия воды.')
            await message.channel.send("*А вот сайт для универсального решения проблем с экологией:* https://bezotxodov.ru/jekologija/puti-reshenija-zagrjaznenija-vody" )
        elif "Производство" in message.content or "производство" in message.content:
            await message.channel.send('1. Регулирование производства')
            await message.channel.send('2. Совершенствование системы сбора и утилизации отходов')
            await message.channel.send('3. Переработка отходов')
            await message.channel.send("*А вот сайт для универсального решения проблем с экологией:* https://wiki.fenix.help/ekologiya/puti-resheniya-yekologicheskih-problem")
        elif  "Инициативные проекты" in message.content or "инициативные проекты" in message.content:
            await message.channel.send('*А вот сайт с проектами по собственной инициативе* https://национальныепроекты.рф/projects/ekologiya')
        elif message.content.startswith("Команды экологи"):
            await message.channel.send('Производство')
            await message.channel.send('Вода')
            await message.channel.send('Земля')
            await message.channel.send('Воздух')
            await message.channel.send('Инициативные проекты')
        else:
            await message.channel.send(message.content)
    
client.run(TOKEN)           
# internal free link 

# [[https://wiki.fenix.help/ekologiya/puti-resheniya-yekologicheskih-problem]]
# [[https://wika.tutoronline.ru/geografiya/class/9/ekologicheskie-problemy]]
# [[https://ludirosta.ru/post/resheniya-problem-ekologii_2146]]
# [[https://национальныепроекты.рф/projects/ekologiya]]
