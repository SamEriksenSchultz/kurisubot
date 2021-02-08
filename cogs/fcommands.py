import discord
from discord.ext import commands

class Fcommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    #events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online')

    #commands
    @commands.command()
    async def assistant(self):
        responses = ['']
        await ctx.send()


def setup(client):
    client.add_cog(Fcommands(client))
