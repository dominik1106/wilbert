import os
import discord

token = os.environ["BOT_TOKEN"]

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(name="r")
async def roll(ctx, dice: str):
    await ctx.respond("Hello!" + dice)

bot.run(token)