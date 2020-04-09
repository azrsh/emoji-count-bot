import sys
import discord
import emojicnt
import dic2text

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
    text = 'Count Result\n' + dic2text.convert(result)
    print(text)
    
    channel = guild.get_channel(channelId)
    if guild is None:
        print('Not Found Channel')
        client.close()
    await channel.send(text)

    await client.close()

client.run(bottoken)