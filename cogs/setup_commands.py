import discord
from discord_slash import cog_ext, SlashContext
from discord.ext import commands

class SetupCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        pass

    @cog_ext.cog_slash(name="test", guild_ids=[892459726212837427])
    async def _test(self, ctx: SlashContext):
        await ctx.send("test")

def setup(bot):
    bot.add_cog(SetupCommands(bot))