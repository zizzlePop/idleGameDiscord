# bot.py
import os
import random
import discord 
from replit import db
from discord.ext import commands
from keep_alive import keep_alive



intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='!', intents = intents)

def update_playerlist(player_member):
  if "players" in db.keys():
    players = db["players"]
    players.append(player_member)
    db["players"] = players
  else:
    db["players"] = [player_member]

def remove_player(index):
  players = db["players"]
  if len(players) > index:
    del players[index]
  db["players"] = players


#this should run when the bot comes online and connects to the server
@bot.event
async def on_ready():
  for guild in bot.guilds:
    if guild.name == GUILD:
      break

  print(
    f'{bot.user.name} has connected to discord! \n',
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

@bot.command(name='setup')
async def bot_setup(ctx):
  for guild in bot.guilds:
    if guild.name == GUILD:
      break

  async for member in guild.fetch_members(limit=150):
      update_playerlist(member.id)

@bot.command(name='list')
async def list_users(ctx):
  players = []
  if "players" in db.keys():
    players = db["players"]
  await ctx.send(players)

@bot.command(name='removeBots')
async def remove_bots(ctx, numOfBots: int):
  for i in range(numOfBots):
    remove_player(0)

keep_alive()
TOKEN = os.environ.get('DISCORD_TOKEN')
GUILD = os.environ.get('DISCORD_GUILD')

bot.run(TOKEN)

