# bot.py
import os
import random
import discord 
import player
from replit import db
from discord.ext import commands
from keep_alive import keep_alive

client = discord.Client()
guild = discord.Guild()
bot = commands.Bot(command_prefix='!')

def update_playerlist(player_member):
  if "players" in db.keys():
    players = db["players"]
    players.append(player_member)
  else:
    db["players"] = players

def remove_player(index):
  players = db["players"]
  if len(players) > index:
    del players[index]
  db["players"] = players


@client.event
async def on_ready():
  for guild in client.guilds:
    if guild.name == GUILD:
      break

  print(
    f'{client.user.name} has connected to discord! \n'
    f'{guild.name}(id: {guild.id})'
  )

  async for member in guild.fetch_members(limit=150):
    player_obj = player.Player(client, member.id)
    update_playerlist(player_obj)

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

@bot.command(name='list')
async def list_users(ctx):
  players = []
  if "players" in db.keys():
    players = db["players"]
  await ctx.send(players)


keep_alive()
TOKEN = os.environ.get('DISCORD_TOKEN')
GUILD = os.environ.get('DISCORD_GUILD')
bot.run(TOKEN)
