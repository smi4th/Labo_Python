import discord
from discord.ext import commands, tasks
from discord.utils import get
from discord.ui import Button, View, Select
import time
import asyncio
from datetime import *
import random
import os
from config import *
import auto_role

class event_class(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.content.startswith("_"): #permet de faire comprendre au bot que un message commençant par _ est une commande
            await self.bot.process_commands(message)

    @commands.Cog.listener()
    async def on_member_join(self,member):
        #fonction de bienvenue
        guild = member.guild
        user_num = len(guild.members)-1 #nombre de membres dans le serveur
        mention=member.mention 
        embed=discord.Embed(title=str("*** Quelqu'un arrive! ***"),colour=0x6BFF33,description=str(f"Bienvenue {mention} dans le {guild}, installe toi!"))
        if member.avatar != None:
            embed.set_thumbnail(url=f"{member.avatar}")
            embed.set_author(name=f"{member.name}",icon_url=f"{member.avatar}")
        else:
            icon = 'https://imgs.search.brave.com/8q2vzpdFmkVX8pvFePnT9a0xfU-i8HKXE7ozolyxSLs/rs:fit:1024:1024:1/g:ce/aHR0cHM6Ly9pLmlt/Z3VyLmNvbS9QUTdE/OUt2LnBuZw'
            embed.set_thumbnail(url=f"{icon}")
            embed.set_author(name=f"{member.name}",icon_url=f"{icon}")
        embed.set_footer(text=f"{member.guild}",icon_url=f"{member.guild.icon}")
        embed.add_field(name="Nom d'utilisateur:", value=member.display_name)
        embed.add_field(name="Nom du serveur:",value=guild)
        embed.add_field(name="Membre numéro:", value=user_num)
        await guild.system_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        mention=member.mention
        guild=member.guild
        embed=discord.Embed(title=str("*** Quelqu'un s'en va! ***"),colour=0x6BFF33,description=str(f"Malheureusement, {mention} a quitté le {guild}, à bientôt!").format(mention=mention, guild=guild))
        if member.avatar != None:
            embed.set_thumbnail(url=f"{member.avatar}")
            embed.set_author(name=f"{member.name}",icon_url=f"{member.avatar}")
        else:
            icon = 'https://imgs.search.brave.com/8q2vzpdFmkVX8pvFePnT9a0xfU-i8HKXE7ozolyxSLs/rs:fit:1024:1024:1/g:ce/aHR0cHM6Ly9pLmlt/Z3VyLmNvbS9QUTdE/OUt2LnBuZw'
            embed.set_thumbnail(url=f"{icon}")
            embed.set_author(name=f"{member.name}",icon_url=f"{icon}")
        embed.set_footer(text=f"{member.guild}",icon_url=f"{member.guild.icon}")
        embed.add_field(name="Nom d'utilisateur:", value=member.display_name)
        embed.add_field(name="Nom du serveur:",value=guild)
        await guild.system_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_unknown_application_command(self, interaction):
        await interaction.response.send_message("Cette commande n'existe pas, ou alors le programmeur (le génie) ne l'a pas encore ajouté", ephemeral=True)


def setup(bot):
    auto_role.setup(bot)