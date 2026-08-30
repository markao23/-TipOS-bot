import discord
from discord.ext import commands
from discord import app_commands

import discord
from discord.ext import commands


class PingCog(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @app_commands.command(name = "ping",
        description = "Verifica a latencia do bot e o status do bot")
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)

        embed=discord.Embed(title="🏓Pong!", description="conexão com o servidor estabelecida", color=discord.Color.brand_green())
        embed.add_field(name="Latencia (API)", value=f"**{latency}ms**", inline=False)
        embed.set_footer(text="Vercontrol Bot • Sistema Operacional Ágil")
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(PingCog(bot))