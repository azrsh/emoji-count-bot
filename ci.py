import sys
import discord
import emojicnt

if (len(sys.argv) < 3):
    sys.exit()
bottoken = sys.argv[1]
guildId = int(sys.argv[2])

client = discord.Client()

@client.event
async def on_ready():
    guild = client.get_guild(guildId)
    if guild is None:
        print('Not Found Guild')
        sys.exit()
    
    result = await emojicnt.count_emoji(guild)
    print(str(result))
    await client.close()

client.run(bottoken)