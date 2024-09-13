# strategy.py

import pandas as pd
from indicators import Indicators

class Strategies:
    def __init__(self):
        self.indicators = Indicators()
        self.high_rsi = 80
        self.low_rsi = 20

    def prepare_dataframe(self, historical_data):
        df = pd.DataFrame(historical_data)
        df.columns = ["timestamp", "open", "high", "low", "close", "volume", "turnover"]
        df['close'] = df['close'].astype(float)
        df.sort_values('timestamp', inplace=True)
        return df

    def mean_reversion_strategy(self, df):
        rsi = df['RSI'].iloc[-1]
        current_price = df['close'].iloc[-1]
        bollinger_upper = df['Bollinger_upper'].iloc[-1]
        bollinger_lower = df['Bollinger_lower'].iloc[-1]

        # Check for overbought (short) or oversold (long) conditions

        if current_price + 60 >= bollinger_upper:
            return 'short'
        elif current_price - 60 <= bollinger_lower:
            return 'long'
        return None
        # if rsi > self.high_rsi or current_price + 50 >= bollinger_upper:
        #     return 'short'
        # elif rsi < self.low_rsi or current_price - 50 <= bollinger_lower:
        #     return 'long'
        # return None
    
        # if rsi > 50:
        #     return 'long'
        # elif rsi < 50:
        #     return 'short'
        # return None

