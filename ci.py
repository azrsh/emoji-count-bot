import sys
import discord
import emojicnt

if (len(sys.argv) < 4):
    sys.exit()
bottoken = sys.argv[1]
guildId = int(sys.argv[2])
channelId = int(sys.argv[3])

client = discord.Client()

@client.event
async def on_ready():
    guild = client.get_guild(guildId)
    if guild is None:
        print('Not Found Guild')
        client.close()
    
    result = await emojicnt.count_emoji(guild)
    print(str(result))
    
    channel = guild.get_channel(channelId)
    if guild is None:
        print('Not Found Channel')
        client.close()
    await channel.send(result)

    await client.close()

client.run(bottoken)