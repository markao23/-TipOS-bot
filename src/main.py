import discord
from discord.ext import commands
import asyncio
import logging
from core.config import settings

logging.basicConfig(lavel=logging.INFO)
logger = logging.getLogger("TipOS-Bot")

class TipOSBot(commands.Cog):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(
            command_prefix="!",
            intents=intents,
            help_command=None
        )

    async def setup_hook(self):
        logger.info("[TipOS-Bot]: Sicronisando os comandos de barra (slash commands)")
        await self.tree.sync()
        logger.info("[TipOS-Bot]: comandos sicronisados com suvesso")

    async def on_ready(self):
        logger.info(f"[TipOS-Bot]: Bot conectado como: {self.user} (ID: {self.user.id})")
        logger.info(f"[TipOS-Bot]: Ambiente atual: {settings.environment}")