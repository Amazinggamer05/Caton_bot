import random
from discord.ext import commands

riddles = """What's red and black and white all over?,
            What is green and fuzzy and will kill you if it falls out of a tree?"""
answers = "A monoracial sacrificial orgy.", "A pool table."

client = commands.Bot(command_prefix="!")


def rand(min1, max2):
    randomnum = random.randint(min1, max2 * max2 - min1 + min1) * (max2 - min1) + min1
    return round(randomnum)


@client.command(name = "riddle", description = "Gives you a brain teaser", cooldown = 3 )
async def riddle(message):
    if len(riddles) != len(answers):
        await message.channel("Too many riddles/answers")
    index = rand(0, len(riddles) - 1)
    message.channel.send(index + "\n||${answers[index]}||")
    await message.channel.send("")
