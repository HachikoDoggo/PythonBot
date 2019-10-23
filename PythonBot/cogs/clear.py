import discord
from discord.ext import commands

class Clear(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def clear(self, ctx, limit: int = 100):
        messages = await ctx.channel.purge(limit=limit)
        await ctx.channel.send('{} messages deleted'.format(len(messages)))

def setup(client):
    client.add_cog(Clear(client))
