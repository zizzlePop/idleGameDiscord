#trivia.py
import os
import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command(name='trivia', help='Simulates a trivia game.')
async def trivia_funct(ctx):
  questions = ["What is the capitol of New Jersey?", "Which Star Wars movie did Boba Fett first appear in?", "What was the Japanese name for the NES?"]
  answers = ["Trenton", "Episode V", "Super Famicom"]
  prompt = random.choice(questions)
  questionIndex = questions.index(prompt)

#  await ctx.send(prompt)

#  reply = 

#  if answers.index(reply) == questionIndex:
#    ctx.send("Correct answer!")   
#  else:
#    ctx.send("Incorrect answer, please try again.")

TOKEN = os.environ.get('DISCORD_TOKEN')
bot.run(TOKEN)
