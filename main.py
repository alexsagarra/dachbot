import settings
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")

def run():
    """ running """
    # print(settings.DISCORD_API_TOKEN)
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
        logger.info(f"Guild ID: {bot.guilds[0].id}")
        # bot.tree.copy_global_to(guild=settings.GUILDS_ID)
        # await bot.tree.sync(guild=settings.GUILDS_ID)

        for cmd_file in settings.CMDS_DIR.glob("*.py"):
            if cmd_file != "__init.py":
                await bot.load_extension(f"cmds.{cmd_file.name[:-3]}")
        
        for cmd_file in settings.COGS_DIR.glob("*.py"):
            if cmd_file != "__init.py":
                await bot.load_extension(f"cogs.{cmd_file.name[:-3]}")

    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("handled error globally")

    bot.run(settings.DISCORD_API_TOKEN, root_logger=True)

if __name__ == "__main__":
    run()
