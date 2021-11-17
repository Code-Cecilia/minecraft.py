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

class Config(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")

    @commands.command(name='changeprefix', aliases=['setprefix'], description='Sets the server-specific prefix')
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def change_prefix_func(self, ctx, prefix):
        with open('./config/prefixes.json', 'r') as f:
            data = json.load(f)

        data[str(ctx.guild.id)] = prefix

        with open('./config/prefixes.json', 'w') as f:
            json.dump(data, f, indent=4)
        await ctx.send(f'The prefix for this server has changed to {prefix}')

def setup(bot):
    bot.add_cog(Config(bot))