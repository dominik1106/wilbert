import os
import discord
import re
import random

token = os.environ["BOT_TOKEN"]

bot = discord.Bot()

def parse_dice_input(dice_input):
    pattern = r'(\d+)[dw](\d+)'
    
    match = re.match(pattern, dice_input)
    
    if match:
        # Extract the amount and sides from the match groups
        amount = int(match.group(1))
        sides = int(match.group(2))
        return amount, sides
    else:
        raise ValueError("Input does not match the expected format")
    
def roll_dice(amount, sides):
    result = [random.randint(1, sides) for _ in range(amount)]
    return " ".join(str(x) for x in result)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(name="r")
async def roll(ctx, input: str):
    try:
        amount, sides = parse_dice_input(input)
        result = roll_dice(amount=amount, sides=sides)

        await ctx.respond(f"{ctx.author.display_name}: `[{input}]` Ergebnis: `[{result}]`")
    except ValueError:
        await ctx.respond("Wrong format!")

@bot.slash_command(name="eigenschaft", description="Rollt 1w20")
async def eigenschaft(ctx):
    result = roll_dice(1, 20)
    await ctx.respond(f"{ctx.author.display_name}: Ergebnis: `[{result}]`")

@bot.slash_command(name="talent", description="Rollt 3w20")
async def talent(ctx):
    result = roll_dice(3, 20)
    await ctx.respond(f"{ctx.author.display_name}: Ergebnis: `[{result}]`")

@bot.slash_command(name="attacke", description="Rollt 2w20, der zweite bestimmt die Trefferzone")
async def attacke(ctx):
    result = roll_dice(1, 20)

    treffer_zone = int(roll_dice(1, 20))
    zone = ""

    if treffer_zone in range(1, 7):
        if treffer_zone % 2 == 0:
            zone = "Rechtes Bein"
        else:
            zone = "Linkes Bein"
    elif treffer_zone in range(7, 9):
        zone = "Bauch"
    elif treffer_zone in range(9, 15):
        if treffer_zone % 2 == 0:
            zone = "Schwertarm"
        else:
            zone = "Schildarm"
    elif treffer_zone in range(15, 19):
        zone = "Brust"
    else:
        zone = "Kopf"

    await ctx.respond(f"{ctx.author.display_name}: Ergebnis: `[{result}]` Trefferzone: `[{treffer_zone}]` `({zone})`")


bot.run(token)