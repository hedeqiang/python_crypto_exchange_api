# Crypto Exchange API

A Python framework for accessing multiple cryptocurrency exchanges' APIs.

# Supported Exchanges
- Binance
- OKX
- Bitget
- Kucoin
- MEXC
- Gate.io
- Bybit
- Kraken

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
bybit_config = ExchangeConfig(api_key='your_bybit_api_key', api_secret='your_bybit_api_secret')
kraken_config = ExchangeConfig(api_key='your_kraken_api_key', api_secret='your_kraken_api_secret')

# get exchanges to the manager
binance = manager.add_exchange(ExchangeName.BINANCE, binance_config).get_exchange()
okx = manager.add_exchange(ExchangeName.OKX, okx_config).get_exchange()
bitget = manager.add_exchange(ExchangeName.BITGET, bitget_config).get_exchange()
kucoin= manager.add_exchange(ExchangeName.KUCOIN, kucoin_config).get_exchange()
mexc = manager.add_exchange(ExchangeName.MEXC, mexc_config).get_exchange()
gate = manager.add_exchange(ExchangeName.GATEIO, gateio_config).get_exchange()
bybit = manager.add_exchange(ExchangeName.BYBIT, bybit_config).get_exchange()
kraken = manager.add_exchange(ExchangeName.KRAKEN,kraken_config).get_exchange()
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
response = binance.send_request( 'GET', '/api/v3/ticker/price', params={'symbol': 'BTCUSDT'}, signed=False)
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
response = binance.send_request('POST', '/sapi/v1/capital/withdraw/apply', params=params, signed=True)
print(response)

```
### OKX
#### Public Endpoint (Market Data)
```python
# Get the ticker information for BTC/USDT
response = okx.send_request('GET', '/api/v5/market/ticker', params={'instId': 'BTC-USDT'}, signed=False)
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
response = okx.send_request('POST', '/api/v5/asset/withdrawal', params=params, signed=True)
print(response)
```

### Bitget
#### Public Endpoint (Market Data)
```python
# Get the latest price of BTC/USDT
response = bitget.send_request('GET', '/api/v2/spot/market/tickers', params={'symbol': 'BTCUSDT'}, signed=False)
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
response = bitget.send_request('POST', '/api/v2/spot/wallet/withdrawal', params=params, signed=True)
print(response)
```

### Kucoin
#### Public Endpoint (Market Data)
```python
# Get all ticker information
response = kucoin.send_request('GET', '/api/v1/market/allTickers', signed=False)
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
response = kucoin.send_request('POST', '/api/v1/withdrawals', params=params, signed=True)
print(response)
```

### MEXC
#### Public Endpoint (Market Data)
```python
# Get the latest price of BTC/USDT
response = mexc.send_request('GET', '/api/v3/ticker/price', params={'symbol': 'BTCUSDT'}, signed=False)
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
response = mexc.send_request('POST', '/api/v3/capital/withdraw', params=params, signed=True)
print(response)
```

### Gate.io
#### Public Endpoint (Market Data)
```python
# Get the ticker information for BTC/USDT
response = gate.send_request('GET', 'v4/spot/currency_pairs/BTC_USDT', signed=False)
print(response)
```
#### Private Endpoint (Withdraw Funds)
```python
# Withdraw funds from your Gate.io account
params = {
    'withdraw_order_id':'123456', 
    'currency': 'BTC',
    'address': 'your_btc_address',
    'amount': '0.01',
    'chain': 'BTC',
}
response = gate.send_request('POST', '/api/v4/withdrawals', params=params, signed=True)
print(response)
```

### Bybit
#### Public Endpoint (Market Data)
```python
# Get the latest price of BTC/USDT
response = bybit.send_request('GET', '/v5/market/tickers', params={'symbol': 'BTCUSDT', 'category': 'spot'},
                                  signed=False)
print(response)
```

#### Private Endpoint (Withdraw Funds)
```python
# Withdraw funds from your Bybit account
params = {
    'coin': 'BTC',
    'chain': 'BTC',
    'address': 'your_btc_address',
    'amount': '0.01',
    'timestamp': 1672196561407,
    'forceChain': 0,
    'accountType': 'FUND'
}
response = bybit.send_request('POST', '/v5/asset/withdraw/create', params=params, signed=True)
print(response)
```

### Kraken

#### Public Endpoint (Market Data)

```python
# Get the latest price of BTC/USD
response = kraken.send_request('GET', '/0/public/Ticker', params={'pair': 'XBTUSD'}, signed=False)
print(response)
```

#### Private Endpoint (Withdraw Funds)
```python
# Withdraw funds from your Kraken account
params = {
    'asset': 'BTC',
    'key': 'your_withdrawal_key',
    'amount': '0.01',
    'address':'your_btc_address'
}
response = kraken.send_request('POST', '/0/private/Withdraw', params=params, signed=True)
print(response)
```
...

# License
This project is licensed under the MIT License.