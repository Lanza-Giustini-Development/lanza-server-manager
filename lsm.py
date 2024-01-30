import discord  # added this
from discord.ext import commands

prefix = "/"
intents = discord.Intents.all()  # added this
bot = commands.Bot(command_prefix=prefix, intents=intents)  # modified this


@bot.event
async def on_ready():
    print("Everything's all ready to go~")


@bot.event
async def on_message(message):
    print("The message's content was", message.content)
    await bot.process_commands(message)


@bot.command()
async def ping(ctx):
    '''
    This text will be shown in the help command
    '''

    print("hello")

    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)


@bot.command()
async def echo(ctx, *, content:str):
    await ctx.send(content)

bot.run("")  # Where 'TOKEN' is your bot token