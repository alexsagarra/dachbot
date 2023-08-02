import discord
from discord.ext import commands
import settings
from pprint import pprint as pp

logger = settings.logging.getLogger(__name__)

# Intents.voice_states is required!


class TemporaryVoice(commands.Cog):
    temporary_channels = []
    channel_list = ["DMZ", "DMZ(3)", "MP", "Geb.21", "Beutegeld", "Rebirth", "Koop"]

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(
        self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState
    ):
        possible_channel_name = f"{member.nick}'s area"
        if after.channel:
            join_name = after.channel.name.strip(" erstellen")
            join_name = join_name.strip("➕")
            print("join_name:", join_name)

            if join_name in TemporaryVoice.channel_list:
                prefix = join_name
                user = str(member.name)
                category_id = after.channel.category_id
                category = self.bot.get_channel(category_id)
                guild_id = self.bot.guilds[0]
                typecount = {}

                for channel in self.bot.guilds[0].voice_channels:
                    for channeltypes in TemporaryVoice.channel_list:
                        typecount[channeltypes] = []
                        if channeltypes in channel.name:
                            typecount[channeltypes].append(channel)

                pp(typecount[join_name])
                print("strip1", join_name)
                count = len(typecount[join_name]) + 1
                print("count: ", join_name, " --> ", count)

                # for guild in self.bot.guilds:
                #     for channel in guild.voice_channels:
                #         if channel.category_id == category_id
                #             print("------------------------")
                #             pp(channel)

                # count = 1

                possible_channel_name = f"{prefix} #{str(count)} - {user}"
                pp(after.channel)
                temp_channel = await after.channel.clone(name=possible_channel_name)
                await member.move_to(temp_channel)
                self.temporary_channels.append(temp_channel.id)

        if before.channel:
            if before.channel.id in self.temporary_channels:
                if len(before.channel.members) == 0:
                    await before.channel.delete()


async def setup(bot):
    await bot.add_cog(TemporaryVoice(bot))
