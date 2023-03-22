import discord,json,os
from discord.ext import commands
from discord.commands import Option
from discord.commands import slash_command

class Info(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    info = discord.SlashCommandGroup(
        "info",
        "查詢資訊",
        guild_only=True,
        default_member_permissions=discord.Permissions(8),
    )

    @info.command(descrtiption="查看機器人資訊")
    async def bot(self,ctx):
        pass

    @info.command(description="查詢用戶資訊")
    async def user(self,ctx,用戶:Option(discord.User,"要查詢的用戶")):
        pass

    @info.command(description="查詢群組資訊")
    async def guild(self,ctx):
        pass

def setup (bot):
    bot.add_cog(Info(bot))