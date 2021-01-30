async def nasa_apod(ctx):
    """ Sends a beautiful space picture of the day from NASA """
    url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"
    response = requests.get(url)
    response = response.json()

    print(response)

    photo = response['url']
    title = response['title']

    await ctx.send(f"** Description: **{title}\n{photo}")