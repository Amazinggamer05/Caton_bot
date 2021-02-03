from discord.ext import commands

client = commands.Bot(command_prefix="!?")


@client.command(name = "not", cooldown = 4, description = "Not!")
async def Not(message):

    await message.channel.send("...Not!")



