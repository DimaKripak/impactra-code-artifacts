import pandas as pd
import matplotlib.pyplot as plt

# Load data
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Preprocess data
def preprocess_data(data):
    try:
        # Convert sqrtPriceX96 to numeric
        data['sqrtPriceX96'] = pd.to_numeric(data['sqrtPriceX96'])
        
        # Calculate change in sqrtPriceX96
        data['change_sqrtPriceX96'] = data['sqrtPriceX96'].diff()
        
        return data
    except Exception as e:
        print(f"Error preprocessing data: {e}")
        return None

# Generate histogram
def generate_histogram(data):
    try:
        # Filter out NaN values
        data_filtered = data.dropna(subset=['change_sqrtPriceX96'])
        
        # Create histogram
        plt.hist(data_filtered['change_sqrtPriceX96'], bins=50)
        plt.title('Histogram of Change in sqrtPriceX96')
        plt.xlabel('Change in sqrtPriceX96')
        plt.ylabel('Frequency')
        plt.show()
    except Exception as e:
        print(f"Error generating histogram: {e}")

# Main function
def main():
    file_path = "ETH-USDC-500-10_2024-01-01-2025-10-23.csv"
    data = load_data(file_path)
    if data is not None:
        data = preprocess_data(data)
        if data is not None:
            generate_histogram(data)

if __name__ == "__main__":
    main()