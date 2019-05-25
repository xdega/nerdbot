import os, discord
from random import randint
from discord.ext.commands import Bot

BOT_PREFIX = os.environ['discord_prefix']
TOKEN = os.environ['discord_token']

client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name="101010 >help"))

@client.command(pass_context = True)
async def commands(ctx):
    await ctx.author.send('Hey there! You need help?')

async def roll(ctx):
    num = randint(1,100)
    num = str(num)
    await client.say(ctx.message.author.mention + ' rolled ' + num)

client.run(TOKEN)
