import asyncio
import os
import random

import discord
from discord.ext import commands
from pathlib import Path

intents = discord.Intents(messages=True, bans=True, guilds=True)
intents.reactions = True
intents.guild_messages = True
intents.typing = True
intents.members = True
intents.voice_states = True

import json

with open('./config/config.json', 'r') as configFile:
    data = json.load(configFile)
    token = data.get("token")

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}")

description = ''' A minecraft discord bot for the guild Hyakuya Family. DISCLAIMER: You will absolute zero support with this bot if you try to host it.'''

class NewHelpName(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            embed = discord.Embed(
                description=page, color=discord.Color.random())
            embed.set_thumbnail(url=bot.user.avatar_url)
            embed.set_footer(text='')
            await destination.send(embed=embed)

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or('!c'),
    description=description,
    owner_id=219410026631135232,
    case_insensitive=True,
    intents=intents,
    help_command=NewHelpName()
)

@bot.event
async def on_ready():
    print('Logged in as', bot.user.name)
    print("Bot ID:", bot.user.id)
    print('Bot latency:', bot.latency * 1000, 2)
    print('Running discord.py version ' + discord.__version__)

if __name__ == "__main__":
    for file in os.listdir(cwd + "/cogs"):
        if file.endswith(".py") and not file.startswith("_"):
            bot.load_extension(f"cogs.{file[:-3]}")
    bot.load_extension("jishaku")
    bot.run(bot.config_token)