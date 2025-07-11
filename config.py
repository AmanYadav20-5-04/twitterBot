from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    """Configuration loaded from environment variables."""
    promised_up: float = float(os.getenv("PROMISED_UP", "1000"))
    promised_down: float = float(os.getenv("PROMISED_DOWN", "1000"))
    twitter_username: str = os.getenv("USERNAME", "")
    twitter_password: str = os.getenv("PASSWORD", "")
    headless: bool = os.getenv("HEADLESS", "False").lower() in {"1", "true", "yes"}
    wait_timeout: int = int(os.getenv("WAIT_TIMEOUT", "30"))
