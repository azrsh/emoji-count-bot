import discord

async def count_emoji(guild):
    countDic = {}
    for emoji in guild.emojis:
        countDic.setdefault(str(emoji), 0)
    
    for channel in guild.text_channels:
        try:
            async for message in channel.history(limit=200):
                for reaction in message.reactions:
                    if str(reaction.emoji) in countDic:
                        countDic[str(reaction.emoji)] += reaction.count
        except discord.errors.Forbidden:
            print('Forbidden error : ' + str(channel) + ' channel')

    return countDic