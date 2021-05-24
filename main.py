import discord
import os
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
import asyncio
def wake_up_the_bot():
  from flask import Flask
  from threading import Thread
  app = Flask('')
  @app.route('/')
  def home():
      return "a wild test bot appeared"
  def run():
    app.run(host='0.0.0.0',port=8080)
  t = Thread(target=run)
  t.start()
wake_up_the_bot()
intents = discord.Intents()
intents.all()
intents.guilds = True
intents.members = True
intents.reactions = True
intents.emojis = True
intents.presences = True
intents.messages = True
intents.typing = True
client = discord.Client()
client = commands.Bot(command_prefix = 'test!', intents=intents)
client.remove_command('help')
helpemb = None

@client.event
async def on_ready():
    d = "---------------------------=+# "
    title = d + "Bot Help" + d[::-1]


    global helpemb
    docstringsbeta = list(globals()[command.name].help for command in client.commands)
    docstrings = list(doc if not doc == None else "Hey creator description of some command is missing" for doc in docstringsbeta)
    helpemb=discord.Embed(title=title, description="", color=0xff3300)
    catdict = {}
    for doc in docstrings:
      spl = doc.split("\n")
      aaaaa = None
      try:
        aaaaa = catdict[spl[0]]
      except KeyError:
        aaaaa = ""
      catdict[spl[0]] = aaaaa + "\n".join(spl[1:]) + "\n"
    for i in catdict.keys():
      if i == "secret": continue
      helpemb.add_field(name=i + "\u200b", value=catdict[i][:-1] + "\u200b", inline=False) 
    helpemb.set_footer(text="Made by [name here]")
    print("bot online")

@client.command()
async def help(ctx):
    '''Help
    `test!help`'''
    global helpemb
    await ctx.send(embed=helpemb)


@client.command()
async def ping(ctx):
    '''Music
    `test!ping` - pings evderyone hahaha'''
    await ctx.send("pong!")
@client.command()
async def ping2(ctx):
    '''Music
    `test!ping2` - ololo'''
    await ctx.send("pong!")
@client.command()
async def ping3(ctx, arg1):
    '''Leisure
    `test!ping3 TEXT` - ololo'''
    await ctx.send("pong!")

@client.command()
async def maintenancecommand(ctx):
    '''secret'''
    await ctx.send("pong!")


client.run(os.getenv("TOKEN"))
