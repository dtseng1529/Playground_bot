import discord
import random
import os
from discord.ext import commands, tasks
from itertools import cycle


client = commands.Bot(command_prefix = '~')
status = cycle(['with the ground...get it? playground?', 'league, aka losing lp', 'development testing'])
#OH = False

@client.event #on ready + status + change status loop
async def on_ready():
    #await client.change_presence(status=discord.Status.dnd, activity=discord.Game('with the ground...get it? playground?'))
    #change_status.start()
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('OH is over'))
    guild = discord.utils.get(client.guilds, name='DiscordBotF20')
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    print('bot is ready')

@client.event #notify join
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event #kick
async def on_member_remove(member):
    print(f'{member} has left a server.')

@client.command() #ping command
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball', '8test']) #8ball command with multiple ways to call
async def _8ball(ctx, *, question):
    responses =     ["It is certain.",
                    "It is decidedly so.",
                    "Without a doubt.",
                    "Yes - definitely.",
                    "You may rely on it.",
                    "As I see it, yes.",
                    "Most likely.",
                    "Outlook good.",
                    "Yes.",
                    "Signs point to yes.",
                    "Reply hazy, try again.",
                    "Ask again later.",
                    "Better not tell you now.",
                    "Cannot predict now.",
                    "Concentrate and ask again.",
                    "Don't count on it.",
                    "My reply is no.",
                    "My sources say no.",
                    "Outlook not so good.",
                    "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command() #clear messages
@commands.has_permissions(manage_messages=True) #a check on permissions
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount + 1)
    if(amount == 1):
        await ctx.channel.send(f'time rewinded {amount} message')
    else:
        await ctx.channel.send(f'time rewinded {amount} messages')

# @client.command()
# async def kick(ctx, member : discord.Member, *, reason = None):
#     await member.kick(reason=reason)

@client.command() #load cog
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command() #unload cog
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

# @tasks.loop(seconds=10) #background task
# async def change_status():
#     await client.change_presence(activity = discord.Game(next(status)))

# @client.event #general error commnad [careful, if error happens we will not know]
# async def on_command_error(ctx, error):
#     if isinstance(error, commands.CommandNotFound):
#         await ctx.send('Command does not exist')

@clear.error #only triggered when clear is triggered
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify amount of messages to delete')

def is_it_me(ctx): #check my id
    return ctx.author.id == 176508595305709568

@client.command() #example custom check
@commands.check(is_it_me)
async def example_custom_check(ctx):
    await ctx.send(f'Hi Im {ctx.author}')

# def OH_true(ctx):
#     return OH
#
# def OH_not_true(ctx):
#     return not OH

@client.command(aliases=['start'])
#@commands.check(OH_not_true)
async def startOH(ctx):
    #global OH
    client.load_extension('cogs.OH')
    await client.change_presence(status=discord.Status.online, activity=discord.Game('OH has started'))
    #OH = True

@client.command(aliases=['stop'])
#@commands.check(OH_true)
async def stopOH(ctx):
    #global OH
    client.unload_extension('cogs.OH')
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('OH is over'))
    #OH = False


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.unload_extension('cogs.OH')

client.run('[token]')
