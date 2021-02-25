async def execute(client, message, args):
    user = client.get_user(message.author.id)
    await user.send("hello")