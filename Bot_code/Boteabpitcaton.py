import discord
import random
from discord.ext import commands
from discord.ext.commands import cooldown
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


@client.command(name="help")
@cooldown(rate=1, per=5)
async def help(ctx):
    await ctx.channel.send("Command not done")
    await ctx.channel.send("Commands are \n!?help(Not done)\n!?not\n!?ping\n!?play\n"
                           "!?playasongprettyplease(Not done)\n!?poe(Beta)\n!?prune(Not done)\n?!riddle(Not "
                           "done)\n!?spek(Beta)\n!?troofax(Beta)")
    await ctx.channel.send("FuK oFf nOw DowNiE")


@client.command(name="not", description="Not!")
@cooldown(rate=1, per=4)
async def Not(ctx):
    await ctx.channel.send("...Not!")


@client.command(name="ping")
@cooldown(rate=1, per=5)
async def Ping(ctx):
    await ctx.channel.send("FcUck Yo Ou")


@client.command(name="play", description="plays a song", usage="<song link>")
async def Play(ctx):
    await ctx.channel.send("the command YOu\'re tryiNG to ask me to do seems to be !?playavideoprettyplease")
    await ctx.channel.send("send that one then we\'ll talk")
    return


@client.command(name="playasongprettyplease")
@cooldown(rate=1, per=5)
async def playasongprettyplease(ctx):
    await ctx.channel.send("Command not done")
    await ctx.channel.send("FuK oFf DowNiE")


@client.command(name="poe", description="Poetic genius", aliases=["poetry", "edgar", "alan"])
@cooldown(rate=1, per=3)
async def Poe(ctx):
    x = random.randint(0, 3)
    if x == 0:
        await ctx.channel.send(theRaven)
        x = random.randint(0, 3)

    if x == 1:
        await ctx.channel.send(theRaven_2)
        x = random.randint(0, 3)

    if x == 2:
        await ctx.channel.send(theRaven_3)
        x = random.randint(0, 3)

    if x == 3:
        await ctx.channel.send(theRaven_4)
        x = random.randint(0, 3)


@client.command(name="prune", description="Bulk deletes messages", aliases=["delete", "bulkdel"],
                usage="<number of messages (1-99)>")
async def prune(ctx):
    await ctx.channel.send("Command not done")
    await ctx.channel.send("FuK oFf DowNiE")


@client.command(name = "riddle", description = "Gives you a brain teaser")
@cooldown(rate = 1, per = 3)
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


client.run('ODA0NzQ4NjIwNjQ1NDAwNjI2.YBQ2jg.VCx8c3grqUw8j0mVRMwmt1lnyGU')
