
async def count_emoji(guild):
    countDic = {}
    for emoji in guild.emojis:
        countDic.setdefault(str(emoji), 0)
    
    for channel in guild.text_channels:
        async for message in channel.history(limit=200):
            for reaction in message.reactions:
                if reaction.custom_emoji:
                    countDic[str(reaction.emoji)] += reaction.count
    
    return countDic