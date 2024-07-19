from typing import Dict, Optional
from .exchanges import ExchangeName, ExchangeFactory, ExchangeConfig, Exchange


class CryptoAPIManager:
    def __init__(self):
        self.exchanges: Dict[ExchangeName, Exchange] = {}
        self.last_added_exchange: Optional[ExchangeName] = None

    def add_exchange(self, exchange_name: ExchangeName, config: ExchangeConfig) -> 'CryptoAPIManager':
        exchange = ExchangeFactory.create_exchange(exchange_name, config)
        self.exchanges[exchange_name] = exchange
        self.last_added_exchange = exchange_name
        return self

    def get_exchange(self, exchange_name: Optional[ExchangeName] = None) -> Exchange:
        if exchange_name is None:
            if self.last_added_exchange is None:
                raise ValueError("No exchange has been added.")
            exchange_name = self.last_added_exchange

        if exchange_name not in self.exchanges:
            raise ValueError(f"Exchange {exchange_name} is not added.")
        return self.exchanges[exchange_name]
