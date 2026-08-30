import discord
from discord.ext import commands
import asyncio
import logging
from core.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("TipOS-Bot")

class TipOSBot(commands.Bot):
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
        await self.load_extension("bot.cogs.ping")
        await self.tree.sync()
        logger.info("[TipOS-Bot]: comandos sicronisados com suvesso")

    async def on_ready(self):
        logger.info(f"[TipOS-Bot]: Bot conectado como: {self.user} (ID: {self.user.id})")
        logger.info(f"[TipOS-Bot]: Ambiente atual: {settings.environment}")

async def main():
    bot = TipOSBot()
    
    async with bot:
        await bot.start(settings.discord_token)

# Este "if" também DEVE estar colado no canto esquerdo
if __name__ == "__main__":
    asyncio.run(main())