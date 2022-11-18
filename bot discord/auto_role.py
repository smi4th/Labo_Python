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

class auto_role_class(discord.ui.View):

    def __init__(self, bot, ctx=None):
        super().__init__(timeout=None)

        if ctx is not None:
            self.guild = ctx.guild

            self.select = Select(options=[
                discord.SelectOption(label=year.name,value=year.name) for year in [discord.utils.get(self.guild.roles,name = f"{i} année") for i in range(1,6)]
                ],custom_id="auto_role")
            self.add_item(self.select)
            self.select.callback = self.callback

            self.years = [discord.utils.get(self.guild.roles,name = f"{i} année") for i in range(1,6)]

    async def callback(self,interaction: discord.Interaction):
        role = discord.utils.get(interaction.guild.roles, name=self.select.values[0])
        if role in interaction.user.roles:
            await interaction.response.send_message(f'Tu as déjà le role {role}!', ephemeral=True)
        else:
            for el in self.years:
                if el in interaction.user.roles:
                    await interaction.user.remove_roles(el)
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f'Tu as maintenant le role {role}!', ephemeral=True)

def setup(bot):
    bot.add_view(auto_role_class(bot))