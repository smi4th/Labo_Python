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
import command, auto_role, ticket

intents = discord.Intents.all()
class Vue_persistante(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix = '_' , owner_ids = set(owners), intents = intents) #Préfixe du bot
        self.persistent_views_added = False

    async def on_ready(self):
        if not self.persistent_views_added: #mise en place de persistent view sur les boutons => fonctionnent meme apres redemarage
            #Ici on met les add_view pour avoir le bot dans les autres fichiers sans problèmes
            self.persistent_views_added = True
            self.add_view(auto_role.auto_role_class(self))
            self.add_view(ticket.ticket_class.button(self))
            
            self.load_extension("command")
            self.load_extension("auto_role")
            self.load_extension("event_handler")

        print(f"\n\n\n\n\n\n\n\n\nSalut! {self.user} à te servir une boisson chaude! (ID: {self.user.id})") #bot lancé
        print("------")


bot = Vue_persistante()
bot.remove_command('help')

print("\n\n\n\n\n------")
bot.run(TOKEN)
