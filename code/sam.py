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

#If the bot enter a command, it doesnt work
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message) #put after the on_message bot.event, to not block bot.command




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
@bot.command(pass_context=True)
async def robot(ctx):
    if ctx.channel.id != 917380109776867328:
        return

    chosen_image = random.choice(robotGif.robotG)

    embed = discord.Embed(color=0xC63232, description=f"**Voici ton gif {ctx.author.name} :**", timestamp=datetime.datetime.utcnow())
    embed.set_image(url=chosen_image)

    msg = await ctx.send(embed=embed)
    await msg.add_reaction("🤖")



#start of the role reaction command
@bot.command(pass_context=True)
@has_permissions(administrator=True)
async def role(ctx):
    if ctx.channel.id != 917449216899555358:
        return
    embed = discord.Embed(
        title="**Did you watched Mr.Robot ?**",
        color=0xC63232
    )

    embed.add_field(name="0️⃣ Never", value="Never watched (i should now)", inline=False)
    embed.add_field(name="1️⃣ Season 1", value="Currently watching season 1", inline=False)
    embed.add_field(name="2️⃣ Season 2", value="Currently watching season 2", inline=False)
    embed.add_field(name="3️⃣ Season 3", value="Currently watching season 3", inline=False)
    embed.add_field(name="4️⃣ Season 4", value="Currently watching season 4", inline=False)
    embed.add_field(name="🔄 All seasons", value="I watched all seasons", inline=False)

    msg = await ctx.send(embed=embed)
    #never
    await msg.add_reaction("0️⃣")
    #season 1
    await msg.add_reaction("1️⃣")
    #season 2
    await msg.add_reaction("2️⃣")
    #season 3
    await msg.add_reaction("3️⃣")
    #season 4
    await msg.add_reaction("4️⃣")
    #season 5
    await msg.add_reaction("🔄")

@bot.event
async def on_raw_reaction_add(payload):
    ourMessageID = 917514374690770974

    if ourMessageID == payload.message_id:
        member = payload.member
        guild = member.guild

        emoji = payload.emoji.name
        if emoji == "0️⃣":
            role = discord.utils.get(guild.roles, name="never watched")
        elif emoji == "1️⃣":
            role = discord.utils.get(guild.roles, name="watching season 1")
        elif emoji == "2️⃣":
            role = discord.utils.get(guild.roles, name="watching season 2")
        elif emoji == "3️⃣":
            role = discord.utils.get(guild.roles, name="watching season 3")
        elif emoji == "4️⃣":
            role = discord.utils.get(guild.roles, name="watching season 4")
        elif emoji == "🔄":
            role = discord.utils.get(guild.roles, name="already watched all")
        await member.add_roles(role)

@bot.event
async def on_raw_reaction_remove(payload):
    ourMessageID = 917514374690770974

    if ourMessageID == payload.message_id:
        guild = await(bot.fetch_guild(payload.guild_id))
        emoji = payload.emoji.name
        if emoji == "0️⃣":
            role = discord.utils.get(guild.roles, name="never watched")
        elif emoji == "1️⃣":
            role = discord.utils.get(guild.roles, name="watching season 1")
        elif emoji == "2️⃣":
            role = discord.utils.get(guild.roles, name="watching season 2")
        elif emoji == "3️⃣":
            role = discord.utils.get(guild.roles, name="watching season 3")
        elif emoji == "4️⃣":
            role = discord.utils.get(guild.roles, name="watching season 4")
        elif emoji == "🔄":
            role = discord.utils.get(guild.roles, name="already watched all")
        member = await(guild.fetch_member(payload.user_id))
        if member is not None:
            await member.remove_roles(role)
        else:
            print("Member not found")
#end of the role reaction command



#clear command
@bot.command(pass_context=True)
@has_permissions(manage_messages=True)
async def clear(ctx, amount: str):

    if amount == "all":
        await ctx.channel.purge()

    else:
        await ctx.channel.purge(limit=(int(amount)+ 1))




bot.run(os.getenv("TOKEN"))
