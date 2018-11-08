import ast
import discord
from discord import Embed, Color
import STATICS

def ex(args, message, client, invoke, sender):

    if len(args) is 0:
        sendstr = """-\n:fire: **ORDERBOOK** :fire:\n\n|WTB|"""

        with open("orderlist.txt") as f:
            for line in f:
                entry = ast.literal_eval(line)
                print(entry[0])
                if entry[0] == 'Buy':
                    sendstr= sendstr + "\n" + str(entry[1])[:-5] + " - " + str(entry[2]) + ' ' + STATICS.CURRENCY + ' @ ' + str(entry[3]) + ' ' + STATICS.CURRENCY2
                else:
                    continue

        sendstr = sendstr + "\n\n" + "|WTS|"

        with open("orderlist.txt") as f:
            for line in f:
                entry = ast.literal_eval(line)
                if entry[0] == 'Sell':
                    sendstr = sendstr + "\n" + str(entry[1])[:-5] + " - " + str(entry[2]) + ' ' + STATICS.CURRENCY + ' @ ' + str(entry[3]) + ' ' + STATICS.CURRENCY2
                else:
                    continue

        yield from client.send_message(message.channel, sendstr)
    else:
        yield from client.send_message(message.channel, embed=Embed(color=Color.red(), description=(STATICS.INVMARKET)))
