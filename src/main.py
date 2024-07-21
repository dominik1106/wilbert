import os, re, random, csv
import discord
from table2ascii import table2ascii, PresetStyle

from info import Info, WaffenInfo

token = os.environ["BOT_TOKEN"]

bot = discord.Bot()

info = bot.create_group("info", "Info's übers Spiel")

ruestungen = Info("ruestungs_tabelle.csv")
talente = Info("talente_tabelle.csv")
waffen = WaffenInfo("waffen_tabelle.csv")


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
async def eigenschaft_roll(ctx):
    result = roll_dice(1, 20)
    await ctx.respond(f"{ctx.author.display_name}: `[3w20]` -> `[{result}]`")

@bot.slash_command(name="talent", description="Rollt 3w20")
async def talent_roll(ctx):
    result = roll_dice(3, 20)
    await ctx.respond(f"{ctx.author.display_name}: `[3w20]` -> `[{result}]`")

@bot.slash_command(name="attacke", description="Rollt 2w20, der zweite bestimmt die Trefferzone")
async def attacke_roll(ctx):
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
    return [item for item in ruestungen.display_namen.keys() if item.lower().startswith(ctx.value.lower())]

@info.command(name="ruestungen", description="Lasst euch die Zonen-RS einer Rüstung anzeigen")
@discord.option("rüstung", description="Die Rüstung nach der ihr suchen wollt", autocomplete=get_ruestungen)
async def info_ruestungen(ctx: discord.ApplicationContext, rüstung: str):
    try:
        stats = [ruestungen.display_namen[rüstung].values()]
    except KeyError:
        await ctx.respond("**Rüstung nicht gefunden!**")
        return

    table = table2ascii(
            header= ruestungen.header,
            body= stats,
            first_col_heading=True,
            style= PresetStyle.thin_box
    )

    await ctx.respond(f"```\n{table}\n```")

async def get_waffen(ctx: discord.AutocompleteContext):
    return [item for item in waffen.display_namen.keys() if item.lower().startswith(ctx.value.lower())]

@info.command(name="waffen", description="Lasst euch die Infos einer Waffe anzeigen")
@discord.option("waffe", description="Die Rüstung nach der ihr suchen wollt", autocomplete=get_waffen)
async def info_waffen(ctx: discord.ApplicationContext, waffe: str):
    try:
        stats = [waffen.display_namen[waffe].values()]
    except KeyError:
        await ctx.respond("**Waffe nicht gefunden!**")
        return

    table = table2ascii(
            header= waffen.header,
            body= stats,
            style= PresetStyle.thin_box
    )

    await ctx.respond(f"```\n{table}\n```")

async def get_talente(ctx: discord.AutocompleteContext):
    return [item for item in talente.display_namen.keys() if item.lower().startswith(ctx.value.lower())]

@info.command(name="talente", description="Sucht nach Talenten")
@discord.option("talent", description="Das Talent nach dem ihr suchen wollt", autocomplete=get_talente)
async def info_talente(ctx: discord.ApplicationContext, talent: str):
    try:
        stats = [talente.display_namen[talent].values()]
    except KeyError:
        await ctx.respond("**Talent nicht gefunden!**")
        return

    table = table2ascii(
            header= talente.header,
            body= stats,
            first_col_heading=True,
            style= PresetStyle.thin_box
    )

    await ctx.respond(f"```\n{table}\n```")



bot.run(token)