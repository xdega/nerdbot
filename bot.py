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

# Remove default help command
client.remove_command('help')

@client.command(pass_context = True)
async def help(ctx):
    context = dir(ctx)
    print(context)
    await ctx.message.author.send('Hey there! You need help?')

@client.command(pass_context = True)
async def roll(ctx):
    num = randint(1,100)
    num = str(num)
    await client.say(ctx.message.author.mention + ' rolled ' + num)

client.run(TOKEN)
