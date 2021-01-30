@bot.command(pass_context=True)
async def help(ctx):
    # Sends help message to the user, informing of available commands
    message = """
Hey there! You need help?
Here are the commands I respond to:
** help ** - I will whisper you this help message.
** roll ** - Nothing unique. I'll just roll a dice from 1-100. Good Luck!
** weather [zip code] ** - Let you know the weather for zipcode, so you don't have to go outside.
** nasa_apod ** - Displays the Astronomy Picture of the Day, provided by the NASA API.
    """
    await ctx.send(message)
