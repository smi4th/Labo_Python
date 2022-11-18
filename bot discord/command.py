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
import auto_role, ticket

class command_class(commands.Cog):
    
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        

    @commands.is_owner()
    @commands.command()
    async def embed(self,ctx,*args):
        """
        Fonction permettant de généré des embed
        string : *args -> Les éléments de l'embed triées de tel manière :
        discord.ApplicationContext : ctx -> Discord application command interaction

        usage : _embed <Titre> <Content> [Titre2] [Content2] ...
        """
        await ctx.message.delete() # Je supprime le message originel
        info = [arg for arg in args] # Je stock les les arguments dans une liste
        if len(info) < 2 or len(info)%2 != 0:
            # Si la liste fait moins de 2 éléments alors, c'est qu'il n'y a pas assez d'éléments
            # Ou, si la liste ne contient pas la paire titre + contenu
            await ctx.send(content='_embed <Titre> <Content> [Titre2] [Content2] ...', delete_after= 5.0)
        else:
            channel = await self.bot.fetch_channel(ctx.message.channel.id) # Le channel d'ou a été envoyé la commande
            # D'après l'usage (définit par mes soins) le premier élément doit être le titre
            # Le suivant la description
            embed = discord.Embed(title=info[0], description=info[1],colour=0x6BFF33) # Je crée un embed avec ses infos là
            for i in range(2,len(info)-1,2):
                # Je commence donc ensuite par les infos suivantes (à partir de 2 dans la liste)
                # Et je vais de 2 en 2 car à chaque ligne crée dans l'embed il y a le binome titre + contenu
                embed.add_field(name=info[i], value=info[i+1], inline=False)
            await channel.send(embed=embed)

    @commands.is_owner()
    @commands.command()
    async def info(self,ctx, *args):
        """
        Fonction permettant d'afficher les informations du laboratoire
        discord.ApplicationContext : ctx -> Discord application command interaction
        """
        await ctx.message.delete()
        if len(args) != 3:
            await ctx.send(content='_info "Date" "Lieu" "Ouvert pour"', delete_after= 5.0)
        else:
            embed=discord.Embed(title=str("*** INFO ***"),colour=0x6BFF33,description="Info concernant la date de la prochaine réunion du laboratoire")
            embed.set_thumbnail(url=f"{ctx.guild.icon}")
            embed.set_author(name=f"{self.bot.user.name}",icon_url=f"{self.bot.user.avatar}")
            embed.set_footer(text=f"{ctx.guild}",icon_url=f"{ctx.guild.icon}")
            embed.add_field(name="Date de la prochaine réunion:", value=args[0])
            embed.add_field(name="Lieu:",value=args[1])
            embed.add_field(name="Ouvert pour:", value=args[2])
            await ctx.send(embed=embed)

    @commands.is_owner()
    @commands.command()
    async def repeat(self,ctx, *args):
        """
        Fonction permettant de répéter un message
        discord.ApplicationContext : ctx -> Discord application command interaction
        string : *args -> Le message à répéter
        """
        await ctx.message.delete()
        await ctx.send(' '.join(args))

    @commands.command()
    async def projet(self,ctx):
        """
        Fonction permettant d'afficher les projets du laboratoire
        discord.ApplicationContext : ctx -> Discord application command interaction
        """
        await ctx.message.delete()
        embed=discord.Embed(title=str("*** PROJET ***"),colour=0x6BFF33,description="Voici les projets du laboratoire")
        embed.set_author(name=f"{ctx.guild}",icon_url=f"{self.bot.user.avatar}")
        embed.set_footer(text=f"Cette commande vous permet d'avoir quelques idées de projets et vers qui se référé",icon_url=f"{ctx.guild.icon}")
        embed.add_field(name="Il n'y a pas encore de projet", value="Veuillez patienter", inline=False)
        await ctx.send(embed=embed)

    @commands.is_owner()
    @commands.command()
    async def test(self, ctx):
        await ctx.send(content='JE vous recois',delete_after=5)
        ctx.message.delete()

    @commands.is_owner()
    @commands.command()
    async def restart_role(self,ctx):
        await ctx.message.delete()

        channel = ctx.channel

        await channel.send(content='**Choisissez votre rôle**', view=auto_role.auto_role_class(self.bot,ctx))

    @commands.is_owner()
    @commands.command()
    async def restart_tickets(self,ctx):

        await ctx.message.delete()
        channel = ctx.channel
        embed = discord.Embed(title="Ouverture de ticket",
                                    description='Clique ici pour ouvrir un ticket avec le bot.',
                                    color=0x00ff91)
        await channel.send( content='Tu souhaites signaler un problème? Tu as une demande?\nCliques sur le bouton ci-dessous et remplis le formulaire pour créer un ticket.\n:arrow_down::arrow_down::arrow_down::arrow_down::arrow_down::arrow_down::arrow_down::arrow_down::arrow_down::arrow_down::arrow_down:',
                            embed=embed,
                            view=ticket.ticket_class.button(self.bot)
                        )


    @commands.command()
    @commands.is_owner()
    async def clear(self,ctx, nombre = 0):
        """
        commande permettant de supprimer un certain nombre de message
        int : nombre -> nombre de message à supprimer
        """
        if nombre >= 100:
            await ctx.channel.purge(limit=1)
            await ctx.send(f"Ok, {ctx.author.mention}, c'est bcp trop", delete_after= 5.0)#on signale que c'est delete et on supp le message 5 sec apres^
        else:
            await ctx.channel.purge(limit=nombre+1)#on supp les messages (la var nombre c'est le nb messages supp)
            await ctx.send(f"Ok, {ctx.author.mention}, j'ai supprimé {nombre} messages!", delete_after= 5.0)#on signale que c'est delete et on supp le message 5 sec apres


    @commands.command()
    @commands.is_owner()
    async def rules(self,ctx: commands.Context):
        #J'envoie les règles sous la forme d'un embed
        await ctx.message.delete()
        embed = discord.Embed(title="Règles", description="Voici les règles du serveur", color=0x00ff00)
        embed.add_field(name="🔴 Ce qu'il ne faut pas faire ! 🔴",value="‎")
        for i in range(len(forbidden)):
            embed.add_field(name=f"Règle {i+1} :",value="⛔ " + forbidden[i],inline=False)
        embed.add_field(name="🟢 Ce qu'il faut faire ! 🟢",value="‎")
        for i in range(len(allow)):
            embed.add_field(name=f"Règle {i+1} :",value="✅ " + allow[i],inline=False)
        embed.add_field(name="🔵 Astuces ! 🔵",value="‎")
        for i in range(len(protips)):
            embed.add_field(name=f"Astuce {i+1} :",value="🛡️ " + protips[i],inline=False)
        embed.set_footer(text="Merci de respecter ces règles !")
        await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(command_class(bot))