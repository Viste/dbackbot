import os, sys, paramiko, discord, yadisk
from discord.ext import commands
from conf import data

bot = commands.Bot(command_prefix = data['pref'])
ya = yadisk.YaDisk(token = data['yatoken'])
host = data['host']
user = data['login']
secret = data['pass']
port = data['port']
dst = data['dst']
src = data['src']

@bot.command()
async def ping(ctx):
    await ctx.reply('pong')

@bot.command()
async def backup(ctx):
    client = paramiko.SSHClient()
    client.connect(hostname=host, username=user, password=secret, port=port)
    y.upload(src, dst)
    await ctx.reply('done')

bot.run(data['token'])