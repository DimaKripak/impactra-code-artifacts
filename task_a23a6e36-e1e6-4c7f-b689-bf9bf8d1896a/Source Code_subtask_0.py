import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data
def load_data(file_path):
    try:
        # Attempt to read csv file
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Failed to load data: {e}")
        return None

# Convert columns to numeric
def convert_to_numeric(data, columns):
    for column in columns:
        try:
            data[column] = pd.to_numeric(data[column], errors='coerce')
        except Exception as e:
            print(f"Failed to convert {column} to numeric: {e}")
    return data

# Calculate the change in sqrtPriceX96
def calculate_change(data):
    try:
        # Ensure timestamp is in datetime format
        data['timestamp'] = pd.to_datetime(data['timestamp'])
        
        # Sort by timestamp
        data = data.sort_values(by='timestamp')
        
        # Calculate change
        data['sqrtPriceX96_change'] = data['sqrtPriceX96'].diff()
        return data
    except Exception as e:
        print(f"Failed to calculate change: {e}")
        return None

# Generate histogram
def generate_histogram(data, column):
    try:
        # Drop NaN values
        data = data.dropna(subset=[column])
        
        # Generate histogram
        plt.hist(data[column], bins=50)
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.title(f'Histogram of {column}')
        plt.show()
    except Exception as e:
        print(f"Failed to generate histogram: {e}")

# Main function
def main():
    file_path = 'ETH-USDC-500-10_2024-01-01-2025-10-23.csv'
    data = load_data(file_path)
    
    if data is not None:
        columns = ['sqrtPriceX96']
        data = convert_to_numeric(data, columns)
        
        if data is not None:
            data = calculate_change(data)
            
            if data is not None:
                column = 'sqrtPriceX96_change'
                generate_histogram(data, column)

if __name__ == "__main__":
    main()