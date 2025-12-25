[
  {
    "function": "load_data",
    "code": """
import pandas as pd

def load_data(file_name):
    # Load the csv file
    data = pd.read_csv(file_name)
    return data
""",
    "completionOrder": 1
  },
  {
    "function": "calculate_change_dynamic",
    "code": """
import pandas as pd

def calculate_change_dynamic(data, column_name):
    # Calculate the change dynamic
    data['change_dynamic'] = data[column_name].diff()
    return data
""",
    "completionOrder": 2
  },
  {
    "function": "whole_source_code",
    "code": """
import pandas as pd

def load_data(file_name):
    # Load the csv file
    data = pd.read_csv(file_name)
    return data

def calculate_change_dynamic(data, column_name):
    # Calculate the change dynamic
    data['change_dynamic'] = data[column_name].diff()
    return data

def main():
    file_name = 'ETH-USDC-500-10_2024-01-01-2025-10-23.csv'
    column_name = 'sqrtPriceX96'
    data = load_data(file_name)
    result = calculate_change_dynamic(data, column_name)
    print(result)

if __name__ == "__main__":
    main()
""",
    "completionOrder": 0
  }
]