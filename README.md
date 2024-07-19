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
### Explanation of the `signed` Parameter
> The `signed` parameter indicates whether the request requires authentication. 
> Public endpoints (such as market data) do not require authentication and can be accessed with signed=False.
> Private endpoints (such as account data or trading) require authentication and must be accessed with signed=True.

## Examples
### Binance
#### Public Endpoint (Market Data)
```python
# Get the latest price of BTC/USDT
response = manager.send_request(ExchangeName.BINANCE, 'GET', '/api/v3/ticker/price', params={'symbol': 'BTCUSDT'}, signed=False)
print(response)
```

#### Private Endpoint (Withdraw Funds)
```python
# Withdraw funds from your Binance account
params = {
    'coin': 'USDT',
    'withdrawOrderId': '123456',
    'amount': 10,
    'network': 'BSC',
    'address': 'your_usdt_address'
}
response = manager.send_request(ExchangeName.BINANCE, 'POST', '/sapi/v1/capital/withdraw/apply', params=params, signed=True)
print(response)

```
### OKX
#### Public Endpoint (Market Data)
```python
# Get the ticker information for BTC/USDT
response = manager.send_request(ExchangeName.OKX, 'GET', '/api/v5/market/ticker', params={'instId': 'BTC-USDT'}, signed=False)
print(response)
```

#### Private Endpoint (Withdraw Funds)
```python
# Withdraw funds from your OKX account
params = {
    'ccy': 'USDT',
    'amt': '10',
    'dest': '4',  # 4 means withdrawal to external address
    'toAddr': 'your_usdt_address',
    'fee': '0.5'
}
response = manager.send_request(ExchangeName.OKX, 'POST', '/api/v5/asset/withdrawal', params=params, signed=True)
print(response)
```

### Bitget
#### Public Endpoint (Market Data)
```python
# Get the latest price of BTC/USDT
response = manager.send_request(ExchangeName.BITGET, 'GET', '/api/v2/spot/market/tickers', params={'symbol': 'BTCUSDT'}, signed=False)
print(response)
```

### Private Endpoint (Withdraw Funds)
```python
# Withdraw funds from your Bitget account
params = {
    'coin': 'USDT',
    'address': 'your_usdt_address',
    'size': '10',
    'tag': '',
    'chain': 'TRX',
    'clientOid': '123456'
}
response = manager.send_request(ExchangeName.BITGET, 'POST', '/api/v2/spot/wallet/withdrawal', params=params, signed=True)
print(response)
```

### Kucoin
#### Public Endpoint (Market Data)
```python
# Get all ticker information
response = manager.send_request(ExchangeName.KUCOIN, 'GET', '/api/v1/market/allTickers', signed=False)
print(response)
```

#### Private Endpoint (Withdraw Funds)
```python
# Withdraw funds from your Kucoin account
params = {
    'currency': 'BTC',
    'address': 'your_btc_address',
    'amount': '0.01',
    'memo': '',
    'chain': 'BTC'
}
response = manager.send_request(ExchangeName.KUCOIN, 'POST', '/api/v1/withdrawals', params=params, signed=True)
print(response)
```

### MEXC
#### Public Endpoint (Market Data)
```python
# Get the latest price of BTC/USDT
response = manager.send_request(ExchangeName.MEXC, 'GET', '/api/v3/ticker/price', params={'symbol': 'BTCUSDT'}, signed=False)
print(response)
```

#### Private Endpoint (Withdraw Funds)
```python
# Withdraw funds from your MEXC account
params = {
    'coin': 'BTC',
    'withdrawOrderId': 'xxxx',
    'address': 'your_btc_address',
    'amount': '0.01',
    'netWork': 'BTC'
}
response = manager.send_request(ExchangeName.MEXC, 'POST', '/api/v3/capital/withdraw', params=params, signed=True)
print(response)
```

### Gate.io
#### Public Endpoint (Market Data)
```python
# Get the ticker information for BTC/USDT
response = manager.send_request(ExchangeName.GATEIO, 'GET', 'v4/spot/currency_pairs/BTC_USDT', signed=False)
print(response)
```
#### Private Endpoint (Withdraw Funds)
```python
# Withdraw funds from your Gate.io account
params = {
    'withdraw_order_id':'123456', # 用户端订单编号,最长32个，输入内容只能包含数字、字母、下划线(_)、中划线(-) 或者点(.)
    'currency': 'BTC',
    'address': 'your_btc_address',
    'amount': '0.01',
    'chain': 'BTC',
}
response = manager.send_request(ExchangeName.GATEIO, 'POST', '/api/v4/withdrawals', params=params, signed=True)
print(response)
```

...

# License
This project is licensed under the MIT License.