# Crypto Exchange API

A Python framework for accessing multiple cryptocurrency exchanges' APIs.

## Installation

```bash
pip install crypto_exchange_api
```

## Usage
```python
from crypto_exchange import CryptoAPIManager, ExchangeConfig, ExchangeName

manager = CryptoAPIManager()

binance_config = ExchangeConfig(api_key='your_binance_api_key', api_secret='your_binance_api_secret')
manager.add_exchange(ExchangeName.BINANCE, binance_config)

response = manager.send_request(ExchangeName.BINANCE, 'GET', '/api/v3/ticker/price', params={'symbol': 'BTCUSDT'}, signed=False)
print(response)

```

## Supported Exchanges
- Binance
- OKX
- Bitget
- Kucoin
- MEXC
- GateIO