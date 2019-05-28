import os, discord
import requests
from random import randint
from discord.ext.commands import Bot

BOT_PREFIX = os.environ['discord_prefix']
TOKEN = os.environ['discord_token']
WEATHER_API_KEY = os.environ['open_weather_map_key']

client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name="101010 >help"))

# Remove default help command
client.remove_command('help')

@client.command(pass_context = True)
async def help(ctx):
    message = """
Hey there! You need help?
Here are the commands I respond to:
** >help ** - I will whisper you this help message
** >roll ** - Nothing unique. I'll just roll a dice from 1-100. Good Luck!
    """
    await client.send_message(ctx.message.author, message)

@client.command()
async def weather(zipcode, country=''):
    url = 'api.openweathermap.org/data/2.5/weather?'
    url += 'zip=' + zipcode
    if(country != ''): url += ',' + country
    url += '&appid=' + WEATHER_API_KEY

    response = requests.get(url)
    response = response.json()

    forecast = response['weather']['description']
    station = response['name']

    await client.say('**The Weather for ' + station + ': **' + forecast)

@client.command()
async def affix():
    response = requests.get("https://raider.io/api/v1/mythic-plus/affixes?region=us&locale=en")
    response = response.json()
    affixes = response['title']
    await client.say('**Current Mythic+ Affixes (US):** ' + affixes)

@client.command()
async def io(region, realm, player):
    # Ensure proper formatting of params
    region = region.lower()
    realm = realm.lower()
    player = player.capitalize()

    # Build request URL
    url = "https://raider.io/api/v1/characters/profile"
    url +="?region=" + region
    url +="&realm=" + realm
    url +="&name=" + player
    url +="&fields=mythic_plus_scores_by_season:current"

    response = requests.get(url)
    response = response.json()
    score = response['mythic_plus_scores_by_season'][0]['scores']['all']
    score = str(score)
    await client.say('**Raider IO score for '+ player + ':** ' + score)

@client.command(pass_context = True)
async def roll(ctx):
    num = randint(1,100)
    num = str(num)
    await client.say(ctx.message.author.mention + ' rolled ' + num)

client.run(TOKEN)
