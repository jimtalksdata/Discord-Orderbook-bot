import ast
import discord
from discord import Embed, Color
import STATICS

def ex(args, message, client, invoke, sender):

    if len(args) is 0:
        yield from client.send_message(message.channel,
                                       embed=Embed(color=Color.blue(), description=(STATICS.HELP)))
    else:
        yield from client.send_message(message.channel, embed=Embed(color=Color.red(), description=(STATICS.INVALIDHELP)))

