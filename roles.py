import discord
import discord.utils

from discord.ext import commands

class Roles(commands.Cog):

    def __init__(self, client):
        self.client = client


    ROLE = "Bot"






def setup(client):
    client.add_cog(Roles(client))
