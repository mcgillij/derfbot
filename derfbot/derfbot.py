import os
import discord
import logging
import requests
import asyncio

# Configure logging
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
log.addHandler(handler)

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

REST_ENDPOINT = "http://fastchat:8000/v1/chat/completions"

PROMPT = """{
    "model": "vicuna-7b-v1.1",
    "messages": [{"role": "user", "content": "PROMPT"}]
}"""


@client.event
async def on_ready():
    log.info('Logged in as')
    log.info(client.user.name)
    log.info(client.user.id)
    log.info('------')


@client.event
async def on_message(message):
    log.info('Received a message')
    # Ignore messages from the bot itself
    if message.author.bot:
        return

    # Check if the message starts with !derf
    if message.content.startswith('!derf'):
        log.info('Received a message starting with !derf')
        try:
            # Make an asynchronous HTTP request to the REST API
            query = PROMPT.replace('PROMPT', message.content[5:])
            loop = asyncio.get_event_loop()
            response = await loop.run_in_executor(None, requests.post, REST_ENDPOINT, query)
            # Process the response here
            response_json = response.json()
            reply = response_json['choices'][0]['message']['content']
            await message.channel.send(f'{reply}')
        except Exception as e:
            await message.channel.send(f'Error: {e}')


client.run(os.getenv('DISCORD_TOKEN2'))
