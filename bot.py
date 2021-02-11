import os
import discord
from discord.ext import commands

TOKEN = os.getenv("discord_token")
BOT_PREFIX = os.getenv("discord_prefix", ">")

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

# Run the bot if a TOKEN is provided
if TOKEN:
    client.run(TOKEN)

print("End of File: bot.py")
