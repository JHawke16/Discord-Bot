import discord 

from discord.ext import commands

import os

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
  print('Bot is ready')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content == 'clown':
    await message.add_reaction('\U0001F921')


client.run(os.environ['TOKEN'])

