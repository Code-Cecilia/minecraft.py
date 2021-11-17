from discord.ext import commands
import os
import json
import asyncio
import datetime 
from datetime import datetime
import discord

with open('./config/config.json') as configFile:
    configs = json.load(configFile)
    prefix = configs.get("prefix")

class Minecraft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")


def setup(bot):
    bot.add_cog(Minecraft(bot))