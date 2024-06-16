import discord
from discord.ext import commands
import json
import random

with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

TOKEN = config['TOKEN']
PREFIX = config['PREFIX']
RESPONSES = config['RESPONSES']

intents = discord.Intents().all()

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if 'хохол' in message.content.lower():
        response = random.choice(RESPONSES)
        await message.channel.send(response)
    await bot.process_commands(message)

@bot.command()
async def test(ctx, *args):
    await ctx.send(args[0])

@bot.command()
async def summa(ctx, num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except:
        await ctx.send('Error')
        return
    result = num1 + num2
    await ctx.send(str(result))

bot.run(TOKEN)