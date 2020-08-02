""" Discord Bot, with a collection of various nerdy commands. """
# System imports
import os
from random import randint

# External packages (pip)
import requests
import discord
from discord.ext import commands

BOT_PREFIX = os.environ['discord_prefix']
TOKEN = os.environ['discord_token']
WEATHER_API_KEY = os.environ['open_weather_map_key']
NASA_API_KEY = os.environ['nasa_api_key']

bot = commands.Bot(command_prefix=BOT_PREFIX)

@bot.event
async def on_ready():
    """ Startup Procedure """
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name=BOT_PREFIX + 'help', type=3))

# Remove default help command
bot.remove_command('help')

@bot.command(pass_context=True)
async def help(ctx):
    """ Sends help message to the user, informing of available commands """
    message = """
Hey there! You need help?
Here are the commands I respond to:
** >help ** - I will whisper you this help message
** >roll ** - Nothing unique. I'll just roll a dice from 1-100. Good Luck!
** >affixes ** - Will tell you what shitty M+ affixes you have to deal with.
** >io [region] [realm] [player] ** - Announce size of 'epeen' (RaiderIO score).
** >weather [zip code] ** - Let you know the weather for zipcode, so you don't have to go outside.
    """
    await ctx.send(message)

@bot.command(pass_context=True)
async def prefix(ctx, value):
    """ Allows server administrators to change the bot prefix """
    if ctx.message.author.server_permissions.administrator:
        os.environ['discord_bot_prefix'] = value
        helpstr = os.environ['discord_bot_prefix'] + 'help'

        await bot.change_presence(game=discord.Game(name=helpstr, type=3))
    else:
        await ctx.send('You cannot run this command, sorry!')

@bot.command(pass_context=True)
async def nasa_apod(ctx):
    """ Sends a beautiful space picture of the day from NASA """
    url = 'https://api.nasa.gov/planetary/apod?api_key=' + NASA_API_KEY
    response = requests.get(url)
    response = response.json()

    print(response)

    photo = response['url']
    title = response['title']

    await ctx.send('** Description: **' + title + "\n" + photo)

@bot.command(pass_context=True)
async def weather(ctx, zipcode):
    """ Gets the current weather for given US zip code """
    url = 'https://api.openweathermap.org/data/2.5/weather?'
    url += 'zip=' + zipcode
    url += '&appid=' + WEATHER_API_KEY

    response = requests.get(url)
    response = response.json()

    print(response)

    forecast = response['weather'][0]['description']
    forecast = forecast.title()
    code = response['weather'][0]['id']
    station = response['name']

    if int(code) <= 800:
        code = int(str(code)[:1])
        emojistr = {
            2: ':thunder_cloud_rain: :fearful:',
            3: ':white_sun_rain_cloud:',
            5: ':cloud_rain: :frowning:',
            6: ':cloud_snow: :snowflake: :snowman:',
            7: ':foggy: :eyeglasses:',
            8: ':white_sun_small_cloud: :sunny: :fire:'
        }
        emojistr = emojistr.get(code, '')
    else:
        emojistr = ':cloud: :slight_frown: :cloud: :slight_frown: :cloud:'

    await ctx.send('**The Weather for ' + station + ' is: **' + forecast + ' ' + emojistr)

@bot.command(pass_context=True)
async def affixes(ctx):
    """ Gets the current Mythic+ affixes """
    response = requests.get("https://raider.io/api/v1/mythic-plus/affixes?region=us&locale=en")
    response = response.json()
    affixes = response['title']
    await ctx.send('**Current Mythic+ Affixes (US):** ' + affixes)

@bot.command(pass_context=True)
async def io(ctx, region, realm, player):
    """ Gets the Raider IO score for region, realm, player """
    # Ensure proper formatting of params
    region = region.lower()
    realm = realm.lower()
    player = player.capitalize()

    # Build request URL
    url = "https://raider.io/api/v1/characters/profile"
    url += "?region=" + region
    url += "&realm=" + realm
    url += "&name=" + player
    url += "&fields=mythic_plus_scores_by_season:current"

    response = requests.get(url)
    response = response.json()
    score = response['mythic_plus_scores_by_season'][0]['scores']['all']
    score = str(score)
    await ctx.send('**Raider IO score for '+ player + ':** ' + score)

@bot.command(pass_context=True)
async def roll(ctx):
    """ Rolls a pseudorandom number from 0 to 100 """
    num = randint(0, 100)
    num = str(num)
    await ctx.send(ctx.message.author.mention + ' rolled ' + num)

bot.run(TOKEN)
