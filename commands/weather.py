@bot.command(pass_context=True)
async def weather(ctx, zipcode):
    # Gets the current weather for given US zip code
    url = 'https://api.openweathermap.org/data/2.5/weather?'
    url += f"zip={zipcode}&appid={WEATHER_API_KEY}"

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
    await ctx.send(f"**The Weather for {station} is:** {forecast} {emojistr}")
