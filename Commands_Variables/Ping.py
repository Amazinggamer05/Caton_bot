from discord.ext import commands

client = commands.Bot(command_prefix="!?")


@client.command(name = "ping", cooldown = 5, description = "PonG?!")
async def Ping(message):

    await message.channel.send("FcUck Yo Ou")
