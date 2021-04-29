import os
import discord
from discord.ext import commands
bot = commands.Bot(command_prefix="$")


@bot.event
async def on_ready():
    print("rdy")

#Help
@bot.command(name='aled')
async def sendHelp(ctx):
    embedVar = discord.Embed(title="Aled", description="T'es un bouffon ? tkt cette aide va te permettre de kiffer la vibe\n", color=0x00ff00)
    embedVar.add_field(name="delete", value="Supprime tout les messages du bot", inline=False)
    embedVar.add_field(name="deleteAll", value="Supprime tout les messages du serveur", inline=False)
    embedVar.add_field(name="shrek", value="Envoie la plus belle image 4K disponible sur Internet", inline=False)
    embedVar.add_field(name="love", value="Envoie du love", inline=False)
    embedVar.set_footer(text="Hesite pas me faire des remarques (seulement positives sinon t mor)")

    await ctx.channel.send(embed=embedVar)

bot.run(os.environ["DISCORD_TOKEN"])

