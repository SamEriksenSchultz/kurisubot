import discord
from discord.ext import commands

class Users(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        sender = ctx.message.author

        await member.kick(reason=f"kicked via command by {sender}: {reason}")

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        sender = ctx.message.author

        await member.ban(reason=f"banned via command by {sender}: {reason}")

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_disciminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.name}#{user.discriminator}")




def setup(client):
    client.add_cog(Users(client))
