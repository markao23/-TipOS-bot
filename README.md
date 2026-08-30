# TipOS-bot

![Build](https://img.shields.io/badge/build-example-lightgrey) ![Python](https://img.shields.io/badge/python-3.11-blue) ![discord.py](https://img.shields.io/badge/discord.py-2.7.1-black) ![License](https://img.shields.io/badge/license-MIT-green)

Documentação profissional para o bot TipOS-bot — um bot em Python baseado em slash commands (Application Commands) para controle de versões, automação de releases e ferramentas de manutenção de projetos.

Sumário
- Visão geral
- Recursos
- Arquitetura (diagrama UML)
- Instalação
- Configuração (.env)
- Execução local
- Exemplos de slash commands (cogs)
- Versionamento e changelog
- CI / GitHub Actions
- Segurança e boas práticas
- Contribuição

Visão geral

O TipOS-bot é um bot para Discord implementado em Python com `discord.py` que expõe um conjunto de slash commands para suporte a operações de versionamento (tags, releases), controle de deploy, e comandos administrativos para equipes de desenvolvimento.

Principais objetivos:
- Fornecer comandos claros para criar e gerenciar versões (SemVer) e releases
- Automatizar criação de changelogs e integração com CI/CD
- Permitir scripts administrativos e integrações com banco de dados para histórico

Recursos
- Comandos de versionamento: `version bump`, `release create`, `changelog generate`
- Comandos administrativos: `reload`, `sync`, `stats`
- Permissões baseadas em roles
- Persistência opcional (Postgres via SQLAlchemy/asyncpg)
- Suporte a Docker e CI (exemplo de GitHub Actions)

Arquitetura

O diagrama de arquitetura está em [docs/diagrams/architecture.puml](docs/diagrams/architecture.puml). Para gerar a imagem localmente:

```bash
# Baixar plantuml.jar (se ainda não tiver):
wget https://github.com/plantuml/plantuml/releases/latest/download/plantuml.jar -O plantuml.jar

# Gerar PNG a partir do .puml
java -jar plantuml.jar -tpng -o docs/diagrams docs/diagrams/architecture.puml
```

No repositório incluímos a fonte PlantUML em [docs/diagrams/architecture.puml](docs/diagrams/architecture.puml). O CI do projeto também contém um job de exemplo que gera o diagrama automaticamente.

Componentes principais
- `src/` — código fonte do bot
- `src/core/config.py` — carregamento de configurações com `pydantic`
- `src/cogs/` — pasta recomendada para cogs/handlers (exemplos abaixo)
- `docs/` — documentação e diagramas

Instalação (desenvolvimento)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Configuração (.env)

Crie um arquivo `.env` na raiz de `TipOS-bot/` com as variáveis abaixo (NUNCA commit):

```
DISCORD_TOKEN=seu_token_aqui
DATABASE_URL=postgresql+asyncpg://user:pass@localhost/dbname
ENVIRONMENT=development
LOG_LEVEL=INFO
```

Execução local

```bash
source .venv/bin/activate
python -m src.main
```

Exemplos de slash commands (cogs)

Exemplo de cog minimal para versionamento (`src/cogs/versioning.py`):

```python
from discord import app_commands
from discord.ext import commands
import discord

class Versioning(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="version-bump", description="Aumenta a versão seguindo SemVer")
    @app_commands.describe(part="Parte a incrementar: major, minor ou patch")
    async def version_bump(self, interaction: discord.Interaction, part: str):
        # Lógica de bump aqui (ex.: ler versão, calcular nova, criar tag)
        await interaction.response.send_message(f"Versão incrementada ({part})")

async def setup(bot: commands.Bot):
    await bot.add_cog(Versioning(bot))
```

Como carregar cogs no `src/main.py` (exemplo mínimo):

```python
from discord.ext import commands
import importlib
import pathlib

async def load_cogs(bot: commands.Bot):
    cogs_dir = pathlib.Path(__file__).parent / "cogs"
    for file in cogs_dir.glob("*.py"):
        module = f"src.cogs.{file.stem}"
        await bot.load_extension(module)

# no setup do bot: await load_cogs(bot)
```

Versionamento e changelog

Adote SemVer (MAJOR.MINOR.PATCH) e commits convencionais para geração de changelog automático (ex.: `conventional-changelog`). Para releases automatizadas, integre o comando `release create` do bot ao pipeline de CI para criar a release no GitHub com changelog gerado.

CI / GitHub Actions (exemplo)

Há um workflow de exemplo em `.github/workflows/ci.yml` que executa lint/test e gera o diagrama PlantUML. Ajuste conforme suas necessidades.

Segurança e boas práticas
- Nunca commite `.env` nem tokens.
- Use secrets do GitHub Actions para `DISCORD_TOKEN` e `DATABASE_URL`.
- Registre eventos sensíveis e implemente rotação de tokens quando necessário.

Contribuição

1. Fork e crie um branch `feature/descricao`
2. Abra PR com descrição clara e changelog
3. Use commits atômicos e mensagens convencionais

Licença

Este repositório segue a licença MIT (adicionar arquivo LICENSE se desejar).

----
Gerado automaticamente: documentação base para um bot de slash commands em Python focado em versionamento e automação. Se quiser, eu crio também exemplos de `src/cogs/*` reais e gero o diagrama PNG para você.
