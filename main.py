import json
import pandas as pd

from dateutil.relativedelta import relativedelta

import quantlib.data_utils as du
import quantlib.general_utils as gu

from subsystems.LBMOM.subsys import Lbmom
from brokerage.oanda.oanda import Oanda

with open("config/auth_config.json", "r") as fp:
    auth_config = json.load(fp)

# df, instruments = du.get_sp500_df()
# df = du.extend_dataframe(traded=instruments, df=df)
# gu.save_file("./Data/data.obj", (df, instruments))

# df, instruments = gu.load_file("./Data/data.obj")
# print(df, instruments)

# with open("./subsystems/LBMOM/config.json", "w") as fp:
#     json.dump({'instruments': instruments}, fp, indent = 4)

# run simulation for 5 years
# VOL_TARGET = 0.20
# sim_start = df.index[-1] - relativedelta(years=5)
# strat = Lbmom(instruments_config="./subsystems/LBMOM/config.json", historical_df=df, simulation_start=sim_start, vol_target=VOL_TARGET)
# strat.get_subsys_pos()

"""
Oanda Trade Client
"""
with open("config/oanda_config.json", "r") as f:
    brokerage_config = json.load(f)

brokerage = Oanda(auth_config=auth_config)
db_instruments = brokerage_config["CURRENCY"]

print(db_instruments)

poll_df = pd.DataFrame()

for db_inst in db_instruments:
    df = brokerage.get_trade_client().get_ohlcv(instrument=db_inst, count=100, granularity="D")
    df.set_index("date", inplace=True)
    cols = list(map(lambda x: "{} {}".format(db_inst, x), df.columns))
    poll_df[cols] = df
    print(poll_df)
