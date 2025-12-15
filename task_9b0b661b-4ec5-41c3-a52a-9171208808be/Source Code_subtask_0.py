import pandas as pd
import matplotlib.pyplot as plt

# Load the data
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Prepare the data for histogram
def prepare_data(data):
    # Ensure timestamp is in datetime format
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    
    # Calculate the change in sqrtPriceX96
    data['sqrtPriceX96_change'] = data['sqrtPriceX96'].diff()
    
    return data

# Generate histogram
def generate_histogram(data, bins=50, title="Histogram of sqrtPriceX96 Change"):
    plt.figure(figsize=(12, 6))
    plt.hist(data['sqrtPriceX96_change'].dropna(), bins=bins, alpha=0.7, color='g')
    plt.title(title)
    plt.xlabel('Change in sqrtPriceX96')
    plt.ylabel('Frequency')
    plt.show()

# Main function
def main():
    file_path = "ETH-USDC-500-10_2024-01-01-2025-10-23.csv"
    data = load_data(file_path)
    if data is not None:
        prepared_data = prepare_data(data)
        generate_histogram(prepared_data)

if __name__ == "__main__":
    main()