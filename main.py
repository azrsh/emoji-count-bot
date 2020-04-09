import discord
import bottoken


client = discord.Client()

@client.event
async def on_ready():
    print('login')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/count-emoji':
        await count_emoji(message.guild, message.channel)

async def count_emoji(guild, notification_channel):
    countDic = {}
    for emoji in guild.emojis:
        countDic.setdefault(str(emoji), 0)
    
    for channel in guild.text_channels:
        async for message in channel.history(limit=200):
            for reaction in message.reactions:
                if reaction.custom_emoji:
                    countDic[str(reaction.emoji)] += reaction.count
    
    await notification_channel.send(countDic)



client.run(bottoken.get_token())