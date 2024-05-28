# main.py (Python)

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.message_mentions = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

initial_extensions = ['cogs.giveaway_cog']

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

    with open('token.txt', 'r') as file:
        token = file.read()

    bot.run(token)