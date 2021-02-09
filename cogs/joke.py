import discord
from discord.ext import commands
import requests
import json
import time

class Joke(commands.Cog):

    def __init__(self, client):
        self.client = client
        print("Loading Command: Joke")

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is Ready")

    # Commands
    @commands.command()
    async def joke():
        joke_api = r"https://official-joke-api.appspot.com/random_joke"
        data = requests.get(joke_api)
        joke_response = json.loads(data.text)
        await ctx.send(f"{joke_response['setup']}")
        time.sleep(2.5)
        await ctx.send(f"{joke_response['punchline']}")

def setup(client):
    client.add_cog(Joke(client))
    print("Added Command: Joke")
