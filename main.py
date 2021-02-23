# bot.py
import os
import random
import discord 
from discord.ext import commands
from keep_alive import keep_alive


bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
  for guild in bot.guilds:
    if guild.name == GUILD:
      break

  print(
    f'{bot.user.name} has connected to discord! \n'
    f'{guild.name}(id: {guild.id})'
  )

@bot.command(name='reverse')
async def reverse_string(ctx, *mssg_rev):
  response = ""
  if ctx.author == bot.user:
    return
  
  for arg in mssg_rev:
    response = response + (arg[::-1]) + ""
  
  await ctx.send(response)

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name='trivia')
async def trivia_funct(ctx):
  await ctx.send("trivia is working")

keep_alive()
TOKEN = os.environ.get('DISCORD_TOKEN')
GUILD = os.environ.get('DISCORD_GUILD')
bot.run(TOKEN)
