# 🛠️ Environment Setup Guide

Complete this **before Day 1**. Total time: ~1–2 hours including downloads.

## 1. Core tools

| Tool | Min version | Check | Install |
|------|-------------|-------|---------|
| Python | 3.11+ | `python3 --version` | https://www.python.org/downloads |
| Poetry | 1.7+ | `poetry --version` | https://python-poetry.org/docs/#installation |
| Git | 2.30+ | `git --version` | https://git-scm.com/downloads |
| Docker Desktop | 24+ | `docker --version` | https://docs.docker.com/get-docker |
| VS Code | any | `code --version` | https://code.visualstudio.com |

### Windows users — use WSL2
All terminal commands target bash (macOS/Linux). On Windows:
```powershell
wsl --install        # run PowerShell as Administrator, then reboot
```
Then use the Ubuntu terminal. Docker Desktop integrates with WSL2 automatically.

## 2. Install Poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
# add to PATH (bash):
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc && source ~/.bashrc
poetry --version
```

## 3. Get your API keys

Copy the template and fill it in:
```bash
cp .env.example .env
```

| Key | Used from | Where to get it | Free? |
|-----|-----------|-----------------|-------|
| `OPENAI_API_KEY` | Day 2 onward | https://platform.openai.com | pay-as-you-go (≈$5 covers the sprint) |
| `PINECONE_API_KEY` | Day 2 | https://www.pinecone.io | free tier |
| `TAVILY_API_KEY` | Day 4 | https://app.tavily.com | free tier |
| `LANGCHAIN_API_KEY` | Day 7 | https://smith.langchain.com | free tier |

> ⚠️ **Never commit `.env`.** It is already in `.gitignore`. Keys committed to a public repo are found by bots within seconds.

## 4. Per-project dependencies

Each project manages its own dependencies. Inside any project folder:
```bash
poetry install          # if the project has a pyproject.toml
# or
pip install -r requirements.txt
```

## 5. Verify everything

```bash
python3 --version       # 3.11+
poetry --version
docker run --rm hello-world
git --version
```

## 6. Can't run Docker locally?

Use **GitHub Codespaces** (free 60 hrs/month) — Docker-in-Docker works there — or **Google Colab** for the notebook-style tasks (no Docker). See each project README for notes.

## Cost expectations

The entire sprint costs **under ~$10** in API usage if you use the recommended `gpt-4o-mini` model and the free tiers. Every project bounds its calls and uses caching where possible.
