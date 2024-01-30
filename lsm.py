import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv('./.env')

TOKEN = os.getenv('DISCORD_TOKEN')
WHITELIST = os.getenv('WHITELIST').split(",")

prefix = "/"
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=intents)


@bot.event
async def on_ready():
    print("LSM is online and ready to recieve commands")


#the bot waits for messages and parses them through this function
@bot.event
async def on_message(message):
    #only whitelisted users are allowed to access the bot commands
    if (str(message.author) in WHITELIST):
        await bot.process_commands(message)


#command to get the ping for the bot to the discord server
@bot.command()
async def ping(ctx):
    print("ping info requested")
    latency = bot.latency
    await ctx.send(latency)


#basic echo command for the bot
@bot.command()
async def echo(ctx, *, content:str):
    await ctx.send(content)

#run the bot
bot.run(TOKEN)