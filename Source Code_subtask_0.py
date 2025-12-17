import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data from CSV file
def load_data(file_name):
    try:
        data = pd.read_csv(file_name)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Convert timestamp to datetime and sqrtPriceX96 to numeric
def prepare_data(data):
    try:
        data['timestamp'] = pd.to_datetime(data['timestamp'], unit='s')
        data['sqrtPriceX96'] = pd.to_numeric(data['sqrtPriceX96'])
        return data
    except Exception as e:
        print(f"Error preparing data: {e}")
        return None

# Calculate changes in sqrtPriceX96
def calculate_changes(data):
    try:
        data['changes'] = data['sqrtPriceX96'].diff()
        return data
    except Exception as e:
        print(f"Error calculating changes: {e}")
        return None

# Generate histogram
def generate_histogram(data):
    try:
        plt.hist(data['changes'].dropna(), bins=50)
        plt.title('Histogram of sqrtPriceX96 Change Dynamics')
        plt.xlabel('Changes')
        plt.ylabel('Frequency')
        plt.show()
    except Exception as e:
        print(f"Error generating histogram: {e}")

# Main function
def main():
    file_name = 'ETH-USDC-500-10_2024-01-01-2025-10-23.csv'
    data = load_data(file_name)
    if data is not None:
        data = prepare_data(data)
        if data is not None:
            data = calculate_changes(data)
            if data is not None:
                generate_histogram(data)

if __name__ == "__main__":
    main()