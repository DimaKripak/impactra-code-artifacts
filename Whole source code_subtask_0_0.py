import pandas as pd

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f'Error loading data: {e}')

def cast_column_to_numeric(data, column_name):
    try:
        data[column_name] = pd.to_numeric(data[column_name], errors='coerce')
        return data
    except Exception as e:
        print(f'Error casting column to numeric: {e}')

def main():
    file_path = 'ETH-USDC-500-10_2024-01-01-2025-10-23.csv'
    data = load_data(file_path)
    data = cast_column_to_numeric(data, 'sqrtPriceX96')
    print(data.head())

if __name__ == '__main__':
    main()