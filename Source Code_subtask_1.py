[
  {
    "function": "load_data",
    "code": """
import pandas as pd
def load_data(file_path):
    # Load the data from the CSV file
    data = pd.read_csv(file_path)
    return data
""",
    "completionOrder": 1
  },
  {
    "function": "calculate_change_dynamic",
    "code": """
import pandas as pd
def calculate_change_dynamic(data):
    # Calculate the change dynamic of 'sqrtPriceX96' over time
    data['sqrtPriceX96_change'] = data['sqrtPriceX96'].diff()
    data['timestamp'] = pd.to_datetime(data['timestamp'], unit='s')
    data.set_index('timestamp', inplace=True)
    return data
""",
    "completionOrder": 2
  },
  {
    "function": "analyze_time_series",
    "code": """
import matplotlib.pyplot as plt
def analyze_time_series(data):
    # Analyze the time-series data
    plt.figure(figsize=(10,6))
    plt.plot(data.index, data['sqrtPriceX96'])
    plt.xlabel('Time')
    plt.ylabel('sqrtPriceX96')
    plt.title('Time Series Analysis')
    plt.show()
    return data
""",
    "completionOrder": 3
  },
  {
    "function": "whole_source_code",
    "code": """
import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    # Load the data from the CSV file
    data = pd.read_csv(file_path)
    return data

def calculate_change_dynamic(data):
    # Calculate the change dynamic of 'sqrtPriceX96' over time
    data['sqrtPriceX96_change'] = data['sqrtPriceX96'].diff()
    data['timestamp'] = pd.to_datetime(data['timestamp'], unit='s')
    data.set_index('timestamp', inplace=True)
    return data

def analyze_time_series(data):
    # Analyze the time-series data
    plt.figure(figsize=(10,6))
    plt.plot(data.index, data['sqrtPriceX96'])
    plt.xlabel('Time')
    plt.ylabel('sqrtPriceX96')
    plt.title('Time Series Analysis')
    plt.show()
    return data

def main():
    file_path = 'ETH-USDC-500-10_2024-01-01-2025-10-23.csv'
    data = load_data(file_path)
    data = calculate_change_dynamic(data)
    data = analyze_time_series(data)

if __name__ == "__main__":
    main()
""",
    "completionOrder": 0
  }
]