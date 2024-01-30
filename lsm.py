import discord  # added this
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv('./.env')

TOKEN = os.getenv('DISCORD_TOKEN')
WHITELIST = os.getenv('WHITELIST').split(",")

prefix = "/"
intents = discord.Intents.all()  # added this
bot = commands.Bot(command_prefix=prefix, intents=intents)  # modified this


@bot.event
async def on_ready():
    print("LSM is online and ready to recieve commands")


@bot.event
async def on_message(message):
    print("The message's author was", message.author)
    print(str(message.author) in WHITELIST)
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

bot.run(TOKEN)  # Where 'TOKEN' is your bot token