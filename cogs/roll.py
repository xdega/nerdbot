import discord
from discord.ext import commands

from random import randint


class Roll(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Loading Command: Roll.")

    # Commands
    @commands.command()
    async def roll(self, ctx):
        # Rolls a pseudo-random number from 0 to 100
        num = str(randint(0, 100))
        await ctx.send(f"{ctx.message.author.mention} rolled {num}")


def setup(client):
    client.add_cog(Roll(client))
