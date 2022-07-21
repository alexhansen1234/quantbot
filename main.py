import json
import pandas as pd

from dateutil.relativedelta import relativedelta

import quantlib.data_utils as du
import quantlib.general_utils as gu

from subsystems.LBMOM.subsys import Lbmom

df, instruments = du.get_sp500_df()
df = du.extend_dataframe(traded=instruments, df=df)
gu.save_file("./Data/data.obj", (df, instruments))

df, instruments = gu.load_file("./Data/data.obj")
print(df, instruments)

with open("./subsystems/LBMOM/config.json", "w") as fp:
    json.dump({'instruments': instruments}, fp, indent = 4)

# run simulation for 5 years
VOL_TARGET = 0.20
print(df.index[-1])
sim_start = df.index[-1] - relativedelta(years=5)
print(sim_start)

strat = Lbmom(instruments_config="./subsystems/LBMOM/config.json", historical_df=df, simulation_start=sim_start, vol_target=VOL_TARGET)
strat.get_subsys_pos()
