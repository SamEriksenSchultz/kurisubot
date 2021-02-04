import discord
import os
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix='.')


@client.command()
async def giverole(ctx, )


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Extension {extension} loaded')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Extension {extension} unloaded')

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'Cleared {amount} messages')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run('Nzk3NTI1NDM0NzA2NjkwMTE5.X_nvcA.RpSSzDcdlO_ImpH3HlIVWOX3XFY')
