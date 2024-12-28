# Install required libraries (run this in your terminal, not in the script)
# pip install pandas yfinance matplotlib

import yfinance as yf
import matplotlib.pyplot as plt

def fetch_stock_data(ticker):
    """Fetches real-time stock data from Yahoo Finance."""
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")  # Get the latest data
    return data

class Portfolio:
    def __init__(self):
        self.stocks = {}  # Corrected variable name to 'stocks'

    def add_stock(self, ticker, quantity):
        """Adds a stock to the portfolio."""
        if ticker in self.stocks:
            self.stocks[ticker] += quantity
        else:
            self.stocks[ticker] = quantity
        print(f"Added {quantity} shares of {ticker}.")

    def remove_stock(self, ticker, quantity):
        """Removes a stock from the portfolio."""
        if ticker in self.stocks and self.stocks[ticker] >= quantity:
            self.stocks[ticker] -= quantity
            if self.stocks[ticker] == 0:
                del self.stocks[ticker]
            print(f"Removed {quantity} shares of {ticker}.")
        else:
            print(f"Cannot remove {quantity} shares of {ticker}. Not enough shares.")

    def view_portfolio(self):
        """Displays the current portfolio."""
        return self.stocks
    
    def calculate_portfolio_value(self):
        """Calculates the total value of the portfolio."""
        total_value = 0
        for ticker, quantity in self.stocks.items():
            stock_data = fetch_stock_data(ticker)
            current_price = stock_data['Close'].iloc[-1]  # Get the latest closing price
            total_value += current_price * quantity
        return total_value 

def plot_stock_performance(ticker):
    """Plots the stock performance over time."""
    stock_data = fetch_stock_data(ticker)
    stock_data['Close'].plot(title=f"{ticker} Stock Price", figsize=(10, 5))
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.show() 

if __name__ == "__main__":
    my_portfolio = Portfolio()
    
    # Adding stocks
    my_portfolio.add_stock("AAPL", 10)  # Add 10 shares of Apple
    my_portfolio.add_stock("GOOGL", 5)  # Add 5 shares of Google
    
    # Viewing portfolio
    print("Current Portfolio:", my_portfolio.view_portfolio())
    
    # Calculating portfolio value
    total_value = my_portfolio.calculate_portfolio_value()
    print(f"Total Portfolio Value: ${total_value:.2f}")
    
    # Removing stocks
    my_portfolio.remove_stock("AAPL", 5)  # Remove 5 shares of Apple
    print("Updated Portfolio:", my_portfolio.view_portfolio())      

    # Plotting stock performance for AAPL
    plot_stock_performance("AAPL")