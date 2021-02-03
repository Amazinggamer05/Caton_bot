from discord.ext import commands

client = commands.Bot(command_prefix="!?")


@client.command()
async def Help(message):

    # Send the author the information about the bot #

    await message.author.send("AL of my Womderful commAnds: !help\n!not\n!ping\n!play\n!playasongprettyplease"
                              "\n!poe\n!prune\n!riddle\n!spek!\n!troofax"
                              "hope that educated you a bit you ignorant shit.")

    if message.channel.type != "dm":
        return message.channel.send(message.author, "ISent YA A DEE eMM")
