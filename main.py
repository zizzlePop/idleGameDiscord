# bot.py
import os
import random
import discord 
import time
from discord.ext import commands
from keep_alive import keep_alive

# Initialize bot
bot = commands.Bot(command_prefix='!')

# Game variables
limitstart = 0
limitend = 0
currencyScore = 0
THREE_HOURS = 10800

# Login event
@bot.event
async def on_ready():
  for guild in bot.guilds:
    if guild.name == GUILD:
      break

  print(
    f'{bot.user.name} has connected to discord! \n'
    f'{guild.name}(id: {guild.id})'
  )

# Reverse a string command
@bot.command(name='reverse', help='Reverses the message in the command')
async def reverse_string(ctx, *, mssg_rev):
  if ctx.author == bot.user:
    return
  
  await ctx.send(mssg_rev[::-1])

# Dice rolling command
@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

# Begin currency generation and initialize game
@bot.command(name='startgame')
async def start_game(ctx):
  limitstart = time.perf_counter()
  embedVar = discord.Embed(title="Welcome traveler!", description="Your new adventure begins today! The adventurer's guild needs your help doing jobs across town, so you can begin making a wage that will allow you to buy more gear and fight monsters. Your time starts now!", color=0xcccc00)
  await ctx.send(embed=embedVar)

@bot.command(name='claim')
async def claim_coin(ctx):
  limitend = time.perf_counter()

  conditionTrue = discord.Embed(title="Claimed Successfully!", color=0x00ff00)
  conditionTrue.add_field(value="Your new balance is %d." % (currencyScore), inline=False)
  conditionTrue.add_field(value="Come back again in 3 hours!", inline=False)
  conditionFalse = discord.Embed(title="Claim Unsuccessful!", color=0xff0000)
  conditionFalse.add_field(value="Please try again in %d minutes" % (THREE_HOURS - (limitend - limitStart)), inline=False)

  if limitend-limitstart == THREE_HOURS:
    currencyScore += 180
    await ctx.send(conditionTrue)
  else:
    await ctx.send(conditionFalse)


keep_alive()
TOKEN = os.environ.get('DISCORD_TOKEN')
GUILD = os.environ.get('DISCORD_GUILD')
bot.run(TOKEN)
