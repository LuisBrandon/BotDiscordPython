import os

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


from discord.ext import commands
bot = commands.Bot(command_prefix='$')

@bot.command(name='invocar',help='Invoca a un usuario')
async def summonUser(ctx):
    fraseParaInvocar = "Invocando a no se quién"

    response = fraseParaInvocar
    await ctx.send(response)

@bot.command(name="hola",help="Saludar")
async def saludar(ctx):
    fraseParaResponder = "hola pichita como estamos"

    response = fraseParaResponder
    await ctx.send(response)





bot.run(TOKEN)