import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(
            command_prefix="!",
            intents=intents
        )

    async def setup_hook(self):
        # Cargar los comandos (cogs)
        await self.load_extension("cogs.custommessage")
        
        # Sincronizar comandos slash
        try:
            synced = await self.tree.sync()
            print(f"✅ Se sincronizaron {len(synced)} comandos.")
        except Exception as e:
            print(f"❌ Error sincronizando: {e}")

bot = Bot()

@bot.event
async def on_ready():
    print(f"✅ Bot en línea como {bot.user}")
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, 
        name="/custommessage"
    ))

bot.run(os.getenv("DISCORD_TOKEN"))
