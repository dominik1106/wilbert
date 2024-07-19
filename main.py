import os, re, random, csv
import discord
from table2ascii import table2ascii, PresetStyle

token = os.environ["BOT_TOKEN"]

bot = discord.Bot()


import csv

with open("Ruestungs_Zonen.csv", "r", encoding="utf-8-sig") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=";")

    ruestungen_header = csv_reader.fieldnames
    ruestungen = list(csv_reader)

ruestungen_namen: str = [item["Name"] for item in ruestungen]


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

@bot.slash_command(name="r", description="Format: 3w20 oder 3d20")
async def roll(ctx, input: str):
    try:
        amount, sides = parse_dice_input(input)
        result = roll_dice(amount=amount, sides=sides)

        await ctx.respond(f"{ctx.author.display_name}: `[{input}]` -> `[{result}]`")
    except ValueError:
        await ctx.respond("Wrong format!")

@bot.slash_command(name="eigenschaft", description="Rollt 1w20")
async def eigenschaft(ctx):
    result = roll_dice(1, 20)
    await ctx.respond(f"{ctx.author.display_name}: `[3w20]` -> `[{result}]`")

@bot.slash_command(name="talent", description="Rollt 3w20")
async def talent(ctx):
    result = roll_dice(3, 20)
    await ctx.respond(f"{ctx.author.display_name}: `[3w20]` -> `[{result}]`")

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

    await ctx.respond(f"{ctx.author.display_name}: AT: `[{result}]` Trefferzone: `[{treffer_zone}]` `({zone})`")

async def get_ruestungen(ctx: discord.AutocompleteContext):
    return 

@bot.slash_command(name="ruestungen")
@discord.option("rüstung", choices=ruestungen_namen, required=False)
async def ruestung(
        ctx: discord.ApplicationContext,
        rüstung: str
):
    if rüstung == None:
        stats = [item.values() for item in ruestungen]
    else:
        stats = [next(item for item in ruestungen if item["Name"] == rüstung).values()]

    table = table2ascii(
            header= ruestungen_header,
            body= stats,
            first_col_heading=True,
            style= PresetStyle.thin_box
    )

    await ctx.respond(f"```\n{table}\n```")


bot.run(token)