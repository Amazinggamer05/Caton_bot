import discord
import random
import commands_caton
from discord.ext import commands
from discord.ext.commands import cooldown, CommandOnCooldown
from commands_caton.poe import *
from commands_caton.riddle import *
from commands_caton.troofax import *
from commands_caton.spek import *


# ToDo: Add Riddle, prune, playa,
# ToDo: Later add help and fix other commands to do actual functions
# ToDo: Also add cooldown notifcations and other stuff cant remember

client = commands.Bot(command_prefix='!?', help_command=None)

#When the bot starts it will run this command#
@client.event
async def on_ready():
	print("We have logged in as {0.user}".format(client))
	

#The help command will make tell the user what this bot can do#
@client.command(name="Help", aliases=["hlp", "help"])
@cooldown(rate=1, per=10)
async def help(ctx):
  hlp = discord.Embed(title="Help", description="Hlp COmmd Yo FucKin TarD")
  hlp.add_field(name="Server Management", value="Prune")
  hlp.add_field(name="Music", value="Playasongprettyplease")
  hlp.add_field(name="Writing", value="Poe, Riddle, Spek, troofax")
  await ctx.channel.send(embed=hlp)

@discord.on_typing()
async def test(ctx):
	print()

#This will play a random song from a youtube playlist#
@client.command(name="playasongprettyplease")
@cooldown(rate=1, per=5)
async def playasongprettyplease(ctx):
	await ctx.channel.send("Command not done")
	await ctx.channel.send("FuK oFf DowNiE")

#This command will tell send a piece of the poe poem#
@client.command(name="poe", description="Poetic genius", aliases=["poetry", "edgar", "alan"])
@cooldown(rate=1, per=3)
async def Poe(ctx):
	y = random.randint(0, 1850)
	x = random.randint(0, 3)
	if x == 0:
		await ctx.channel.send(theraven[0:y])
		x = random.randint(0, 3)

	if x == 1:
		await ctx.channel.send(theraven_2[0:y])
		x = random.randint(0, 3)

	if x == 2:
		await ctx.channel.send(theraven_3[0:y])
		x = random.randint(0, 3)

	if x == 3:
		await ctx.channel.send(theraven_4[0:y])
		x = random.randint(0, 3)

#This will delete bulk messages#
@client.command(name="prune", description="Bulk deletes messages", aliases=["delete", "bulkdel"],
usage="<number of messages (1-99)>")
async def prune(ctx):
	await ctx.channel.send("Command not done")
	await ctx.channel.send("FuK oFf DowNiE")

#This will send a random riddle that will have an answer#
@client.command(name="riddle", description="Gives you a brain teaser")
@cooldown(rate=1, per=3)
async def riddle(ctx):
  
  x = random.randint(0,2)

  await ctx.channel.send(riddles_answers[x][0])
  await ctx.channel.send(riddles_answers[x][1])

#This will send a line of the troofax#
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

#This will send a piece of the simpdiss or imbest#
@client.command(name="spek", description="spits actual fire.", aliases=["sp3k"])
@cooldown(rate=1, per=3)
async def spek(ctx):
	x = random.randint(0, 1)
	if x == 0:
			await ctx.channel.send(simpdiss)
	if x == 1:
			await ctx.channel.send(imbest)
			await ctx.channel.send(imbest_2)

#When the cooldown happens this will tell the how much is left#
@client.event
async def cool(ctx):
	x = CommandOnCooldown(retry_after = x)
	await ctx.channel.send(CommandOnCooldown)

client.run('ODA0NzQ4NjIwNjQ1NDAwNjI2.YBQ2jg.dchqLTFIyKFOMCpXZ2VDiMuJTTk')
