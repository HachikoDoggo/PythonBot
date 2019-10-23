import discord
import asyncio
import os
import config
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

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
	change_status.start()
	print('Bot Is Loaded!')
	print('Status Is Changing!')

@tasks.loop(seconds=3)
async def change_status():
	await client.change_presence(activity=discord.Game(next(status)))

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

for filename in os.listdir("./cogs"):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)
