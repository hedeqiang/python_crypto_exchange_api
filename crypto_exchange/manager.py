from typing import Dict, Any, Optional
from .exchanges import ExchangeName, ExchangeFactory, ExchangeConfig, Exchange


class CryptoAPIManager:
    def __init__(self):
        self.exchanges: Dict[ExchangeName, Exchange] = {}

    def add_exchange(self, exchange_name: ExchangeName, config: ExchangeConfig):
        exchange = ExchangeFactory.create_exchange(exchange_name, config)
        self.exchanges[exchange_name] = exchange

    def send_request(self, exchange_name: ExchangeName, method: str, endpoint: str,
                     params: Optional[Dict[str, Any]] = None, signed: bool = True) -> Dict[str, Any]:
        if exchange_name not in self.exchanges:
            raise ValueError(f"Exchange {exchange_name} is not added.")
        return self.exchanges[exchange_name].send_request(method, endpoint, params, signed)
