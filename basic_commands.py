import settings
import random
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")


class Slapper(commands.Converter):
    def __init__(self, *, use_nicknames) -> None:
        self.use_nicknames = use_nicknames

    async def convert(self, ctx, argument):
        """slapper"""
        someone = random.choice(ctx.guild.members)
        nickname = ctx.author
        if self.use_nicknames:
            nickname = ctx.author
            return f"{nickname} slaps {someone} with {argument}"


def run():
    # print(settings.DISCORD_API_TOKEN)
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")

        for cmd_file in settings.CMDS_DIR.glob("*.py"):
            if cmd_file != "__init.py":
                await bot.load_extension(f"cmds.{cmd_file.name[:-3]}")

    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("handled error globally")

    @bot.command(
        aliases=["p"],
        help="This ist help",
        description="This ist the Description",
        brief="brief",
        enabled=True,
    )
    async def ping(ctx):
        """ping pong"""
        await ctx.send("pong")

    @bot.command()
    async def say(ctx, what="What?"):
        """say"""
        await ctx.send(what)

    @bot.command()
    async def say2(ctx, *what):
        """say"""
        await ctx.send(" ".join(what))

    @bot.command()
    async def choices(ctx, *options):
        """say"""
        await ctx.send(random.choice(options))

    @bot.command()
    async def joined(ctx, who: discord.Member):
        """say"""
        await ctx.send(who.joined_at)

    @bot.command()
    async def slap(ctx, reason: Slapper(use_nicknames=True)):
        """slap"""
        await ctx.send(reason)

    bot.run(settings.DISCORD_API_TOKEN, root_logger=True)


if __name__ == "__main__":
    run()
