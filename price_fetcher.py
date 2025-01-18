import yfinance as yf

class PriceFetcher:
    def get_current_price(self, symbol, timeframe='1m'):
        """
        Fetches the current price of a given financial instrument symbol for a specified timeframe.

        Args:
            symbol (str): The ticker symbol of the financial instrument
                           (e.g., 'AAPL', 'EURUSD=X', 'BTC-USD').
            timeframe (str): The timeframe for which to fetch the price.
                             Common values include '1d' (daily), '1h' (hourly),
                             '30m' (30 minutes), '5m' (5 minutes), etc.
                             Default is '1d'.

        Returns:
            float: The last closing price within the specified timeframe, or None if an error occurs.
        """
        try:
            ticker = yf.Ticker(symbol)
            # Fetch historical data for the specified timeframe, retrieving only the most recent interval.
            todays_data = ticker.history(period='1d', interval=timeframe)
            if not todays_data.empty:
                return todays_data['Close'].iloc[-1]
            else:
                print(f"Could not retrieve price data for symbol: {symbol} with timeframe: {timeframe}")
                return None
        except Exception as e:
            print(f"Error fetching price for {symbol} with timeframe {timeframe}: {e}")
            return None

if __name__ == '__main__':
    fetcher = PriceFetcher()
    five_min_timeframe = '5m'

    # Examples for Currency and Crypto using 5-minute timeframe
    forex_symbol = "EURUSD=X"
    crypto_symbol = "BTC-USD"

    forex_price_5min = fetcher.get_current_price(forex_symbol)
    if forex_price_5min:
        print(f"The current price of {forex_symbol} (5-min) is: {forex_price_5min}")

    crypto_price_5min = fetcher.get_current_price(crypto_symbol)
    if crypto_price_5min:
        print(f"The current price of {crypto_symbol} (5-min) is: {crypto_price_5min}")

    # Example for a Stock (for comparison) using 5-minute timeframe
    stock_symbol = "AAPL"
    stock_price_5min = fetcher.get_current_price(stock_symbol)
    if stock_price_5min:
        print(f"The current price of {stock_symbol} (5-min) is: {stock_price_5min}")

    