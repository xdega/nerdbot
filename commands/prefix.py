@bot.command(pass_context=True)
async def prefix(ctx, value):
    """ Allows server administrators to change the bot prefix """
    if ctx.message.author.server_permissions.administrator:
        os.environ['discord_prefix'] = value
        helpstr = os.environ['discord_prefix'] + 'help'

        await bot.change_presence(game=discord.Game(name=helpstr, type=3))
    else:
        await ctx.send('You cannot run this command, sorry!')
