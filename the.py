import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.command(help='Displays Rule 11')
async def r11(ctx):
    await ctx.send('Please refrain from asking for or giving assistance with installing, using, or obtaining pirated software.')

@bot.command(help="dispways wuwe 11")
async def wuwe11(ctx):
    await ctx.send('pwease wefwain fwom asking fow ow giving assistance with instawwing, using, ow obtaining piwated softwawe')

@bot.command(help="dispways wuwe 11")
async def w11(ctx):
    await ctx.send('pwease wefwain fwom asking fow ow giving assistance with instawwing, using, ow obtaining piwated softwawe')

@bot.command(help="Bans a member.")
async def ban(ctx, member : discord.Member):
    if member.name == 'Joe Bot':
        await ctx.send('no')
    else:
        thing = [':hammer: ', member.mention, ' has been banned.']
        x = ''.join(thing)
        await ctx.send(x)

@bot.command(help="Super bans a member.")
async def superban(ctx, member : discord.Member):
    if member.name == 'Joe Bot':
        await ctx.send('no')
    else:
        thing = [member.mention, ' is now SUPER BANNED. :thumbup: https://nintendohomebrew.com/assets/img/banned.gif']
        x = ''.join(thing)
        await ctx.send(x)

@bot.command(help="Takes away help from a member.")
async def takehelp(ctx, member : discord.Member):
        thing = [member.mention, ' can no longer access the help channels.']
        x = ''.join(thing)
        await ctx.send(x)

@bot.command(help="Displays information about the bot.", )
async def about(ctx):
    await ctx.send('Joe Bot Version v5.5')
    await ctx.send('--------------------------------')
    await ctx.send('This is a JOE Bot, all hail Joe!')

@bot.command(help="idk", pass_context=True)
async def furry(ctx):
    area = ctx.message.channel
    await ctx.send(file=discord.File(r'C:\Users\Evanz\real.png'))

@bot.command(help="sends a random image from evans furry folder")
async def evansfurryfolder(ctx):
    x=random.randint(1, 10)
    if x==1:
        await ctx.send(file=discord.File(r'C:\FURRY\hahaevanlol.png'))
    elif x==2:
        await ctx.send(file=discord.File(r'C:\FURRY\furry-protest-mcdonalds.png'))
    elif x==3:
        await ctx.send(file=discord.File(r'C:\FURRY\GrandDAD.jpg'))
    elif x==4:
        await ctx.send(file=discord.File(r'C:\FURRY\thismotherFUCKER.jpg'))
    elif x==3:
        await ctx.send(file=discord.File(r'C:\FURRY\classicuberefrence.jpg'))
    elif x==4:
        await ctx.send(file=discord.File(r'C:\FURRY\purodrawing.jpg'))
    elif x==5:
        await ctx.send(file=discord.File(r'C:\FURRY\birdlee.png'))
    elif x==6:
        await ctx.send(file=discord.File(r'C:\FURRY\FURRY.gif'))
    elif x==7:
        await ctx.send(file=discord.File(r'C:\FURRY\realhewwospotted.png'))
    elif x==8:
        await ctx.send(file=discord.File(r'C:\FURRY\research.png'))
    elif x==9:
        await ctx.send(file=discord.File(r'C:\FURRY\ohdeargod.png'))


@bot.command(help="Make the Joe Bot say what you want it to!")
async def say(ctx, *args):
    arguments = ' '.join(args)
    await ctx.send(arguments)

bot.run('token')
