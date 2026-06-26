import discord
from discord import app_commands
from discord.ext import commands

# Vista con botón
class RepeatView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)  # El botón no desaparece

    @discord.ui.button(label="Repetir Mensaje", style=discord.ButtonStyle.green, emoji="🔁")
    async def repeat(self, interaction: discord.Interaction, button: discord.ui.Button):
        mensaje = "¡Hola! Este es un mensaje repetido con el botón 🔁"
        await interaction.response.send_message(mensaje)


# Cog (grupo de comandos)
class CustomMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="custommessage", description="Envía un mensaje con botón")
    async def custommessage(self, interaction: discord.Interaction, texto: str = "Mensaje por defecto"):
        embed = discord.Embed(
            title="📢 Mensaje Personalizado",
            description=texto,
            color=discord.Color.blue()
        )
        
        view = RepeatView()
        await interaction.response.send_message(embed=embed, view=view)


async def setup(bot: commands.Bot):
    await bot.add_cog(CustomMessage(bot))
