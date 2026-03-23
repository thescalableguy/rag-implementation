from dotenv import load_dotenv
import os
from pathlib import Path

# 👇 Resolve absolute path to .env
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

print("Looking for .env at:", ENV_PATH)

load_dotenv(dotenv_path=ENV_PATH)

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3.2"
DISCORD_WEBHOOK_NOTES = ""

print("✅ settings.py loaded")

print("OLLAMA_URL:", OLLAMA_URL)
print("OLLAMA_MODEL:", OLLAMA_MODEL)
print("DISCORD_WEBHOOK:", DISCORD_WEBHOOK_NOTES)
