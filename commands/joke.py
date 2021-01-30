async def joke(ctx):
    joke_api = "https://official-joke-api.appspot.com/random_joke"
    data = requests.get(joke_api)
    joke = json.loads(data.text)
    for i in (joke):
        await ctx.send(f"{i['type']}\n{i['setup']}\n{i['punchline']}")
