from kucoin_futures.client import Market
from kucoin_futures.client import Trade
from kucoin_futures.client import User

class TradeClient():
    """
    https://github.com/Kucoin/kucoin-futures-python-sdk
    """

    def __init__(self, auth_config, sandbox=True):
        self.api_key = auth_config["kucoin_futures_api_key"]
        self.api_secret = auth_config["kucoin_futures_api_secret"]
        self.api_passphrase = auth_config["kucoin_futures_api_passphrase"]
        self.market = Market(is_sandbox=sandbox)
        self.trade = Trade(
            key=self.api_key,
            secret=self.api_secret,
            passphrase=self.api_passphrase,
            is_sandbox=sandbox
        )
        self.user = User(
            key=self.api_key,
            secret=self.api_secret,
            passphrase=self.api_passphrase,
            is_sandbox=sandbox
        )

    """
    We are interested in getting:
    1. Capital
    2. Positions
    3. Submit Orders
    4. Get OHLCV data etc...
    """

    def get_account_details(self):
        pass

    def get_account_summary(self):
        pass

    def get_account_capital(self):
        pass

    def get_account_positions(self):
        pass

    def get_account_trades(self):
        pass

    def get_account_orders(self):
        pass

    def get_ohlcv(self, instrument, count, granularity):
        pass

    def market_order(self, inst, order_config={}):
        pass
