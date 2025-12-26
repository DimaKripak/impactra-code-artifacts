import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

def load_data(file_name):
    try:
        data = pd.read_csv(file_name)
        return data
    except FileNotFoundError:
        print(f'The file {file_name} was not found.')
        return None

def prepare_data(data):
    data['date'] = pd.to_datetime(data['timestamp'], unit='s')
    return data

def generate_chart(data):
    plt.figure(figsize=(10,6))
    plt.plot(data['date'], data['sqrtPriceX96'])
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gcf().autofmt_xdate()
    plt.title('Change Dynamics of sqrtPriceX96 Over Time')
    plt.xlabel('Date')
    plt.ylabel('sqrtPriceX96')
    plt.grid(True)
    plt.show()

def main():
    file_name = 'ETH-USDC-500-10_2024-01-2025-10-23.csv'
    data = load_data(file_name)
    if data is not None:
        data = prepare_data(data)
        generate_chart(data)

if __name__ == '__main__':
    main()