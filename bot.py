# bot.py
import os

import discord
from dotenv import load_dotenv

import botCommands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print('Bot connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    quote = "gilipollas"

    if message.content == "bobo":
        response = quote
        await message.channel.send(response)
        


client.run(TOKEN)