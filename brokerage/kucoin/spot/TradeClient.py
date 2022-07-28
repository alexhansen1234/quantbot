from kucoin.client import Client

class TradeClient():

    def __init__(self, auth_config, sandbox=True):
        self.api_key = auth_config["kucoin_api_key"]
        self.api_secret = auth_config["kucoin_api_secret"]
        self.api_passphrase = auth_config["kucoin_api_passphrase"]
        self.client = Client(self.api_key, self.api_secret, self.api_passphrase, sandbox=sandbox)

    """
    We are interested in getting:
    1. Capital
    2. Positions
    3. Submit Orders
    4. Get OHLCV data etc...
    """

    def get_account_details(self):
        try:
            return self.client.get_accounts()
        except Exception as err:
            print(err)

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
