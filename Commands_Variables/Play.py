from discord.ext import commands

client = commands.Bot(command_prefix="!")


@client.command(name = "play", description = "plays a song", usage = "<song link>")
async def Play(message):

    # Send the author the information about the bot #

    await message.channel.send("the command YOu\'re tryiNG to ask me to do seems to be !playavideoprettyplease")
    await message.channel.send("send that one then we\'ll talk")
    return


