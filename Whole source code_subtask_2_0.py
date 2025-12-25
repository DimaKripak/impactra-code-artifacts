import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.lines import Line2D
import numpy as np
import warnings
warnings.filterwarnings('ignore')

def load_data(file_name):
    try:
        data = pd.read_csv(file_name)
        return data
    except Exception as e:
        print(f'An error occurred: {e}')

def generate_chart(data):
    try:
        data['timestamp'] = pd.to_datetime(data['timestamp'], unit='s')
        plt.figure(figsize=(10,6))
        plt.plot(data['timestamp'], data['sqrtPriceX96'], label='sqrtPriceX96')
        plt.xlabel('Timestamp')
        plt.ylabel('sqrtPriceX96')
        plt.title('Data Visualization')
        plt.legend()
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f'An error occurred: {e}')

def main():
    file_name = 'ETH-USDC-500-10_2024-01-01-2025-10-23.csv'
    data = load_data(file_name)
    if data is not None:
        generate_chart(data)

main()