import discord
import random
from discord.ext import commands
from discord.ext.commands import cooldown
from Commands_Variables.Poe import *
from Commands_Variables.Riddle import *
from Commands_Variables.troofax import *
from Commands_Variables.Spek import *

client = commands.Bot(command_prefix='!?')


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.command(name="ping")
@cooldown(rate=1, per=5)
async def Ping(ctx):
    await ctx.channel.send("FcUck Yo Ou")
