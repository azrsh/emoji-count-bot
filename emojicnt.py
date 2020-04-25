import discord

async def count_emoji(guild, limit=100, before=None, after=None, around=None, oldest_first=None):
    countDic = {}
    for emoji in guild.emojis:
        countDic.setdefault(str(emoji), 0)
    
    for channel in guild.text_channels:
        try:
            async for message in channel.history(limit=limit, before=before, after=after, around=around, oldest_first=oldest_first):
                if message.author.bot:
                    continue
                for reaction in message.reactions:
                    if str(reaction.emoji) in countDic:
                        countDic[str(reaction.emoji)] += reaction.count
                    #else:
                    #    countDic.setdefault(str(reaction.emoji), reaction.count)
        except discord.errors.Forbidden:
            print('Forbidden error : ' + str(channel) + ' channel')

    return countDic