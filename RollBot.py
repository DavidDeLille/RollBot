#!/usr/bin/python3
EMAIL = 'ministryofsillyhacks@gmail.com'
PASSWORD = 'justalongpw'

    # client = discord.Client()
    # client.login(EMAIL, PASSWORD)

from getpass import getpass 
import discord
import logging
import asyncio
import random

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('RollBot')

if __name__ == "__main__":

    client = discord.Client()

    @client.event
    async def on_message(message):
        # we do not want the bot to reply to itself
        if message.author == client.user:
            return

        if message.content.startswith('!hello'):
            msg = 'Hello {0.author.mention}'.format(message)
            await client.send_message(message.channel, msg)

    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')

    client.run(EMAIL, PASSWORD)