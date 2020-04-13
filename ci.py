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
    
    text = 'Count Result\n'
    
    lastweek = datetime.datetime.now() - datetime.timedelta(weeks=1)
    last1week_result = await emojicnt.count_emoji(guild, after=lastweek)
    sorted_last1week_result = dict(sorted(last1week_result.items(), key=lambda x:x[1], reverse=True))
    text += 'Last 1 week messages\n' + dic2text.convert(sorted_last1week_result)
    
    last200_result = await emojicnt.count_emoji(guild, limit=200)
    sorted_last200_result = dict(sorted(last200_result.items(), key=lambda x:x[1], reverse=True))
    text += 'Last 200 messages for each channel\n' + dic2text.convert(sorted_last200_result)
    
    print(text)
    
    channel = guild.get_channel(channelId)
    if channel is None:
        print('Not Found Channel')
        await client.close()
        return
    await channel.send(text)

    await client.close()

client.run(bottoken)