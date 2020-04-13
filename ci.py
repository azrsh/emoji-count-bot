import sys
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
    
    result = await emojicnt.count_emoji(guild)
    sorted_result = dict(sorted(result.items(), key=lambda x:x[1], reverse=True))
    text = 'Count Result\n' + dic2text.convert(sorted_result)
    print(text)
    
    channel = guild.get_channel(channelId)
    if channel is None:
        print('Not Found Channel')
        await client.close()
        return
    await channel.send(text)

    await client.close()

client.run(bottoken)