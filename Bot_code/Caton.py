import discord
import random
from discord.ext import commands
from discord.ext.commands import cooldown, CommandOnCooldown
from Commands_Variables.Poe import *
from Commands_Variables.Riddle import *
from Commands_Variables.troofax import *
from Commands_Variables.Spek import *

# ToDo: Add Riddle, prune, playa,
# ToDo: Later add help and fix other commands to do actual functions
# ToDo: Also add cooldown notifcations and other stuff cant remember


client = commands.Bot(command_prefix='!?', help_command=None)


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.command(name="Help", aliases=["hlp", "help"])
@cooldown(rate=1, per=10)
async def help(ctx):
    hlp = discord.Embed(title="Help", description="Hlp COmmd Yo FucKin TarD")
    hlp.add_field(name="Server Management", value="Prune")
    hlp.add_field(name="\nMusic", value="Playasongprettyplease")
    hlp.add_field(name="\nWriting", value="Poe, Riddle, Spek, troofax")
    await ctx.channel.send(embed=hlp)


@client.command(name="playasongprettyplease")
@cooldown(rate=1, per=5)
async def playasongprettyplease(ctx):
    await ctx.channel.send("Command not done")
    await ctx.channel.send("FuK oFf DowNiE")


@client.command(name="poe", description="Poetic genius", aliases=["poetry", "edgar", "alan"])
@cooldown(rate=1, per=3)
async def Poe(ctx):
    y = random.randint(0, 1850)
    x = random.randint(0, 3)
    if x == 0:
        await ctx.channel.send(theRaven[0:y])
        x = random.randint(0, 3)

    if x == 1:
        await ctx.channel.send(theRaven_2[0:y])
        x = random.randint(0, 3)

    if x == 2:
        await ctx.channel.send(theRaven_3[0:y])
        x = random.randint(0, 3)

    if x == 3:
        await ctx.channel.send(theRaven_4[0:y])
        x = random.randint(0, 3)


@client.command(name="prune", description="Bulk deletes messages", aliases=["delete", "bulkdel"],
                usage="<number of messages (1-99)>")
async def prune(ctx):
    await ctx.channel.send("Command not done")
    await ctx.channel.send("FuK oFf DowNiE")


@client.command(name="riddle", description="Gives you a brain teaser")
@cooldown(rate=1, per=3)
async def riddle(ctx):
    await ctx.channel.send("Command not done")
    await ctx.channel.send("FuK oFf DowNiE")


@client.command(name="troofax", description="Spits FAX", aliases=["truth", "truefacts", "fax", "facts"])
@cooldown(rate=1, per=1)
async def troofax(ctx):
    x = random.randint(0, 1)
    if x == 0:
        await ctx.channel.send("BreD's Troo FACt: \n")
        await ctx.channel.send(truth)
        x = random.randint(0, 1)

    if x == 1:
        await ctx.channel.send("BreD's Troo FACt: \n")
        await ctx.channel.send(truth_2)
        x = random.randint(0, 1)


@client.command(name="spek", description="spits actual fire.", aliases=["sp3k"])
@cooldown(rate=1, per=3)
async def spek(ctx):
    x = random.randint(0, 1)
    if x == 0:
        await ctx.channel.send(simpDiss)
    if x == 1:
        await ctx.channel.send(imBest)
        await ctx.channel.send(imBest_2)


@client.event
async def cool(ctx):
    x = CommandOnCooldown(retry_after = x)
    await ctx.channel.send(CommandOnCooldown)


client.run('ODA0NzQ4NjIwNjQ1NDAwNjI2.YBQ2jg.OhvVsJCp9NUarI7e6QP0AeRg6Ps')
