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

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        sender = ctx.message.author
        channel = member.voice.channel
        await member.edit(reason=f"muted via command by {sender}", mute=True)

        await ctx.send(f"{member} has been muted")

    @mute.error
    async def mute_error(self, ctx, error):
        raise error

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def unmute(self, ctx, member: discord.Member, *, reason=None):
        sender = ctx.message.author
        channel = member.voice.channel
        await member.edit(reason=f"unmuted via command by {sender}", mute=False)

        await ctx.send(f"{member} has been unmuted")

    @unmute.error
    async def mute_error(self, ctx, error):
        raise error


    @commands.has_permissions(administrator=True)
    @commands.command()
    async def deafen(self, ctx, member: discord.Member, *, reason=None):
        sender = ctx.message.author
        channel = member.voice.channel
        await member.edit(reason=f"deafened via command by {sender}", deafen=True)

        await ctx.send(f"{member} has been deafened")

    @deafen.error
    async def deafen_error(self, ctx, error):
        raise error


    @commands.has_permissions(administrator=True)
    @commands.command()
    async def undeafen(self, ctx, member: discord.Member, *, reason=None):
        sender = ctx.message.author
        channel = member.voice.channel
        await member.edit(reason=f"undeafened via command by {sender}", deafen=False)

        await ctx.send(f"{member} has been undeafened")

    @undeafen.error
    async def undeafen_error(self, ctx, error):
        raise error

def setup(client):
    client.add_cog(Users(client))
