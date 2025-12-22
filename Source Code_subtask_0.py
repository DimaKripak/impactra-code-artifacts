[
  {
    "function": "load_data",
    "code": """
import pandas as pd
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data
""",
    "completionOrder": 1
  },
  {
    "function": "cast_column_to_numeric",
    "code": """
def cast_column_to_numeric(data, column_name):
    data[column_name] = pd.to_numeric(data[column_name])
    return data
""",
    "completionOrder": 2
  },
  {
    "function": "whole_source_code",
    "code": """
import pandas as pd

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def cast_column_to_numeric(data, column_name):
    data[column_name] = pd.to_numeric(data[column_name])
    return data

def main():
    file_path = 'ETH-USDC-500-10_2024-01-01-2025-10-23.csv'
    data = load_data(file_path)
    data = cast_column_to_numeric(data, 'sqrtPriceX96')
    print(data.head())

if __name__ == "__main__":
    main()
""",
    "completionOrder": 0
  }
]