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

@bot.command(name='reverse', help='Reverses the message in the command')
async def reverse_string(ctx, *, mssg_rev):
  if ctx.author == bot.user:
    return
  
  await ctx.send(mssg_rev[::-1])

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

"""

@bot.command(name='trivia', help='Simulates a trivia game. (unfinished beta)')
async def trivia_funct(ctx):
  questions = ["What is the capitol of New Jersey?", "Which Star Wars movie did Boba Fett first appear in?", "What was the Japanese name for the NES?"]
  answers = ["Trenton", "Episode V", "Super Famicom"]
  prompt = random.choice(questions)
  questionIndex = questions.index(prompt)

  embedVar = discord.Embed(title="Trivia", desc="", color = 0x00ff00)
  embedVar.add_field(name="Question: ", value=prompt, inline=False)
  await ctx.send(embed=embedVar)
  
"""

keep_alive()
TOKEN = os.environ.get('DISCORD_TOKEN')
GUILD = os.environ.get('DISCORD_GUILD')
bot.run(TOKEN)