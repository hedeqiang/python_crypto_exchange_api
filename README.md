# Crypto Exchange API

A Python framework for accessing multiple cryptocurrency exchanges' APIs.

# Supported Exchanges
- Binance
- OKX
- Bitget
- Kucoin
- MEXC
- Gate.io

## Installation

```bash
pip install crypto_exchange_api
```

## Usage
First, import the necessary modules and set up your API configurations:
```python
from crypto_exchange import CryptoAPIManager, ExchangeConfig, ExchangeName

# Create a manager instance
manager = CryptoAPIManager()

# Set up your API configurations
binance_config = ExchangeConfig(api_key='your_binance_api_key', api_secret='your_binance_api_secret')
okx_config = ExchangeConfig(api_key='your_okx_api_key', api_secret='your_okx_api_secret', api_passphrase='your_okx_api_passphrase')
bitget_config = ExchangeConfig(api_key='your_bitget_api_key', api_secret='your_bitget_api_secret', api_passphrase='your_bitget_api_passphrase')
kucoin_config = ExchangeConfig(api_key='your_kucoin_api_key', api_secret='your_kucoin_api_secret', api_passphrase='your_kucoin_api_passphrase')
mexc_config = ExchangeConfig(api_key='your_mexc_api_key', api_secret='your_mexc_api_secret')
gateio_config = ExchangeConfig(api_key='your_gateio_api_key', api_secret='your_gateio_api_secret')

# Add exchanges to the manager
manager.add_exchange(ExchangeName.BINANCE, binance_config)
manager.add_exchange(ExchangeName.OKX, okx_config)
manager.add_exchange(ExchangeName.BITGET, bitget_config)
manager.add_exchange(ExchangeName.KUCOIN, kucoin_config)
manager.add_exchange(ExchangeName.MEXC, mexc_config)
manager.add_exchange(ExchangeName.GATEIO, gateio_config)
```

### Binance
```python
response = manager.send_request(ExchangeName.BINANCE, 'GET', '/api/v3/ticker/price', params={'symbol': 'BTCUSDT'}, signed=False)
print(response)
```

### OKX
```python
response = manager.send_request(ExchangeName.OKX, 'GET', '/api/v5/market/ticker', params={'instId': 'BTC-USDT'}, signed=True)
print(response)
```

...

# License
This project is licensed under the MIT License.