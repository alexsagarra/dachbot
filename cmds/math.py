
from discord.ext import commands


@commands.group()
async def math(ctx):
    """ math group """
    if ctx.invoked_subcommand is None:
        await ctx.send(f"No, {ctx.subcommand_passed} does not belong to math")  

@math.command()
async def add(ctx, one : int, two : int):
    """ add """
    await ctx.send(one + two)  

@math.command()
async def subtract(ctx, one : int, two : int):
    """ subtract """
    await ctx.send(one - two)  

async def setup(bot):
    bot.add_command(math)

# @add.error
# async def add_error(ctx, error):
#     """ add error handling """
#     if isinstance(error, commands.MissingRequiredArgument):
#         await ctx.send("handled error locally")
