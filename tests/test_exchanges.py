import unittest
from crypto_exchange import Binance, OKX, Bitget, Kucoin, MEXC, GateIO, ExchangeConfig


class TestExchanges(unittest.TestCase):
    def setUp(self):
        self.binance_config = ExchangeConfig(api_key='test_key', api_secret='test_secret')
        self.okx_config = ExchangeConfig(api_key='test_key', api_secret='test_secret', api_passphrase='test_passphrase')
        self.bitget_config = ExchangeConfig(api_key='test_key', api_secret='test_secret',
                                            api_passphrase='test_passphrase')
        self.kucoin_config = ExchangeConfig(api_key='test_key', api_secret='test_secret',
                                            api_passphrase='test_passphrase')
        self.mexc_config = ExchangeConfig(api_key='test_key', api_secret='test_secret')
        self.gateio_config = ExchangeConfig(api_key='test_key', api_secret='test_secret')

    def test_binance_init(self):
        binance = Binance(self.binance_config)
        self.assertEqual(binance.base_url, 'https://api.binance.com')

    def test_okx_init(self):
        okx = OKX(self.okx_config)
        self.assertEqual(okx.base_url, 'https://www.okx.com')

    def test_bitget_init(self):
        bitget = Bitget(self.bitget_config)
        self.assertEqual(bitget.base_url, 'https://api.bitget.com')

    def test_kucoin_init(self):
        kucoin = Kucoin(self.kucoin_config)
        self.assertEqual(kucoin.base_url, 'https://api.kucoin.com')

    def test_mexc_init(self):
        mexc = MEXC(self.mexc_config)
        self.assertEqual(mexc.base_url, 'https://api.mexc.com')

    def test_gateio_init(self):
        gateio = GateIO(self.gateio_config)
        self.assertEqual(gateio.base_url, 'https://api.gateio.ws')


if __name__ == '__main__':
    unittest.main()
