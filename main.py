import asyncio as asyncio
import discord
import SECRETS
from discord import Game, Server, Member, Embed, Color

import STATICS
from commands import cmd_ping, cmd_wtb, cmd_wts, cmd_market, cmd_help, cmd_clear

client = discord.Client()

commands = {

    "ping": cmd_ping,
    "wtb": cmd_wtb,
    "wts": cmd_wts,
    "market": cmd_market,
    "help": cmd_help,
    "clear": cmd_clear

}

@client.event
@asyncio.coroutine
def on_ready():
    print("Bot is logged in succesfully. Running on servers: \n")
    for s in client.servers:
        print(" - %s (%s)" % (s.name, s.id))
    yield from client.change_presence(game=Game(name="Mesh"))

@client.event
@asyncio.coroutine
def on_message(message):
    sender = str(message.author)
    # print(message.content + " - " + message.author.name)
    if message.content.startswith(STATICS.PREFIX):
        invoke = message.content[len(STATICS.PREFIX):].split(" ")[0]
        invoke = invoke.lower()
        args = message.content.split(" ")[1:]
        print("INVOKE: %s\nARGS: %s" % (invoke, args.__str__()[1:-1].replace("'","")))

        if commands.__contains__(invoke):
            yield from commands.get(invoke).ex(args, message, client, invoke, sender)
        else:
            yield from client.send_message(message.channel, embed=Embed(color=Color.red(), description=("The command '%s' is not valid." % invoke)))
            #to send a message to the author directly: yield from client.send_message(message.author, embed=Embed(color=Color.red(), description=("The command '%s' is not valid." % invoke)))
client.run(SECRETS.TOKEN)