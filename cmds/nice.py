from discord.ext import commands


@commands.group()
async def nice(ctx):
    """nice group"""
    if ctx.invoked_subcommand is None:
        await ctx.send(f"No, {ctx.subcommand_passed} does not belong to nice")


@nice.command()
async def getguild(ctx):
    """get guild id"""

    guildid = bot.guilds[0].id
    if guildid is None:
        guildid = "123"
    print(guildid)
    logger.info(f"nice Guild ID: {guildid}")

    msg = f"nice Guild ID: {str(guildid)}"
    await ctx.send(msg)


@nice.command()
async def plus(ctx, one: int, two: int):
    """add"""
    await ctx.send(one + two)


async def setup(bot):
    bot.add_command(nice)


# @add.error
# async def add_error(ctx, error):
#     """ add error handling """
#     if isinstance(error, commands.MissingRequiredArgument):
#         await ctx.send("handled error locally")
