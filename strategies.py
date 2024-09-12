# strategy.py

import pandas as pd
from indicators import Indicators

class Strategies:
    def __init__(self):
        self.indicators = Indicators()
        self.high_rsi = 85
        self.low_rsi = 15

    def prepare_dataframe(self, historical_data):
        df = pd.DataFrame(historical_data)
        df.columns = ["timestamp", "open", "high", "low", "close", "volume", "turnover"]
        df['close'] = df['close'].astype(float)
        df.sort_values('timestamp', inplace=True)
        return df

    def calculate_margin(self, price, percent=0.17):
        """
        Calculate the margin based on the given percentage.
        
        Args:
            price (float): The base price to calculate the margin from.
            percent (float): The percentage to calculate, default is 0.17%.
            
        Returns:
            float: The calculated margin.
        """
        margin = price * (percent / 100)
        return margin

    def mean_reversion_strategy(self, df):
        rsi = df['RSI'].iloc[-1]
        current_price = df['close'].iloc[-1]
        bollinger_upper = df['Bollinger_upper'].iloc[-1]
        bollinger_lower = df['Bollinger_lower'].iloc[-1]

        # Calculate the extra margin (0.17% of current_price)
        extra_margin = self.calculate_margin(current_price, 0.13)

        # Check for overbought (short) or oversold (long) conditions
        if rsi > self.high_rsi or current_price >= (bollinger_upper + extra_margin):
            return 'short'
        elif rsi < self.low_rsi or current_price <= (bollinger_lower - extra_margin):
            return 'long'
        return None
