import os
import discord
from discord.ext import commands
import getEDT

from googleapiclient.discovery import build
from google.oauth2 import service_account

bot = commands.Bot(command_prefix="$")


@bot.event
async def on_ready():
    print("rdy")

#Help
@bot.command(name='aled')
async def sendHelp(ctx):
    embedVar = discord.Embed(title="Aled", description="T'es un bouffon ? tkt cette aide va te permettre de kiffer la vibe\n", color=0x00ff00)
    embedVar.add_field(name="delete", value="Supprime tous les messages du bot", inline=False)
    embedVar.add_field(name="deleteAll", value="Supprime tous les messages du serveur", inline=False)
    embedVar.add_field(name="shrek", value="Envoie la plus belle image 4K disponible sur Internet", inline=False)
    embedVar.add_field(name="love", value="Envoie du love", inline=False)
    embedVar.set_footer(text="Hesite pas me faire des remarques (seulement positives sinon t mor)")

    await ctx.channel.send(embed=embedVar)


#Delete Bot's messages
@bot.command(name='delete')
async def deleteBot(ctx):
    messages = await ctx.channel.history().flatten()
    for m in messages:
        if (str(m.author) == "Bot App#7796"):
            await m.delete()
        elif (m.content.startswith("$")):
            await m.delete()

# Delete all messages
@bot.command(name='deleteAll')
async def deleteAll(ctx):
    messages = await ctx.channel.history().flatten()
    for m in messages:
        await m.delete()

#send a shrek pic
@bot.command(name='shrek')
async def sendShrek(ctx):
    await ctx.channel.send(file=discord.File("shrek.jpg"))

# send love
@bot.command(name='love')
async def sendLove(ctx, dest: discord.Member):
    if (dest == None):
        await ctx.channel.send("Choisi ta victime bg <3")
    else:
        await ctx.channel.send('jtm bg {}'.format(dest.mention))

# send love
@bot.command(name='hitman')
async def hitman(ctx, dest: discord.Member):

    SERVICE_ACCOUNT_FILE = 'keys.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    hitman = '18ruCwTm2IDwFKwBVT4FGQyXIZ2Z5Wq67oslwKM_lvq0'
    service = build('sheets', 'v4', credentials=credentials)
    sheet = service.spreadsheets()

    if (str(dest) == "Spaaz#1765"):
        result1 = sheet.values().get(spreadsheetId=hitman, range="Hitman 1 - Spaaz!C11").execute()
        result2 = sheet.values().get(spreadsheetId=hitman, range="Hitman 2 - Spaaz!C20").execute()
        await ctx.channel.send('Spaaz est a : \n {} de Hitman 1 \n {} de Hitman 2'.format(result1.get("values")[0][0], result2.get("values")[0][0]))
    elif (str(dest) == "LayZ#1501"):
        result1 = sheet.values().get(spreadsheetId=hitman, range="HITMAN MEGA FEUILLE!C17").execute()
        result2 = sheet.values().get(spreadsheetId=hitman, range="HITMAN MEGA FEUILLE!C34").execute()
        result3 = sheet.values().get(spreadsheetId=hitman, range="HITMAN MEGA FEUILLE!C50").execute()
        await ctx.channel.send('LayZ est a : \n {} de Hitman 1 \n {} de Hitman 2 \n {} de Hitman 3'.format(result1.get("values")[0][0], result2.get("values")[0][0], result3.get("values")[0][0]))
    else:
        await ctx.channel.send('Ce joueur est un hater')

@bot.command(name='dm')
async def dm(ctx, dest: discord.Member):
    if (dest == None):
        await ctx.channel.send("Choisi ta victime bg <3")
    else:
        await dest.send("jte baise")

@bot.command(name='cours')
async def cours(ctx):
    cours = getEDT.getCours()
    message = ""
    for seance in cours:
        matiere = seance.get('SUMMARY')
        salle = seance.get('LOCATION')
        heure = seance.get('DTSTART').dt.hour
        min = seance.get('DTSTART').dt.minute

        message += "Heure : " + str(heure+2) + " : " + str(min)  + "\n"
        message += "Matiere : " + matiere  + "\n"
        message += "Salle : " + salle + "\n"
        message += "\n\n"



    await ctx.channel.send(message)



bot.run(os.environ["DISCORD_TOKEN"])

