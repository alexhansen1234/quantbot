import json
import pandas as pd
import quantlib.indicators_cal as indicators_cal

class Lbmom:
    def __init__(self, instruments_config, historical_df, simulation_start, vol_target):
        self.pairs = [(23, 44), (113, 240), (117, 234), (23, 24), (17, 178), (61, 250), (33, 251), (166, 275), (39, 130), (68, 78), (148, 156), (74, 101), (20, 47), (175, 193), (103, 238), (58, 194), (48, 150), (36, 153), (205, 278), (109, 215), (152, 193)]
        self.instruments_config = instruments_config
        self.historical_df = historical_df
        self.simulation_start = simulation_start
        self.vol_target = vol_target
        with open(instruments_config) as fp:
            self.instruments_config = json.load(fp)
        self.sysname = "LBMOM"

    def extend_historicals(self, instruments, historical_data):
        print(instruments)
        for inst in instruments:
            historical_data["{} adx".format(inst)] = indicators_cal.adx_series(
                high = historical_data["{} high".format(inst)],
                low = historical_data["{} low".format(inst)],
                close = historical_data["{} close".format(inst)],
                n = 14
            )
            for pair in self.pairs:
                # calculate the fastMA - slowMA
                historical_data["{} ema{}".format(inst, str(pair))] = indicators_cal.ema_series(historical_data["{} close".format(inst)], n = pair[0]) - \
                    indicators_cal.ema_series(historical_data["{} close".format(inst)], n = pair[1])
        return historical_data

    def run_simulation(self, historical_data):
        """
        Init Params
        """
        instruments = self.instruments_config["instruments"]

        """
        Pre-processing
        """
        historical_data = self.extend_historicals(instruments=instruments, historical_data=historical_data)
        print(historical_data)
        portfolio_df = pd.DataFrame(index=historical_data[self.simulation_start:].index).reset_index()
        portfolio_df.loc[0, "capital"] = 10000
        print(portfolio_df)

        """
        Run Simulation
        """

        pass

    def get_subsys_pos(self):
        self.run_simulation(historical_data=self.historical_df)

    def update_config(self, instruments, indent = 4):
        with open(self.instruments_config, 'w') as fp:
            json.dump({"instruments": instruments}, fp, indent = indent)
