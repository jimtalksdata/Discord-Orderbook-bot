import ast
import discord
from discord import Embed, Color
import STATICS


def ex(args, message, client, invoke, sender):
    if len(args) is 2:
        amtnyzo = args[0]
        amtsats = args[1]
        try:
            amtnyzo = float(amtnyzo)
            amtsats = float(amtsats)
        except:
            # yield from client.send_message(message.channel, embed=Embed(color=Color.red(), description=(STATICS.HELPER)))
            print('No numbers')

        with open("orderlist.txt") as f:
            count = 0
            for line in f:
                entry = ast.literal_eval(line)
                if entry[1] == sender in line:
                    count = count + 1

        if count < STATICS.MAXORDERS:
            if type(amtnyzo) is float and type(amtsats) is float:
                if amtnyzo > 0 and amtsats > 0:
                    cal = round((amtnyzo * amtsats) / 100000000, 8)
                    cal = format(cal, '.8f')
                    sendstr = """-\n:loudspeaker: New order added: \n**Sell** {0} Nyzo for {1} sats each = {2} BTC\n\n:fire: **ORDERBOOK** :fire:\n\n|WTB|""".format(
                        amtnyzo, amtsats, cal)

                    neworder = ['Sell', sender, amtnyzo, amtsats, cal]
                    with open("orderlist.txt", "a") as f:
                        f.write("{}".format(neworder))
                        f.write("\n")

                    with open("orderlist.txt") as f:
                        for line in f:
                            entry = ast.literal_eval(line)
                            print(entry[0])
                            if entry[0] == 'Buy':
                                sendstr = sendstr + "\n" + str(entry[1])[:-5] + " - " + str(
                                    entry[2]) + ' ' + STATICS.CURRENCY + ' @ ' + str(entry[3]) + ' ' + STATICS.CURRENCY2
                            else:
                                continue

                    sendstr = sendstr + "\n\n" + "|WTS|"

                    with open("orderlist.txt") as f:
                        for line in f:
                            entry = ast.literal_eval(line)
                            print(entry[0])
                            if entry[0] == 'Sell':
                                sendstr = sendstr + "\n" + str(entry[1])[:-5] + " - " + str(
                                    entry[2]) + ' ' + STATICS.CURRENCY + ' @ ' + str(entry[3]) + ' ' + STATICS.CURRENCY2
                            else:
                                continue

                        yield from client.send_message(message.channel, sendstr)
                else:
                    yield from client.send_message(message.channel,
                                                   embed=Embed(color=Color.red(), description=(STATICS.HELPER)))

            else:
                yield from client.send_message(message.channel,
                                               embed=Embed(color=Color.red(), description=(STATICS.HELPER)))

        elif count >= STATICS.MAXORDERS:
            yield from client.send_message(message.channel, embed=Embed(color=Color.red(), description=(STATICS.INMAX)))
    else:
        yield from client.send_message(message.channel, embed=Embed(color=Color.red(), description=(STATICS.HELPER)))
