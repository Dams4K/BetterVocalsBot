import json
import discord
from discord.ext import commands
from utils.references import References

class BetterVocals(commands.Bot):
    def __init__(self):
        super().__init__(get_prefix, case_insensitive=True, help_command=None, intents=discord.Intents.all())
        self.events = {
            "join": self.on_member_join,
            "leave": self.on_member_leave
        }


    async def on_ready(self):
        print("ready")


    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        before_channel: discord.VoiceChannel = before.channel
        after_channel: discord.VoiceChannel = after.channel
        channel = None
        event = ""

        if before_channel == None and after_channel != None: 
            channel: discord.VoiceChannel = after_channel
            event = "join"
        elif before_channel != None and after_channel == None:
            channel: discord.VoiceChannel = before_channel
            event = "leave"

        if channel == None or event == "" or channel.category == None: return
        category: discord.CategoryChannel = channel.category

        voice_channels = [channel for channel in category.channels if type(channel) == discord.VoiceChannel]

        await self.events[event](category, voice_channels, channel)


    async def on_member_join(self, category: discord.CategoryChannel, voice_channels: list, current_channel: discord.VoiceChannel):
        for voice_ch in voice_channels:
            if voice_ch.members == []:
                return
        
        await current_channel.clone()

    
    async def on_member_leave(self, category: discord.CategoryChannel, voice_channels: list, current_channel: discord.VoiceChannel):
        if current_channel.members == [] and len(voice_channels) > 1:
            await current_channel.delete()
    
    def get_prefix(bot, message):
        return References.BOT_PREFIX
