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
    channel = await bot.fetch_channel("917380109776867328")
    user_id = "<@329906866756911105>"
    await channel.send(f"{user_id} **You know what to do !**\n" "https://10fastfingers.com/typing-test/french\n""https://www.keybr.com/")


#If the bot enter a command, it doesnt work
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)


#This help command help the user to find commands available for the bot
@bot.command()
async def help(ctx):
    if ctx.channel.id != 917380109776867328:
        return

    embed = discord.Embed(
        description="**Here's the few commands you can use for the bot :**",
        color=0xC63232
    )

    embed.set_author(name="Sam esmail commands :", icon_url="https://assets.wprock.fr/emoji/joypixels/512/2753.png")
    embed.set_image(url="https://i.pinimg.com/originals/db/db/ba/dbdbbad5798bfc3ff27a499dc5ca2b30.gif")

    embed.add_field(name="!robot", value="Send a random Mr Robot gif from a personnal data base.", inline=False)
    embed.add_field(name="!join", value="To make me join your voice channel, dont forget to be on a channel. *[Only for admin]*", inline=False)
    embed.add_field(name="!leave", value="To make me leave the channel if i am in a channel. *[Only for admin]*", inline=False)
    embed.add_field(name="!about", value="To learn about the story of Sam Esmail bot.", inline=False)

    embed.set_footer(text=f"Last update : 06/12/2021")
    await ctx.send(embed=embed)


#This command talk about the bot
@bot.command()
async def about(ctx):
    if ctx.channel.id != 917380109776867328:
        return

    embed = discord.Embed(
        title="**About this bot :**",
        description="This bot is a little project who can publish and react to commands, he can post, for now, randoms Mr.Robot Gifs, and others stuff.\n\n"
                    "Originally this bot was a learning python project, and he evolved to what the creator imagines.\n",
        color=0xC63232
    )

    embed.set_image(url="https://giffiles.alphacoders.com/206/206739.gif")
    embed.set_footer(text=f"Creator : Natsuki#4977 \n"
                          f"Created in : 2021")
    await ctx.send(embed=embed)

#Randomly take a mrRobot gif from pyfile
@bot.command()
async def robot(ctx):
    if ctx.channel.id != 917380109776867328:
        return

    chosen_image = random.choice(robotGif.robotG)

    embed = discord.Embed(color=0xC63232, description=f"**Voici ton gif {ctx.author.name} :**", timestamp=datetime.datetime.utcnow())
    embed.set_image(url=chosen_image)

    await ctx.send(embed=embed)


auto_send.start()
bot.run(os.getenv("TOKEN"))
