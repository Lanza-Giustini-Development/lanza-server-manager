import discord
from discord.ext import commands
import os
import subprocess

TOKEN = os.getenv('DISCORD_TOKEN')
WHITELIST = os.getenv('WHITELIST').split(",")

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

@bot.command()
async def palworld_shutdown(ctx):
    try:
        result = subprocess.run(
            ["docker", "compose", "down"], 
            cwd=pal_dir, 
            check=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            text=True
        )
        print("debug")
        print("Output:", result.stdout)
        print("Error:", result.stderr)
    except subprocess.CalledProcessError as e:
        print("Failed to run docker-compose down:", e)

@bot.command()
async def palworld_startup(ctx):
    try:
        pal_dir = '/docker-compose-palworld'
        subprocess.run(["docker","compose","up", "-d"], cwd=pal_dir,check=True)
        await ctx.send("Starting up The Palworld Server")
    except subprocess.CalledProcessError as e:
        await ctx.send(f"Failed to Startup Palworld Server: {e}")

#run the bot
bot.run(TOKEN)
