""" Discord Bot, with a collection of various nerdy commands. """
# System imports
import os
from random import randint

# External packages (pip)
import requests
import discord
from discord.ext import commands


BOT_PREFIX = '>'
# TOKEN = os.environ['discord_token']
# WEATHER_API_KEY = os.environ['open_weather_map_key']
# NASA_API_KEY = os.environ['nasa_api_key']

bot = commands.Bot(command_prefix=BOT_PREFIX)

# Remove default help command
bot.remove_command('help')

@bot.event
async def on_ready():
    """ Startup Procedure """
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    activity = discord.Game(name=f"{BOT_PREFIX}help", type=discord.ActivityType.watching)
    await bot.change_presence(status=discord.Status.online, activity=activity)

# Commands
import commands


# bot.run(TOKEN)
