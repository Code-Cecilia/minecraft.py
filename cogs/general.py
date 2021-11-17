from discord.ext import commands
import os
import asyncio
import datetime 
from datetime import datetime
import discord

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")

    @commands.command(
        name="Info"
    )
    @commands.guild_only()
    async def information(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        embed = discord.Embed(
                title="Information", colour=member.color, timestamp=datetime.utcnow(), description="The server is currently whitelisted as it is being developed so is this bot.\nThe modpack is Enigmatica 2 Light and it is avaliable for download in GDLauncher and Curseforge.")
        embed.add_field(name="Server IP:", value="play.yuichiro.club", inline=False)
        embed.add_field(name="Online Players:", value="UNDER CONSTRUCTION | type playerlist in <#894100344949334026>", inline=False)
        embed.add_field(name="Commands", value="Type !help", inline=False)
        
        await ctx.send(embed=embed)

    @commands.command(
        name="ping",
        description="Shows the bot latency"
    )
    @commands.guild_only()
    async def ping(self, ctx):
        await ctx.send(f"{'Hello, the current latency is `{0}`'.format(round(self.bot.latency * 1000, 2))}ms")

def setup(bot):
    bot.add_cog(General(bot))