import os
import discord
import requests
from discord.ext import commands


class Nasa(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.NASA_API_KEY = os.environ["nasa_api_key"]

        print("Loading Command: NASA")

    # Commands
    @commands.command()
    async def nasa_apod(self, ctx):
        # Sends a beautiful space picture of the day from NASA
        url = f"https://api.nasa.gov/planetary/apod?api_key={self.NASA_API_KEY}"
        response = requests.get(url)
        response = response.json()

        photo = response["url"]
        title = response["title"]

        await ctx.send(f"** {title} ** \n {photo}")


def setup(client):
    client.add_cog(Nasa(client))
    print("Added Command: NASA")
