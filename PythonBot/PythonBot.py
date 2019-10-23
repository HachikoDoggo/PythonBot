import discord
import time
import asyncio
import sys
import os
import config
import random
import io
import traceback
import warnings
import concurrent.futures
import threading
import logging
from discord.ext import commands, tasks
from itertools import cycle

token = open("token.txt","r").read()

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

status = cycle(['Serving 1 Server', 'And thats my testing server', 'LOL', 'Contact My creator on xbox!', 'XBOX=Hachi Is My Dog', 'Remember im still in development!', 'FUCK LIFE'])
#valid_users = ["╲⎝⧹Tony Stark⧸⎠╱#6947"]

client = commands.Bot(command_prefix = '.')

#joined = 0
#messages = 0

@client.event
async def on_ready():
	change_status.start()
	print('Bot Is Loaded!')
	print('Status Is Changing!')

@tasks.loop(seconds=3)
async def change_status():
	await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_message(message):
    id = client.get_guild(596539671471980544)

    if message.content.find("!hello") != -1:
        await message.channel.send("Hi")
    elif message.content == "!users":
        await message.channel.send(f"""# of Members: {id.member_count}""")


@client.event
async def update_stats():
    await client.wait_until_ready()
    global messages, joined

@client.command()
async def load(ctx, extension):
	client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
		client.unload_extension(f'cogs.{extension}')
for filename in os.listdir(r"C:\Users\missw\Desktop\PythonBot\Cogs"):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

@client.command()
async def say(ctx, arg):
	await ctx.send(arg)


client.run(token)
