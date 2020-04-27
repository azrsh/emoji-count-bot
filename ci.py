import sys
import datetime
import discord
import emojicnt
import dic2text

if (len(sys.argv) < 4):
    print("Argument Error")
    sys.exit(1)
bottoken = sys.argv[1]
guildId = int(sys.argv[2])
channelId = int(sys.argv[3])

client = discord.Client()

@client.event
async def on_ready():
    guild = client.get_guild(guildId)
    if guild is None:
        print('Not Found Guild')
        await client.close()
        return
    
    channel = guild.get_channel(channelId)
    if channel is None:
        print('Not Found Channel')
        await client.close()
        return

    textLines = ['Count Result']
    
    last1week = datetime.datetime.now() - datetime.timedelta(weeks=1)
    last1week_result = await emojicnt.count_emoji(guild, limit=None, after=last1week)
    sorted_last1week_result = dict(sorted(last1week_result.items(), key=lambda x:x[1], reverse=True))
    textLines.append('Last 1 week messages')
    textLines.extend(dic2text.convert_to_ranking(sorted_last1week_result))

    messageSendThreshold = 200
    textBlock = ''
    for line in textLines:
        textBlock += line + '\n'
        if len(textBlock) > messageSendThreshold:
            await channel.send(textBlock + '\n')
            textBlock = ''
    if textBlock != '':
        await channel.send(textBlock + '\n')
    
    #last1week = datetime.datetime.now() - datetime.timedelta(weeks=1)
    #last1week_result = await emojicnt.count_emoji(guild, limit=None, after=last1week)
    #sorted_last1week_result = dict(sorted(last1week_result.items(), key=lambda x:x[1], reverse=True))
    #text += 'Last 1 week messages\n' + dic2text.convert(sorted_last1week_result)
    #await channel.send(text)

    #last200_result = await emojicnt.count_emoji(guild, limit=200)
    #sorted_last200_result = dict(sorted(last200_result.items(), key=lambda x:x[1], reverse=True))
    #text += 'Last 200 messages for each channel\n' + dic2text.convert(sorted_last200_result)
    #await channel.send(text)

    await client.close()

client.run(bottoken)