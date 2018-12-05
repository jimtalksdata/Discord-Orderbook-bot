import ast
import discord
from discord import Embed, Color
import STATICS

def ex(args, message, client, invoke, sender):
    
    if len(args) is 0:
        buylist = []
        selllist = []
        
        with open("orderlist.txt") as f:
          for line in f:
            entry = ast.literal_eval(line)
            if entry[0] == 'Buy':
                buylist.append(entry)
            elif entry[0] == 'Sell':
                selllist.append(entry)
            else:
                continue
        
        buylist = sorted(buylist,key=itemgetter(3))
        selllist = sorted(selllist,key=itemgetter(3))
                    
        sendstr = """-\n:fire: **ORDERBOOK** :fire:\n\n|WTB|"""

        for entry in buylist:
            sendstr = sendstr + "\n" + str(entry[1])[:-5] + " - " + str(entry[2]) + ' ' + CURRENCY + ' @ ' + str(entry[3]) + ' ' + CURRENCY2

        sendstr = sendstr + "\n\n" + "|WTS|"

        for entry in selllist:
            sendstr = sendstr + "\n" + str(entry[1])[:-5] + " - " + str(entry[2]) + ' ' + CURRENCY + ' @ ' + str(entry[3]) + ' ' + CURRENCY2

        yield from client.send_message(message.channel, sendstr)
    else:
        yield from client.send_message(message.channel, embed=Embed(color=Color.red(), description=(STATICS.INVMARKET)))
