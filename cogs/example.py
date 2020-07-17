import discord
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client;

    #Events
    @commands.Cog.listener() #decorator
    async def on_ready(self):
        print('bot is ready from cog')

    #Commands
    @commands.command()
    async def ping2(self, ctx):
        await ctx.send('Pong!')

def setup(client):
    client.add_cog(Example(client))
