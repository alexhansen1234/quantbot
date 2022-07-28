from brokerage.kucoin.futures.TradeClient import TradeClient

class KucoinFutures():

    def __init__(self, auth_config, sandbox=True):
        self.trade_client = TradeClient(auth_config=auth_config, sandbox=sandbox)

    def get_service_client(self):
        pass

    def get_trade_client(self):
        return self.trade_client
