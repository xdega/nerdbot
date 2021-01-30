async def joke(ctx):
    joke_api = r"https://official-joke-api.appspot.com/random_joke"
    data = requests.get(joke_api)
    joke_response = json.loads(data.text)
    for i in (joke_response):
        await ctx.send(f"{i['type']}\n{i['setup']}\n{i['punchline']}")
