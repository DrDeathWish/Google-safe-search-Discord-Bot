import discord
import requests

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print('Bot ID: {}'.format(client.user.id))

@client.event
async def on_message(message):
    # Check if the message contains a link
    if 'http' in message.content:
        # Extract the link from the message
        link = message.content.split('http')[1]
        link = f'http{link}'

        # Use the Google Safe Search API to check the safety of the link
        response = requests.get('https://safebrowsing.googleapis.com/v4/threatMatches:find', params={
            'key': 'YOUR_API_KEY',
            'threatTypes': 'MALWARE',
            'platformTypes': 'ALL_PLATFORMS',
            'threatEntryTypes': 'URL',
            'threatEntries': [{'url': link}]
        })

        # If the link is not safe, delete the message
        if response.json()['matches']:
            await message.delete()

client.run('YOUR_BOT_TOKEN')
