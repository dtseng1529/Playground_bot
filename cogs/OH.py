import discord
from discord.ext import commands

class OH(commands.Cog):
     
     def __init__(self, client):
          self = client
          OHQueue = 
          
    #Events
    @commands.Cog.listener() #decorator
    async def on_ready(self):
        print('bot is ready from cog')

    #Commands
    @commands.command()
    async def ping2(self, ctx):
        await ctx.send('Pong!')
    
    @commands.command() #join queue
    async def q(self, ctx, *, question):
        await ctx.author.send(f'you have joined the queue as number {number}')
        await ctx.author.send(f'your question: {question}')
    
    @commands.command()
    async def edit(self, ctx, *, question):
    
    @commands.command()
    async def leave(self
    
    @commands.command()
    async def next():
    

def setup(client):
    client.add_cog(OH(client))
        await client.change_presence(status=discord.available, activity=discord.Game(f'{number} \. {name} is currently being helped'))
