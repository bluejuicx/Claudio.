import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = False  # Ya no lo necesitas con slash commands
        
        super().__init__(
            command_prefix="!",  # Puedes dejarlo temporalmente o quitarlo
            intents=intents,
            application_id=os.getenv("APPLICATION_ID")  # Opcional pero recomendado
        )
    
    async def setup_hook(self):
        # Cargar cogs
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await self.load_extension(f"cogs.{filename[:-3]}")
        
        # Sincronizar comandos (¡importante!)
        try:
            synced = await self.tree.sync()
            print(f"✅ Se sincronizaron {len(synced)} comandos slash.")
        except Exception as e:
            print(f"❌ Error al sincronizar: {e}")

bot = Bot()

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user} (ID: {bot.user.id})")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="/help"))

bot.run(os.getenv("DISCORD_TOKEN"))
