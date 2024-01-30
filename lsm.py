import discord
from discord.ext import commands
import os
import requests

TOKEN = os.getenv('DISCORD_TOKEN')
WHITELIST = os.getenv('WHITELIST').split(",")
base_url= "http://localhost:5000/"
palworld_startup_url =  base_url + "/palworld/startup"
palworld_shutdown_url = base_url + "/palworld/shutdown"


prefix = "/"
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=intents)
pal_dir = "/docker-compose-palworld"

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

#stop palworld server
@bot.command()
async def palworld_shutdown(ctx):
    print("palworld startup requested")
    ret = requests.post(palworld_shutdown_url)
    if (ret.status_code == 200):
        msg = "Palworld shutdown succeeded"
        await ctx.send(msg)
    else:
        msg = "Palworld shutdown failed"
        await ctx.send(msg)

#start palworld server
@bot.command()
async def palworld_startup(ctx):
    print("palworld startup requested")
    ret = requests.post(palworld_startup_url)
    if (ret.status_code == 200):
        msg = "Palworld startup succeeded"
        await ctx.send(msg)
    else:
        msg = "Palworld startup failed"
        await ctx.send(msg)

@bot.command()
async def test_flask(ctx):
    ret = requests.get(base_url)
    if (ret.status_code == 200):
        msg = "Flask Service Alive"
        await ctx.send(msg)
    else:
        msg = "No Flask Service Avaliable"
        await ctx.send(msg)

#run the bot
bot.run(TOKEN)
