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

class MyModal(discord.ui.Modal):
    def __init__(self, bot, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.bot = bot

        self.add_item(discord.ui.InputText(label='Titre',placeholder='Titre de ton ticket ici',required=True))
        self.add_item(discord.ui.InputText(style=discord.InputTextStyle.paragraph, label='Description',placeholder='Décris nous ton problème/idée ici',required=True))

    async def callback(self, interaction: discord.Interaction):
        channel = await self.bot.fetch_channel(admin_channel)
        embed = discord.Embed(title=f"Résultat du ticket de {interaction.user.name}")
        embed.add_field(name="Titre du Ticket", value=self.children[0].value,inline=False)
        embed.add_field(name="Description", value=self.children[1].value,inline=False)
        await channel.send(embed=embed,view=button_fermeture_ticket(self.bot)) #J'envoi l'embed dans le salon ticket-admin
        self.stop()
        await interaction.response.send_message(content='Merci, ton ticket à été envoyé aux modos',ephemeral =True)

class ticket_class(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    class button(discord.ui.View):
        def __init__(self,bot, *args):
            super().__init__(timeout=None, *args)
            self.bot = bot

        @discord.ui.button(
                label="Ouvrir un ticket",
                style=discord.ButtonStyle.green,
                emoji="🎫",
                custom_id="persistent_view:open",
            )
        
        async def open(self, button: discord.ui.Button, interaction):
            """
            Fonction callback du bouton
            """
            modal = MyModal(self.bot, title=f'Ticket de {interaction.user.name}🎫') # Je crée un modal
            await interaction.response.send_modal(modal) #J'envoi ce modal à l'utilisateur via l'interaction



class button_fermeture_ticket(discord.ui.View):
        def __init__(self, bot):
            super().__init__(timeout=None)
            self.bot = bot


        @discord.ui.button(
                    label="Fermeture du ticket",
                    style=discord.ButtonStyle.blurple,
                    emoji="🎫",
                    custom_id="fini",
                )

        async def fini(self,  button: discord.ui.Button, interaction):
            """
            Focntion callback du bouton de fermeture du ticket
            """
            message = interaction.message.embeds[0]
            await interaction.message.delete()
            
            channel_log = await self.bot.fetch_channel(admin_channel) # Le channel des logs
            embed = discord.Embed(title=f"Ticket terminé")
            embed.add_field(name="Ticket fermé par l'admin:", value=interaction.user.name, inline=True)
            embed.add_field(name="Ticket ouvert par:", value=message.title[len('Résultat du ticket de '):], inline=True)
            embed.add_field(name='Titre du ticket:', value=message.fields[0].value,inline=False)
            embed.add_field(name="Description:", value=message.fields[1].value,inline=False)
            await channel_log.send(embed=embed)

def setup(bot):
    bot.add_cog(ticket_class(bot))