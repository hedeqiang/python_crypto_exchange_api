from dataclasses import dataclass
from typing import Optional


@dataclass
class ExchangeConfig:
    api_key: str
    api_secret: str
    base_url: Optional[str] = None
    api_passphrase: Optional[str] = None
