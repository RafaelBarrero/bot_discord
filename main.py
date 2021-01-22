# bot.py
import os
import random

import discord
from discord.ext import commands

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!', case_insensitive=True)


@bot.event
async def on_ready():
    guild_found = discord.utils.find(lambda g: g.name == GUILD, bot.guilds)
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild_found.name}(id: {guild_found.id})'
    )


@bot.command(name='99', help='Responde con una cita aleatoria de Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
        'Title of you sex tape'
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)


@bot.command(name='c', help='Manda a una persona al canal de "Que me caigooo"')
async def caigo(ctx):
    author = ctx.message.author
    mencion = ctx.message.mentions
    if len(mencion) == 0:
        await ctx.send("Menciona a alguien, cara de red")
    elif len(mencion) == 1:
        if author.voice:
            persona = ctx.message.mentions[0]
            canal_caida = discord.utils.get(ctx.guild.channels, name='Que me caigoooo')
            try:
                await persona.move_to(canal_caida)
                await ctx.send("TIRIRIRIRI. QUE ME CAIGOOOO")
            except discord.errors.HTTPException:
                await ctx.send(f"{persona.mention} no está, imbesil")
        else:
            await ctx.send("Entra al canal, COBARDE")
    else:
        await ctx.send("Menciona sólo a una persona, tonto")


@bot.command(name='rafa', help='Responde si Rafa sigue vivo o no')
async def rafa(ctx):
    rafa_mention = '<@205283670209200129>'
    await ctx.send(f"{rafa_mention} sigue vivo :'c")


@bot.command(name='thanos', help='Comprueba si Thanos te ha matado o no')
async def thanos(ctx):
    author = ctx.message.author
    thanos_quote = [
        'Fuiste asesinado por Thanos, por el bien del universo :(',
        'Thanos te perdonó :D'
    ]

    response = random.choice(thanos_quote)
    await ctx.send(f"{author.mention} {response}")


@bot.command(name='d', help='Lanza un dado. Argumentos: Caras y número de veces')
async def roll_dice(ctx, *args):
    count = 1
    if args:
        dice = int(args[0])
        if len(args) == 2:
            tries = int(args[1])
        else:
            tries = 1
        number_list = []
        while count <= tries:
            number = random.randint(1, dice)
            number_list.append(number)
            count += 1
        str_number = ', '.join([f"{number}" for number in number_list])
        await ctx.send(str_number)
    else:
        await ctx.send("Indica que dado quieres tirar")

bot.run(TOKEN)

