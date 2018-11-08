import discord

def ex(args, message, client, invoke):
    yield from client.send_message(message.channel, "Pong")