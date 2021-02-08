import discord
import os
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Bot is online')
    activity = discord.Game(name="osu!")
    await client.change_presence(status=discord.Status.idle, activity=activity)



@client.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Extension {extension} loaded')

@load.error
async def load_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send('Error, extension already loaded')
    else:
        raise error

@client.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Extension {extension} unloaded')

@unload.error
async def unload_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send('Error, extension has not been loaded')
    else:
        raise error

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'Cleared {amount} messages')

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 801742271552290826:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
        role = discord.utils.get(guild.roles, name="Certifiably Competent")

        if role is not None:
            member = payload.member
            await member.add_roles(role)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run('Nzk3NTI1NDM0NzA2NjkwMTE5.X_nvcA.ZzlaNlzXaH21L_SSgGRE_dndHm4')
