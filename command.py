import discord
import bottoken
import emojicnt
import dic2text

client = discord.Client()

@client.event
async def on_ready():
    print('login')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/count-emoji':
        result = await emojicnt.count_emoji(message.guild)
        text = 'Count Result\n' + dic2text.convert(result)
        await message.channel.send(text)

client.run(bottoken.get_token())