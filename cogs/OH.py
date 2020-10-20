import discord
from discord.ext import commands

class OH(commands.Cog):

    def __init__(self, client):
          self.client = client
          self.OHQueue = []
          self.number = 0


    #Events
    @commands.Cog.listener() #decorator
    async def on_ready(self):
        print('bot is ready from OH')


    #Commands
    @commands.command() #join queue
    async def q(self, ctx, *, question):
        self.number += 1
        user = ctx.author
        tuple = (self.number, user, question)
        self.OHQueue.append(tuple)
        #client.clear(1)
        role = discord.utils.get(user.guild.roles, name='In queue')
        await user.add_roles(role)
        await user.send(f'you have joined the queue as number {self.number}')
        await user.send(f'your question: {question}')
        print(tuple)



    # @commands.command()
    # async def edit(self, ctx, *, question):
    #     pass

    @commands.command()
    async def leave(self, ctx):
        user = ctx.author
        role = discord.utils.get(user.guild.roles, name='In queue')
        await user.remove_roles(role)
        self.OHQueue = [tuple for tuple in self.OHQueue if str(tuple[1]) != str(user)]
        print(self.OHQueue)
        await ctx.send('you have left the queue')

    @commands.command()
    async def next(self, ctx):
        if(not self.OHQueue):
            await ctx.send('queue is empty')
            self.number = 0
            await client.change_presence(status=discord.Status.online, activity=discord.Game('OH has started'))
        else:
            tuple = self.OHQueue.pop(0)
            number = tuple[0]
            user = tuple[1]
            question = tuple[2]
            name = str(user)
            await self.client.change_presence(status=discord.Status.online, activity=discord.Game(f'{number}. {name} is currently being helped'))
            role = discord.utils.get(user.guild.roles, name='In queue')
            await user.remove_roles(role)
            await user.send('you are currently being helped')


def setup(client):
    client.add_cog(OH(client))
