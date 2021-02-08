import discord
from discord.ext import commands

class Roles(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def giverole(self, ctx, *, pendingRole:str):
        user = ctx.message.author
        knownrole = discord.utils.get(ctx.guild.roles, name=f"{pendingRole}")
        await user.add_roles(knownrole)
        await ctx.send(f"{user.mention}, you have been assigned the role **{pendingRole}**")

    @giverole.error
    async def giverole_error(self, ctx, error):
        await ctx.send('Error:')
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please include all necessary arguments.')
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('Role not found')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have the necessary permissions for that role")
        else:
            raise error

    @commands.command()
    async def addrole(self, ctx, *, newRole:str):
        creator = ctx.message.author
        guild = ctx.guild
        await guild.create_role(name=newRole, mentionable=True, reason=f"requested by user {creator}")
        await ctx.send(f"Role **{newRole}** has been created.")

    @addrole.error
    async def addrole_error(self, ctx, error):
        await ctx.send('Error:')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You are not authorized to create new roles")
        else:
            raise error

    @commands.command()
    async def removerole(self, ctx, *, role:str):
        user = ctx.message.author
        knownrole = discord.utils.get(ctx.guild.roles, name=f"{role}")
        await user.remove_roles(knownrole)
        await ctx.send(f"{user.mention}, your role **{pendingRole}**, has been removed")

    @removerole.error
    async def removerole_error(self, ctx, error):
        await ctx.send('Error:')
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please include all necessary arguments.')
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('Role not found')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have the necessary permissions for that role")
        else:
            raise error







def setup(client):
    client.add_cog(Roles(client))
