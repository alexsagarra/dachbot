import discord
from discord.ext import commands
import settings
import os
from pprint import pprint as pp

logger = settings.logging.getLogger(__name__)

# Intents.voice_states is required!


class TemporaryVoice(commands.Cog):
    temporary_channels = []
    temporary_categories = []

    def __init__(self, bot):
        self.bot = bot
        self.temp_channels = []

    @commands.Cog.listener()
    async def on_voice_state_update(
        self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState
    ):
        category_id = 1127863272893337640
        guild_id = 853309621091172362

        count_channel = len(self.temp_channels) + 1
        possible_channel_name = f"DMZ #{count_channel}"
        self.temp_channels.append(possible_channel_name)
        # possible_channel_name = f"{member.nick}'s area"

        text_channel_list = []

        for guild in self.bot.guilds:
            pp(guild)
            print("---------------------------------------")
            for channel in guild.voice_channels:
                if channel.category_id == 1127863272893337640:  # DMZ Srachkanäle
                    pp(channel)
                    text_channel_list.append(channel)
        next_channel_number = len(text_channel_list) + 1
        possible_channel_name = (
            after.channel.name.strip(" erstellen")
            + " #"
            + str(next_channel_number)
            + " - "
            + str(member.name)
        )

        if after.channel:
            if after.channel.name == "DMZ erstellen":
                temp_channel = await after.channel.clone(name=possible_channel_name)
                await member.move_to(temp_channel)
                self.temporary_channels.append(temp_channel.id)
            if after.channel.name == "MP erstellen":
                temporary_category = await after.channel.guild.create_category(
                    name=possible_channel_name
                )
                await temporary_category.create_text_channel(name="text")
                temp_channel = await temporary_category.create_voice_channel(name="voice")
                await member.move_to(temp_channel)
                self.temporary_categories.append(temp_channel.id)

        if before.channel:
            if before.channel.id in self.temporary_channels:
                if len(before.channel.members) == 0:
                    await before.channel.delete()
            if before.channel.id in self.temporary_categories:
                if len(before.channel.members) == 0:
                    for channel in before.channel.category.channels:
                        await channel.delete()
                    await before.channel.category.delete()


async def setup(bot):
    await bot.add_cog(TemporaryVoice(bot))
