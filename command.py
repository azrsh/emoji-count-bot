import discord
import bottoken
import emojicnt


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
        await message.channel.send(result)

client.run(bottoken.get_token())