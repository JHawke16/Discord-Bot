import discord 

from discord.ext import commands

import os

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
  print('Bot is ready')

@client.event
async def on_message(msg):
  if msg.author == client.user:
    return

  if msg.content == 'clown':
    await msg.add_reaction('\U0001F921')

  if 'clown' in msg.content.lower():
    await msg.add_reaction('\U0001F921')
    await msg.channel.send('I am a clown too  \U0001F921')

client.run(os.environ['TOKEN'])

