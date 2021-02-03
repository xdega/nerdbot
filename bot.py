import os
import discord
from discord.ext import commands

# TODO: These could probably be factored into a settings file
#TOKEN = os.environ['discord_token']
BOT_PREFIX = os.environ['discord_prefix']
#BOT_PREFIX = '>'

# TODO: These Env variables should be moved to their respective cog files
# WEATHER_API_KEY = os.environ['open_weather_map_key']
# NASA_API_KEY = os.environ['nasa_api_key']

client = commands.Bot(command_prefix=BOT_PREFIX)


@client.event
async def on_ready():
    activity = discord.Game(
        name=f"{BOT_PREFIX}help",
        type=discord.ActivityType.watching)
    await client.change_presence(status=discord.Status.online, activity=activity)

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(TOKEN)
