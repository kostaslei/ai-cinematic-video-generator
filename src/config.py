import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY      = os.getenv("OPENAI_API_KEY")

POWERFUL_MODEL      = "gpt-5.1"
STRONG_MODEL        = "gpt-4.1"
BALANCED_MODEL      = "gpt-4.1-mini"

DEFAULT_MAX_TOKENS  = 4000