import datetime  #tell the exact time
import discord
from discord.ext import tasks, commands  #bot commmand usage
from dotenv import load_dotenv  #Package link to token
import os
import random  #Random choice
import robotGif  #Gif of mrRobot
from discord.ext.commands import has_permissions, MissingPermissions #Permissions


load_dotenv(dotenv_path="token.0")
bot = commands.Bot(command_prefix="!")
bot.remove_command("help")


#Consol message bot online + activity
@bot.event
async def on_ready():
    game = discord.Game("Coding...")
    await bot.change_presence(status=discord.Status.online, activity=game)
    print("Bot is now online as {0.user}.".format(bot))

@tasks.loop(minutes=50.0)
async def auto_send():
    channel = await bot.fetch_channel("912768323907891263")
    user_id = "<@329906866756911105>"
    await channel.send(f"{user_id} **You know what to do !**\n" "https://10fastfingers.com/typing-test/french\n""https://www.keybr.com/")


#If the bot enter a command, it doesnt work
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

#This command send the few commands that the bot can do
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Help commands :",
    description="**!mrRobot =** Send a random Mr Robot gif from a personnal data base.\n"
    "**!join =** To make me join your voice channel, dont forget to be on a channel. *[Only for admin]*\n"
    "**!leave =** To make me leave the channel if i am in a channel. *[Only for admin]*"
    "**!about =** To learn about the history of the Sam Esmail bot.",
    color=0xC63232)
    embed.set_footer(text=f"Last update : 27/11/2021")
    await ctx.send(embed=embed)
    
#This command talk about the bot
@bot.command()
async def about(ctx):
    embed = discord.Embed(title="**About this bot :**",
    description="This bot is a little project who publish and react to commands, he can post, for now, randoms Mr.Robot Gifs, and others stuff.\n"
                "Originally this bot was a learning python project, and he evolved to what the creator imagines.\n", color=0xC63232)
    embed.set_footer(text=f"Creator : Natsuki#4977 \n"
                          f"Created in : 2021")
    await ctx.send(embed=embed)

#Randomly take a mrRobot gif from pyfile
@bot.command()
async def mrRobot(ctx):
    chosen_image = random.choice(robotGif.robotG)

    embed = discord.Embed(color=0xC63232, timestamp=datetime.datetime.utcnow())
    embed.set_image(url=chosen_image)
    embed.set_footer(text=f"Voici ton gif {ctx.author.name}")

    await ctx.send(embed=embed)


#Command for join
@bot.command(pass_context = True)
@has_permissions(administrator=True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send(f"{ctx.author.mention} Tu dois être dans un salon vocal pour que je puisse te rejoindre.")


#Command for leave
@bot.command(pass_context = True)
@has_permissions(administrator=True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send(f"{ctx.author.mention} Je viens de quitter le salon vocal.")
    else:
        await ctx.send(f"{ctx.author.mention}Je ne suis pas dans un salon vocal.")

auto_send.start()
bot.run(os.getenv("TOKEN"))
